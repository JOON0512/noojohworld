from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, re
root=Path(__file__).resolve().parents[1]/'docs'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=[];self.links=[];self.h1=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag in ('a','link','script'):
   url=a.get('href',a.get('src',''))
   if url:self.links.append(url)
pages={p.resolve():Page(p.read_text()) for p in root.rglob('*.html')}
errors=[]
for path,p in pages.items():
 if p.h1!=1:errors.append(f'{path.name}: expected 1 h1')
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{path.name}: duplicate IDs')
 for url in p.links:
  u=urlsplit(url)
  if u.scheme or u.netloc:continue
  dest=(path.parent/unquote(u.path)).resolve() if u.path else path
  if not dest.exists():errors.append(f'{path.name}: missing {url}')
  elif u.fragment and dest in pages and u.fragment not in pages[dest].ids:errors.append(f'{path.name}: missing anchor {url}')
projects=json.loads((root/'data/projects.json').read_text())
assert len({p['id'] for p in projects})==len(projects), 'Duplicate project IDs'
for item in json.loads((root/'data/videos.json').read_text()):
 assert re.fullmatch(r'[\w-]{11}', item['id']) and isinstance(item['title'],str), 'Invalid video metadata'
assert not errors,errors
print(f'PASS: {len(pages)} pages; headings, IDs, local links, asset paths, project IDs, video metadata')
