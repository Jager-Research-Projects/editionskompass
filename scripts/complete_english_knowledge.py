"""Bring all English node explanations and graph relationships to DE content parity."""
from pathlib import Path
import json,re,sys,html
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def norm(s):return re.sub(r'\s+',' ',html.unescape(str(s))).strip()
MAP=json.loads((R/'inhalte/uebersetzung/en.json').read_text(encoding='utf-8'))
def t(s):return MAP.get(norm(s),MAP.get(s,s))
p=R/'inhalte/wissen.json';w=json.loads(p.read_text(encoding='utf-8'))
for n in w['nodes']:
 fields=['detail'] if n['kind']=='M' else ['surprise','utility','limits'];n['en']['detail']=' '.join(t(n[k]) for k in fields if n.get(k))
p.write_text(json.dumps(w,ensure_ascii=False,indent=2),encoding='utf-8')
p=R/'inhalte/module/discovery/index.html';h=p.read_text(encoding='utf-8');raw=re.search(r'<script id="data" type="application/json">(.*?)</script>',h,re.S);d=json.loads(raw.group(1));by_id={n['id']:n for n in w['nodes']}
for n in d['nodes']:n['en']=by_id[n['id']]['en']
for r in d['relations']:
 for key,value in r.items():
  if key not in ['a','b','direction','en'] and isinstance(value,str):r.setdefault('en',{})[key]=t(value)
h=h[:raw.start(1)]+json.dumps(d,ensure_ascii=False)+h[raw.end(1):];p.write_text(h,encoding='utf-8');print('Full English explanations:',len(w['nodes']),'relationships:',len(d['relations']))
