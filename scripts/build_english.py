"""Create full English case routes and English resource sources from translation memory.
The original applications keep their IDs and internal model values. A local presentation
layer translates dynamically generated text and exports without modifying their logic.
"""
from pathlib import Path
import sys,json,shutil,re,html,zipfile,io
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'.translation-runtime'));sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,str(R/'inhalte'))
from bs4 import BeautifulSoup,Comment,Doctype
def norm(s):return re.sub(r'\s+',' ',html.unescape(str(s))).strip()
from integration import MODULES,EN
B=R/'inhalte/uebersetzung';MAP=json.loads((B/'en.json').read_text(encoding='utf-8'));D=R/'dist'
partials=sorted((k for k in MAP if (5<=len(k)<180 or k in ['hoch','neu','und','oder','von','bis','mit','für','zum','Mai','Mär']) and MAP[k]!=k and not re.search(r'[<>{}]',k)),key=len,reverse=True)
missing=set()

def code_prose(value):
 value=re.sub(r'<!--(.*?)-->',lambda m:'<!--'+tr(m.group(1))+'-->',value,flags=re.S)
 return re.sub(r'^(\s*[│├└─ ]*[a-zA-Z0-9_.-]+/?[ \t]{2,})([^<>\n]+)$',lambda m:m[1]+tr(m[2]),value,flags=re.M)
def tr(s):
 if not str(s).strip():return s
 n=norm(s)
 if n in MAP:return str(s).replace(str(s).strip(),MAP[n])
 missing.add(n);result=str(s)
 for k in partials:
  if k in result:result=re.sub((r'(?<!\w)' if k[0].isalnum() else '')+re.escape(k)+(r'(?!\w)' if k[-1].isalnum() else ''),lambda _:MAP[k],result)
 return result
def html_en(source,svg=False):
 soup=BeautifulSoup(source,'xml' if svg else 'html.parser')
 for n in list(soup.find_all(string=True)):
  if isinstance(n,(Comment,Doctype)) or n.find_parent(['script','style','textarea']):continue
  if n.find_parent(['code','pre']):
   value=code_prose(str(n))
   if value!=str(n):n.replace_with(value)
   continue
  if n.strip():n.replace_with(tr(str(n)))
 for tag in soup.find_all(True):
  for attr in ['alt','title','aria-label','placeholder']:
   if tag.get(attr):tag[attr]=tr(tag[attr])
 if soup.html:soup.html['lang']='en'
 if soup.head:
  style=soup.new_tag('style');style.string='@media print{svg{max-height:180mm!important;max-width:100%!important;width:auto!important;break-inside:avoid}.print-graph{break-inside:auto!important;page-break-inside:auto!important}}';soup.head.append(style)
 return str(soup)
def md_en(source):
 lines=[];fenced=False
 for line in source.splitlines():
  if line.strip().startswith('```'):fenced=not fenced;lines.append(line);continue
  if fenced:lines.append(code_prose(line));continue
  m=re.match(r'^(\s*(?:#{1,6}\s+|[-*>]\s+|\d+[.)]\s+)?)(.*)$',line);prefix,body=m.groups()
  lines.append(prefix+tr(body))
 return '\n'.join(lines)+'\n'
def json_en(x):
 if isinstance(x,str):return x if re.fullmatch(r'[A-Za-z0-9_./:#%+@?=&-]+',x) else MAP.get(norm(x),x)
 if isinstance(x,list):return [json_en(v) for v in x]
 if isinstance(x,dict):return {k:json_en(v) for k,v in x.items()}
 return x
def prefix(m):return '/en/'+('projects/' if m['kind']=='project' else 'perspectives/')+m['id']+'/full/'
module_routes={m['id']:prefix(m) for m in MODULES};en_catalog=[]
RESOURCE_TITLES={'family-architecture':'Repository architecture','family-cascade':'Consequence chain','family-project':'Project and persona','family-rules':'Shared working rules','family-risks':'Opportunities and risks','family-scenarios':'Project scenarios','family-strategy':'Recommended Git strategy','architecture':'Repository architecture','graph':'Decision graph','strategy':'Git strategy','persona':'Project and persona','stories':'Project scenarios','manual':'Project handbook','handover':'Handover checklist','access':'Access and participation','publication':'Publication','quality':'Data quality','analysis':'Reproducible analysis','benchmark':'Benchmark design','releases':'Versions and releases','maintenance':'Maintenance','expansions':'Extending the corpus','early':'Early publication','starter':'Getting started','risks':'Opportunities and risks','decisions':'Decision graph','familie-architektur':'Repository architecture','familie-entscheidungen':'Decision graph','familie-projekt':'Project and persona','familie-regeln':'Shared working rules','familie-risiken':'Opportunities and risks','familie-situationen':'Project scenarios','familie-strategie':'Recommended Git strategy','anna-architektur':'Repository architecture','anna-entscheidungsgraph':'Decision graph','anna-folgekette':'Consequence chain','albrecht-git-handbuch':'Albrecht project handbook','albrecht-mitarbeitervereinbarung':'Staff agreement','git-datennutzung-muster':'Git data-use agreement','proposal':'Infrastructure proposal','recherche':'Sources and research notes','redaktion':'Editorial planning','zugangspruefung':'Access and permissions review','grammatik':'Design and content grammar','zugangsplan':'Access and handover','musterstrategie':'Recommended Git strategy','importuebergabe':'Import handover','handbuch':'Project handbook','fruehe-veroeffentlichung':'Early publication','quellen':'Further reading','werkzeug-bildnachweise':'Tools and image credits','werk':'The editorial work','vier-uhren':'Project timelines','genese-und-git':'Textual genesis and Git','publikationsstaende':'Publication versions','architektur':'Repository architecture','repo-handbuch':'Repository handbook','publikationskonzept':'Publication concept','nutzungsstart':'Getting started','pflegehandbuch':'Maintenance handbook','beitragsregeln':'Contribution guidelines','dateinamen':'Filename conventions','demonstration':'Example package','demostelle':'Demonstration passage','forschungsablage':'Working research repository','ordnerstruktur':'Publication repository structure','entscheidungen':'Decision graph','lesefolgen-demoseite':'Reading-order demonstration','lesefassung':'Reading edition','frontend-arbeitsplan':'Frontend development plan'}
for m in MODULES:
 src=R/'inhalte/module'/m['id'];dest=D/prefix(m).strip('/');shutil.copytree(src,dest,dirs_exist_ok=True)
 for p in dest.rglob('*'):
  if not p.is_file():continue
  if p.suffix in ['.html','.svg','.md']:
   source=p.read_text(encoding='utf-8-sig');translated=html_en(source,p.suffix=='.svg') if p.suffix in ['.html','.svg'] else md_en(source)
   p.write_text(translated,encoding='utf-8')
  elif p.suffix=='.zip':
   out=io.BytesIO()
   with zipfile.ZipFile(p) as old,zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as new:
    for name in old.namelist():
     content=old.read(name);ext=Path(name).suffix
     try:
      text=content.decode('utf-8-sig')
      if ext=='.md':content=md_en(text).encode('utf-8')
      elif ext in ['.html','.svg']:content=html_en(text,ext=='.svg').encode('utf-8')
      elif ext=='.json':content=json.dumps(json_en(json.loads(text)),ensure_ascii=False,indent=2).encode('utf-8')
     except (UnicodeDecodeError,json.JSONDecodeError):pass
     new.writestr(name,content)
   p.write_bytes(out.getvalue())
 h=(dest/'index.html').read_text(encoding='utf-8')
 # Local translated map is available before the original application's scripts.
 h=h.replace('</head>','<script src="/assets/english-map.js"></script><script src="/assets/english-runtime.js"></script><link rel="stylesheet" href="/assets/module-shell.css"><script src="/assets/module-shell.js" defer></script></head>')
 title,subtitle=EN[m['id']]
 nav=[('projects','Project examples'),('strategy','Your strategy'),('perspectives','Other perspectives'),('understanding-git/handover','Understanding Git'),('workshop','Workshop'),('resources','Resources')]
 frame='<div class="portal-frame" role="banner"><a class="portal-brand" href="/en/">Editionskompass</a><nav aria-label="Main navigation">'+''.join('<a href="/en/'+u+'/">'+t+'</a>' for u,t in nav)+'</nav><a class="portal-lang" href="'+m['route']+'">Deutsch</a></div><div class="portal-context"><span>'+html.escape(title+' · '+subtitle)+'</span><a href="/en/resources/#gesamtkatalog">All resources</a></div>'
 h=re.sub(r'(<body\b[^>]*>)',lambda match:match.group(1)+frame,h,count=1,flags=re.I)
 h=re.sub(r'<a class="family-brand"[^>]*>.*?</a>',lambda _:'<span class="portal-local-label">'+html.escape(title)+'</span>',h,count=1,flags=re.S)
 h=h.replace('</body>','<div class="portal-after"><h2>What does this mean for your project?</h2><p>Record a decision, the responsible role and your next check.</p><a href="/en/strategy/">Prepare an action →</a><nav><a href="/en/about/">About</a><a href="/en/legal-notice/">Legal notice</a><a href="/en/accessibility/">Accessibility</a><a href="/en/privacy/">Privacy</a></nav></div></body>')
 (dest/'index.html').write_text(h,encoding='utf-8')
 # Translate downloadable example metadata while keeping internal application JSON stable.
 soup=BeautifulSoup(h,'html.parser')
 for a in soup.find_all('a',download=True):
  href=a.get('href','')
  if href.endswith('.json') and not href.startswith(('http','/')):
   file=dest/href
   if file.exists():
    out=dest/'materials-en'/Path(href).name;out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(json_en(json.loads(file.read_text(encoding='utf-8'))),ensure_ascii=False,indent=2),encoding='utf-8');a['href']='materials-en/'+out.name
 # Only serialize again if a JSON link actually changed.
 if soup.find('a',href=re.compile(r'^materials-en/')):(dest/'index.html').write_text(str(soup),encoding='utf-8')
for item in json.loads((R/'inhalte/materialkatalog.json').read_text(encoding='utf-8')):
 m=next(m for m in MODULES if m['id']==item['module']);formats={kind:url.replace(m['route'],prefix(m),1) for kind,url in item['formats'].items()};stem=Path(next(iter(item['formats'].values()))).stem;title=RESOURCE_TITLES.get(stem,tr(item['title']));en_catalog.append({**item,'case':EN[m['id']][0],'title':title,'formats':formats})
(R/'inhalte/materialkatalog-en.json').write_text(json.dumps(en_catalog,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'restliche-einheiten.json').write_text(json.dumps(sorted(missing),ensure_ascii=False,indent=2),encoding='utf-8')
print('Full English cases:',len(MODULES),'resource groups:',len(en_catalog),'additional text fragments:',len(missing))
