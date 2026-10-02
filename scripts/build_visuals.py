#!/usr/bin/env python3
"""Build original, dependency-free SVG artwork for the profile."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets'
PALETTES = {
    'dark': dict(bg='#111119', panel='#191923', ink='#f5f1ff', muted='#b0a8c2', line='#393345', purple='#bfa3ff', rose='#e7a5c6', mint='#9cd9c5', amber='#f0c58d'),
    'light': dict(bg='#f5f2fa', panel='#ffffff', ink='#30263f', muted='#70617e', line='#d6cde1', purple='#7650ad', rose='#a4517d', mint='#367b66', amber='#966522'),
}

def svg(w, h, title, body, p, animated=False):
    motion = '''
.flow{stroke-dasharray:7 17;animation:flow 4s linear infinite}
.signal{animation:signal 14s ease-in-out infinite}
.gate{animation:gate 14s ease-in-out infinite}
.replay{stroke-dasharray:6 12;animation:replay 14s linear infinite}
.orbit{transform-origin:920px 221px;animation:orbit 70s linear infinite}
@keyframes flow{to{stroke-dashoffset:-96}}
@keyframes signal{0%,5%{opacity:.2}18%,37%{opacity:1}48%,100%{opacity:.2}}
@keyframes gate{0%,30%{opacity:.3}38%,57%{opacity:1}70%,100%{opacity:.3}}
@keyframes replay{0%,57%{opacity:0;stroke-dashoffset:0}63%{opacity:1}92%{opacity:1;stroke-dashoffset:120}100%{opacity:0;stroke-dashoffset:150}}
@keyframes orbit{to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){.flow,.signal,.gate,.replay,.orbit{animation:none!important}.replay{opacity:.5}}
''' if animated else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">Original illustration by Heggria. Workflow animation is a schematic, not a live run.</desc>
<defs>
<radialGradient id="glow"><stop stop-color="{p['purple']}" stop-opacity=".19"/><stop offset="1" stop-color="{p['purple']}" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="{p['muted']}" opacity=".2"/></pattern>
</defs>
<style>text{{font-family:Arial,Helvetica,sans-serif;fill:{p['ink']}}}.mono{{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}}.muted{{fill:{p['muted']}}}{motion}</style>
<rect width="{w}" height="{h}" rx="24" fill="{p['bg']}"/>
{body}
</svg>\n'''

def text(x,y,s,size=16,cls='',extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" class="{cls}" {extra}>{escape(s)}</text>'

def graph(p, mobile=False):
    # Normalized diagram, also reused on mobile; no scripts or external resources.
    b=f'<circle cx="280" cy="160" r="218" fill="url(#glow)"/>'
    b+=f'<g fill="none" stroke="{p["line"]}"><circle cx="280" cy="160" r="155"/><circle cx="280" cy="160" r="190" stroke-dasharray="2 12"/></g>'
    paths=['M38 160H92Q108 160 108 144V98Q108 82 124 82H170', 'M38 160H92Q108 160 108 176V222Q108 238 124 238H170', 'M220 82H260Q276 82 276 98V144Q276 160 292 160H322', 'M220 238H260Q276 238 276 222V176Q276 160 292 160H322']
    for d in paths:
        b+=f'<path d="{d}" fill="none" stroke="{p["line"]}" stroke-width="2"/><path class="flow signal" d="{d}" fill="none" stroke="{p["purple"]}" stroke-width="2"/>'
    b+=f'<path d="M366 160H432" stroke="{p["line"]}" stroke-width="2" stroke-dasharray="4 6"/>'
    b+=f'<path d="M344 188V284Q344 306 322 306H60Q38 306 38 284V191" fill="none" stroke="{p["line"]}" stroke-width="1.5"/>'
    b+=f'<path class="replay" d="M344 188V284Q344 306 322 306H60Q38 306 38 284V191" fill="none" stroke="{p["rose"]}" stroke-width="2.5"/>'
    for x,y,label in [(38,160,'PLAN'),(195,82,'BUILD'),(195,238,'CHECK')]:
        b+=f'<rect x="{x-23}" y="{y-23}" width="46" height="46" rx="13" fill="{p["panel"]}" stroke="{p["purple"]}" stroke-width="1.5"/>'
        b+=f'<circle class="signal" cx="{x}" cy="{y}" r="6" fill="{p["purple"]}"/>'
        b+=text(x,y-38,label,13,'mono muted','text-anchor="middle"')
    b+=f'<rect x="326" y="142" width="36" height="36" rx="6" transform="rotate(45 344 160)" fill="{p["panel"]}" stroke="{p["amber"]}" stroke-width="2"/>'
    b+=f'<path class="gate" d="M339 151V169M349 151V169" stroke="{p["amber"]}" stroke-width="3"/>'
    b+=text(344,117,'VERIFY',13,'mono muted','text-anchor="middle"')
    b+=f'<circle cx="446" cy="160" r="14" fill="{p["panel"]}" stroke="{p["line"]}" stroke-width="2"/>'
    b+=f'<path d="M440 160H452" stroke="{p["muted"]}" stroke-width="2"/>'
    b+=text(446,201,'HELD',12,'mono muted','text-anchor="middle"')
    b+=text(188,335,'↶  REPLAY THE TRACE',12,'mono muted','text-anchor="middle"')
    return b

for theme,p in PALETTES.items():
    b='<rect x="620" y="20" width="560" height="430" fill="url(#dots)"/>'
    b+=text(48,51,'H / PERSONAL LAB',14,'mono muted','letter-spacing="2"')
    b+=text(1152,51,'BEIJING · OPEN SOURCE',12,'mono muted','text-anchor="end" letter-spacing="1"')
    b+=text(46,155,'HEGGRIA',82,'','font-weight="750" letter-spacing="-5"')
    b+=text(50,228,'Work that',40,'','font-weight="400" letter-spacing="-1.5"')
    b+=text(50,277,'outlives the chat.',40,'','font-weight="400" letter-spacing="-1.5"')
    b+=text(51,325,'Agent systems. Thoughtful tools.',17,'muted')
    b+=f'<g transform="translate(654 42)">{graph(p)}</g>'
    b+=f'<path d="M48 400H1152" stroke="{p["line"]}"/>'
    b+=f'<circle cx="55" cy="437" r="4" fill="{p["purple"]}"/>'
    b+=text(70,442,'BUILD / VERIFY / REPLAY',12,'mono muted','letter-spacing="1"')
    b+=text(1152,442,'WORKFLOW STUDY 001 · ANIMATED SCHEMATIC',11,'mono muted','text-anchor="end"')
    (OUT/f'hero-{theme}.svg').write_text(svg(1200,480,'Heggria — Work that outlives the chat. A workflow branches, pauses at verification, and replays its trace.',b,p,True))
    b='<rect x="20" y="235" width="560" height="390" fill="url(#dots)"/>'
    b+=text(32,44,'H / PERSONAL LAB',15,'mono muted','letter-spacing="2"')
    b+=text(28,133,'HEGGRIA',81,'','font-weight="750" letter-spacing="-4"')
    b+=text(32,187,'Work that outlives the chat.',26,'','letter-spacing="-.8"')
    b+=text(32,220,'Agent systems. Thoughtful tools.',18,'muted')
    b+=f'<g transform="translate(46 253) scale(1.08)">{graph(p,True)}</g>'
    b+=f'<path d="M32 653H568" stroke="{p["line"]}"/>'
    b+=text(32,686,'WORKFLOW STUDY 001',13,'mono muted','letter-spacing="1"')
    b+=text(568,686,'ANIMATED SCHEMATIC',12,'mono muted','text-anchor="end"')
    (OUT/f'hero-mobile-{theme}.svg').write_text(svg(600,720,'Heggria — Work that outlives the chat. Workflow schematic.',b,p,True))

    for name,number,label,subtitle in [('taskflow','01','taskflow','AGENT WORKFLOWS'),('opendesign','02','OpenDesign','AT WORK'),('selffield','03','SelfField','PERSONAL EXPERIMENT')]:
        b=f'<rect x="460" y="0" width="540" height="210" fill="url(#dots)"/>'
        b+=text(32,40,number+' / '+subtitle,12,'mono muted','letter-spacing="1.5"')
        b+=text(30,110,label,50,'','font-weight="600" letter-spacing="-2"')
        if name=='taskflow':
            b+=text(32,160,'Make the run inspectable.',18,'muted')
            for y in [55,105,155]:
                b+=f'<path d="M544 105H596Q608 105 608 {y}H679Q691 {y} 691 105H735" fill="none" stroke="{p["purple"]}" stroke-width="2"/>'
                b+=f'<rect x="628" y="{y-13}" width="40" height="26" rx="7" fill="{p["panel"]}" stroke="{p["purple"]}"/>'
            b+=f'<circle cx="536" cy="105" r="12" fill="{p["purple"]}"/><rect x="738" y="89" width="32" height="32" rx="5" transform="rotate(45 754 105)" fill="{p["panel"]}" stroke="{p["amber"]}" stroke-width="2"/><path d="M784 105H848" stroke="{p["line"]}" stroke-width="2" stroke-dasharray="5 5"/><circle cx="864" cy="105" r="12" fill="none" stroke="{p["line"]}" stroke-width="2"/>'
        elif name=='opendesign':
            b+=text(32,160,'Design meets engineering.',18,'muted')
            for x,y,w,h in [(552,37,150,127),(706,59,143,99)]:
                b+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{p["panel"]}" stroke="{p["line"]}"/>'
            b+=f'<rect x="572" y="58" width="111" height="68" rx="7" fill="{p["purple"]}" opacity=".15"/><circle cx="646" cy="92" r="21" fill="{p["rose"]}" opacity=".7"/><path d="M571 145H656M724 81H812M724 100H792M724 134H764" stroke="{p["muted"]}" stroke-width="5" stroke-linecap="round"/>'
            b+=f'<rect x="551" y="36" width="153" height="130" rx="0" fill="none" stroke="{p["purple"]}" stroke-dasharray="4 5"/>'
            for x,y in [(551,36),(704,36),(551,166),(704,166)]:b+=f'<rect x="{x-3}" y="{y-3}" width="6" height="6" fill="{p["purple"]}"/>'
        else:
            b+=text(32,160,'A mirror, without the labels.',18,'muted')
            for rad in [26,49,74]:b+=f'<circle cx="722" cy="105" r="{rad}" fill="none" stroke="{p["line"]}"/>'
            b+=f'<path d="M722 31L778 75L764 144L684 158L662 86Z" fill="{p["purple"]}" fill-opacity=".11" stroke="{p["purple"]}" stroke-width="2"/>'
            for x,y in [(722,31),(778,75),(764,144),(684,158),(662,86)]:b+=f'<circle cx="{x}" cy="{y}" r="4" fill="{p["rose"]}"/>'
            b+=f'<circle cx="722" cy="105" r="7" fill="{p["purple"]}"/>'
        (OUT/f'{name}-{theme}.svg').write_text(svg(940,210,f'{label} — {subtitle}. Conceptual illustration.',b,p))
print('Built 10 SVG assets (desktop/mobile hero + three project illustrations, light/dark).')
