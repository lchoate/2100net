from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
root=Path(__file__).parent/'dist'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.ids=[];self.h1=0;self.images=[];self.title='';self.in_title=False;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.in_title=True
  if tag=='img':self.images.append(a)
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
 def handle_endtag(self,tag):
  if tag=='title':self.in_title=False
 def handle_data(self,data):
  if self.in_title:self.title+=data
pages={p.name:Page(p.read_text()) for p in root.glob('*.html')}
errors=[]
for name,p in pages.items():
 if p.h1!=1:errors.append(f'{name}: expected one h1')
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{name}: duplicate ids')
 for im in p.images:
  if not im.get('alt'):errors.append(f'{name}: image without description')
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=root/unquote(u.path or name)
  if not target.is_file():errors.append(f'{name}: missing {link}')
  elif u.fragment and target.suffix=='.html' and u.fragment not in pages[target.name].ids:errors.append(f'{name}: missing anchor {link}')
if len(set(p.title for p in pages.values()))!=len(pages):errors.append('Duplicate page titles')
assert len(pages)==9,f'Expected 9 pages, got {len(pages)}'
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages; local links, anchors, images, headings and titles validated.')
