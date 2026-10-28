from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import json,re
R=Path(__file__).resolve().parents[1];cfg=json.loads((R/'publication.json').read_text());base=cfg['base_path'].rstrip('/');D=R/'_site';errors=[];links=0
def exact_case(path):
 here=D
 for part in path.relative_to(D).parts:
  if part not in {p.name for p in here.iterdir()}:return False
  here=here/part
 return True
for p in D.rglob('*.html'):
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for el in s.find_all(True):
  for attr in ['src','href']:
   value=el.get(attr)
   if not value or not value.startswith('/') or value.startswith('//'):continue
   links+=1;path=unquote(urlsplit(value).path)
   if not path.startswith(base+'/'):errors.append([str(p.relative_to(D)),value,'outside project path']);continue
   target=D/path[len(base)+1:]
   if not(target.is_file() or (target/'index.html').is_file()):errors.append([str(p.relative_to(D)),value,'missing target'])
   elif not exact_case(target):errors.append([str(p.relative_to(D)),value,'case mismatch on Linux'])
for lang in ['de','en']:
 for row in json.loads((D/'assets/data.json').read_text(encoding='utf-8'))['routes'][lang].values():
  assert row.startswith(base+'/'),row
 for row in json.loads((R/'inhalte'/('materialkatalog.json' if lang=='de' else 'materialkatalog-en.json')).read_text(encoding='utf-8')):
  for url in row['formats'].values():assert (D/url.lstrip('/')).exists(),url
report={'linksChecked':links,'errors':errors};(R/'reports/link-check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
assert not errors,errors[:15]
print('PASS',links,'project-prefixed HTML links and all registered resources')
