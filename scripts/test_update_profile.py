"""Behavior checks for the scheduled public-profile writer."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError
import update_profile as updater

RELEASE = {'draft': False, 'prerelease': True, 'published_at': '2026-08-20T00:00:00Z', 'tag_name': 'v1', 'html_url': 'https://github.com/heggria/taskflow/releases/tag/v1'}
BASE = 'Intro\n<!-- releases:start -->\nold release\n<!-- releases:end -->\n<!-- writing:start -->\nold post\n<!-- writing:end -->\nOutro'
FEED = b'''<rss><channel><item><title>Latest post</title><link>https://heggria.github.io/writing/latest/</link><pubDate>Fri, 14 Aug 2026 16:00:00 GMT</pubDate></item></channel></rss>'''

class ProfileRefreshTests(unittest.TestCase):
    def run_in_temp(self, action):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text(BASE)
            with patch.object(updater, 'ROOT', root):
                action(root / 'README.md')

    def test_failed_second_source_preserves_published_content(self):
        def action(path):
            with patch.object(updater, 'fetch', side_effect=[json.dumps([RELEASE]).encode(), URLError('fixture: feed unavailable')]):
                with self.assertRaises(URLError): updater.main()
            self.assertEqual(path.read_text(), BASE)
        self.run_in_temp(action)

    def test_refresh_preserves_surroundings_and_is_idempotent(self):
        def action(path):
            with patch.object(updater, 'fetch', side_effect=[json.dumps([RELEASE]).encode(), FEED]*2):
                updater.main(); first=path.read_bytes(); updater.main()
            self.assertEqual(path.read_bytes(), first)
            self.assertTrue(path.read_text().startswith('Intro\n'))
            self.assertTrue(path.read_text().endswith('\nOutro'))
            self.assertIn('prerelease', path.read_text())
            self.assertIn('Latest post', path.read_text())
        self.run_in_temp(action)

    def test_draft_never_becomes_published_release(self):
        draft = dict(RELEASE, draft=True, tag_name='private-draft')
        rows=updater.release_lines(json.dumps([draft, RELEASE]))
        self.assertNotIn('private-draft', rows)
        self.assertIn('[taskflow v1]', rows)

    def test_missing_or_duplicate_markers_fail_without_writing(self):
        for text in ['missing', '<!-- writing:end --><!-- writing:start -->', '<!-- writing:start --><!-- writing:start --><!-- writing:end -->']:
            with self.subTest(text=text), self.assertRaises(ValueError): updater.replace_section(text, 'writing', 'new')

    def test_unexpected_feed_link_is_rejected(self):
        with self.assertRaises(ValueError): updater.writing_lines(FEED.replace(b'https://heggria.github.io/writing/latest/', b'https://example.com/unrelated/'))

if __name__ == '__main__': unittest.main()
