"""Comprueba las páginas generadas y todos sus enlaces internos."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls=[]
        self.h1=0
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        self.h1+=t=='h1'
        for k in ('href','src'):
            if a.get(k,'').startswith('/'): self.urls.append(urlsplit(a[k]).path)
out=Path('dist')
pages=list(out.rglob('*.html'))
bad=[]
for p in pages:
    h=Check()
    h.feed(p.read_text())
    if h.h1!=1: bad.append((str(p),h.h1))
    for u in h.urls:
        if not (out/u.lstrip('/')).exists(): bad.append((str(p),u))
assert pages and not bad,bad[:20]
print(f'{len(pages)} páginas verificadas')
