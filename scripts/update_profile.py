#!/usr/bin/env python3
"""Refresh two small README sections from public sources, without dependencies."""
import json
import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


def fetch(url):
    headers = {'User-Agent': 'heggria-profile', 'Accept': 'application/json' if 'api.github.com' in url else 'application/xml'}
    token = os.environ.get('GH_TOKEN')
    if token and url.startswith('https://api.github.com/'):
        headers['Authorization'] = f'Bearer {token}'
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
        return response.read()


def md(value):
    return re.sub(r'([\\`*{}\[\]<>])', r'\\\1', ' '.join(value.split()))


def release_lines(raw):
    releases = [r for r in json.loads(raw) if not r['draft'] and r.get('published_at')]
    releases.sort(key=lambda r: r['published_at'], reverse=True)
    if not releases:
        raise ValueError('No public releases; retaining previous README')
    rows = []
    for r in releases[:2]:
        if not r['html_url'].startswith('https://github.com/heggria/taskflow/releases/'):
            raise ValueError('Unexpected release URL')
        date = r['published_at'][:10]
        state = ' · prerelease' if r['prerelease'] else ''
        rows.append(f"- `{date}` [taskflow {md(r['tag_name'])}]({r['html_url']}){state}")
    return '\n'.join(rows)


def writing_lines(raw):
    items = ET.fromstring(raw).findall('./channel/item')
    now = datetime.now(timezone.utc)
    dated = [(parsedate_to_datetime(i.findtext('pubDate')), i) for i in items]
    dated = sorted(((d, i) for d, i in dated if d <= now), key=lambda pair: pair[0], reverse=True)[:2]
    if not dated:
        raise ValueError('No published posts; retaining previous README')
    rows = []
    for d, i in dated:
        url = i.findtext('link')
        if not url or not url.startswith('https://heggria.github.io/writing/'):
            raise ValueError('Unexpected writing URL')
        date = d.astimezone(ZoneInfo('Asia/Shanghai')).date().isoformat()
        rows.append(f"- `{date}` [{md(i.findtext('title') or 'Untitled')}]({url})")
    return '\n'.join(rows)


def replace_section(text, name, content):
    start, end = f'<!-- {name}:start -->', f'<!-- {name}:end -->'
    if text.count(start) != 1 or text.count(end) != 1 or text.index(start) >= text.index(end):
        raise ValueError(f'Invalid {name} section markers')
    return text[:text.index(start) + len(start)] + '\n' + content + '\n' + text[text.index(end):]


def main():
    path = ROOT / 'README.md'
    old = path.read_text()
    # Fetch and validate both sources before changing anything on disk.
    releases = release_lines(fetch('https://api.github.com/repos/heggria/taskflow/releases?per_page=20'))
    writing = writing_lines(fetch('https://heggria.github.io/rss.xml'))
    updated = replace_section(replace_section(old, 'releases', releases), 'writing', writing)
    if updated != old:
        path.write_text(updated)
        print('Updated releases and writing.')
    else:
        print('Already up to date.')


if __name__ == '__main__':
    main()
