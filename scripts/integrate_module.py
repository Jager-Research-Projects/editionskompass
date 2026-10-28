from pathlib import Path
import sys,re,json,shutil,hashlib,html
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'inhalte'))
from integration import MODULES,EN
D=R/'dist';B=R/'inhalte/module'
nav=[('projekte','Projektbeispiele'),('strategie','Eigene Strategie'),('perspektiven','Perspektivenwechsel'),('git-verstehen/uebergabe','Git verstehen'),('workshop','Workshop'),('materialien','Materialien')]
def frame(title,lang,other,related=''):
 en=lang=='en';items=[('projects','Project examples'),('strategy','Your strategy'),('perspectives','Other perspectives'),('understanding-git/handover','Understanding Git'),('workshop','Workshop'),('resources','Resources')] if en else nav
 return '<div class="portal-frame" role="banner"><a class="portal-brand" href="/'+lang+'/">Editionskompass</a><nav aria-label="'+('Main navigation' if en else 'Hauptnavigation')+'">'+''.join('<a href="/'+lang+'/'+u+'/">'+t+'</a>' for u,t in items)+'</nav><a class="portal-lang" href="'+other+'">'+('Deutsch' if en else 'English')+'</a></div><div class="portal-context"><span>'+html.escape(title)+'</span><a href="/'+lang+'/'+('resources' if en else 'materialien')+'/#gesamtkatalog">'+('All resources' if en else 'Alle Materialien')+'</a>'+related+'</div>'
def finish(h,title,lang,other,related=''):
 # The local header identifies the case and its sections, the global frame the portal.
 h=re.sub(r'<a class="family-brand"[^>]*>.*?</a>',lambda _:'<span class="portal-local-label">'+html.escape(title.split(' · ')[0])+'</span>',h,count=1,flags=re.S)
 h=h.replace('</head>','<link rel="stylesheet" href="/assets/module-shell.css"><script src="/assets/module-shell.js" defer></script></head>')
 h=re.sub(r'(<body\b[^>]*>)',lambda m:m.group(1)+frame(title,lang,other,related),h,count=1,flags=re.I)
 h=h.replace('</body>','<div class="portal-after"><h2>'+('What does this mean for your project?' if lang=='en' else 'Was bedeutet das für Ihr Projekt?')+'</h2><p>'+('Record one decision, a responsible role and a next check.' if lang=='en' else 'Halten Sie eine Entscheidung, die zuständige Rolle und den nächsten Prüfschritt fest.')+'</p><a href="/'+lang+'/'+('strategy' if lang=='en' else 'strategie')+'/">'+('Prepare an action →' if lang=='en' else 'Eine Maßnahme vorbereiten →')+'</a><nav><a href="/'+lang+'/'+('about' if lang=='en' else 'ueber-uns')+'/">'+('About' if lang=='en' else 'Über den Editionskompass')+'</a><a href="/'+lang+'/'+('legal-notice' if lang=='en' else 'impressum')+'/">'+('Legal notice' if lang=='en' else 'Impressum')+'</a><a href="/'+lang+'/'+('accessibility' if lang=='en' else 'barrierefreiheit')+'/">'+('Accessibility' if lang=='en' else 'Barrierefreiheit')+'</a><a href="/'+lang+'/'+('privacy' if lang=='en' else 'datenschutz')+'/">'+('Privacy' if lang=='en' else 'Datenschutz')+'</a></nav></div></body>')
 return h
catalog=[];manifest=[]
for m in MODULES:
 src=B/m['id'];dest=D/m['route'].strip('/');shutil.copytree(src,dest,dirs_exist_ok=True)
 h=(src/'index.html').read_text(encoding='utf-8')
 other='/en/'+('projects/' if m['kind']=='project' else 'perspectives/')+m['id']+'/full/'
 targets={'anna':('agenten','Was können andere in Annas Kommentaren finden?'),'albrecht':('christine','Wie liest eine Gutachterin diesen Bestand?'),'korpus':('agenten','Wie erschließen andere den veröffentlichten Bestand?'),'stadt':('emre','Was braucht die nächste Person für die Weiterarbeit?'),'emre':('albrecht','Wie beginnt eine tragfähige gemeinsame Arbeitsweise?'),'christine':('albrecht','Wie werden Infrastrukturentscheidungen begründet?'),'dorothee':('albrecht','Prozesslernen im großen Editionsprojekt'),'agenten':('korpus','Ein Repositorium als nutzbare Publikation')}
 target,label=targets[m['id']];route=next(x['route'] for x in MODULES if x['id']==target)
 route+={'anna':'#geschichte','albrecht':'#s5','korpus':'#quellen','stadt':'#ek-funde','emre':'#handbuch','christine':'#familie-strategie','dorothee':'#P02-S05','agenten':'#publikation'}[m['id']]
 (dest/'index.html').write_text(finish(h,m['title']+' · '+m['subtitle'],'de',other,'<a href="'+route+'">'+label+' →</a>'),encoding='utf-8')
 groups={}
 for p in dest.rglob('*'):
  if not p.is_file():continue
  ext=p.suffix.lower();fmt={'.pdf':'PDF','.md':'Markdown','.svg':'SVG','.zip':'ZIP','.png':'PNG'}.get(ext)
  if not fmt or (ext=='.png' and 'tischvorlage' not in p.name):continue
  if ext=='.md' and p.name in ['pruefprotokoll.md','pruefstand.md','medienverzeichnis.md','bildprompts.md']:continue
  stem=str(p.relative_to(dest).with_suffix(''));item=groups.setdefault(stem,{'module':m['id'],'case':m['title'],'title':p.stem.replace('-',' ').replace('_',' '),'formats':{}})
  item['formats'][fmt]='/'+p.relative_to(D).as_posix()
  hp=p.with_suffix('.html')
  if hp.exists():
   item['formats']['HTML']='/'+hp.relative_to(D).as_posix();title=re.search(r'<title[^>]*>(.*?)</title>',hp.read_text(encoding='utf-8'),re.S|re.I)
   if title:item['title']=html.unescape(re.sub('<[^>]+>','',title.group(1)))
 class Downloads(HTMLParser):
  def handle_starttag(self,tag,attrs):
   a=dict(attrs)
   if tag=='a' and 'download' in a and a.get('href','').startswith('assets/'):
    f=dest/a['href'];fmt={'.png':'PNG','.svg':'SVG','.zip':'ZIP','.pdf':'PDF'}.get(f.suffix.lower())
    if fmt and f.exists():
     stem=str(f.relative_to(dest).with_suffix(''));item=groups.setdefault(stem,{'module':m['id'],'case':m['title'],'title':Path(a.get('download') or f.name).stem.replace('-',' '),'formats':{}});item['formats'][fmt]='/'+f.relative_to(D).as_posix()
 Downloads().feed(h)
 catalog.extend(groups.values());manifest.append({**m,'integratedIndexSHA256':hashlib.sha256((dest/'index.html').read_bytes()).hexdigest()})
# Academy, both native language versions; language links stay within the portal.
for lang in ['de','en']:
 dest=D/lang/('git-verstehen/antipatterns' if lang=='de' else 'understanding-git/antipatterns');shutil.copytree(B/'academy',dest,dirs_exist_ok=True)
 h=(B/'academy'/('index.html' if lang=='de' else 'index-en.html')).read_text(encoding='utf-8')
 h=re.sub(r'<script>try\{const selected=.*?</script>','',h,count=1,flags=re.S)
 h=h.replace('href="index.html?lang=de"','href="/de/git-verstehen/antipatterns/"').replace('href="index-en.html?lang=en"','href="/en/understanding-git/antipatterns/"')
 h=h.replace('href="index.html"','href="/de/git-verstehen/antipatterns/"').replace('href="index-en.html"','href="/en/understanding-git/antipatterns/"')
 other='/en/understanding-git/antipatterns/' if lang=='de' else '/de/git-verstehen/antipatterns/'
 h=finish(h,'Git Antipattern Academy',lang,other)
 # Explicit access to the complete reading edition alongside game collection.
 h=h.replace('<main id="app">','<div class="portal-context"><a href="/'+lang+'/'+('git-verstehen/wissen-kompakt' if lang=='de' else 'understanding-git/compact-knowledge')+'/">'+('Alle Themen ohne Spiel lesen und herunterladen →' if lang=='de' else 'Read and download every topic without playing →')+'</a></div><main id="app">')
 (dest/'index.html').write_text(h,encoding='utf-8')
 # index-en is a legacy entry point retained as a redirect, not a second unframed app.
 (dest/'index-en.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/en/understanding-git/antipatterns/"><a href="/en/understanding-git/antipatterns/">English</a>',encoding='utf-8')
# The complete bilingual discovery keeps its graph and all 101 relations.
for lang in ['de','en']:
 dest=D/lang/('git-verstehen/entdeckungsreise' if lang=='de' else 'understanding-git/discovery');dest.mkdir(parents=True,exist_ok=True)
 h=(B/'discovery/index.html').read_text(encoding='utf-8')
 if lang=='en':h=h.replace("lang:'de',page:","lang:'en',page:")
 other='/en/understanding-git/discovery/' if lang=='de' else '/de/git-verstehen/entdeckungsreise/'
 (dest/'index.html').write_text(finish(h,'Git-Entdeckungsreise' if lang=='de' else 'Git Discovery',lang,other),encoding='utf-8')
catalog.sort(key=lambda x:(x['module'],x['title']))
(R/'inhalte/materialkatalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
(D/'assets/integrationsmanifest.json').write_text(json.dumps({'modules':manifest,'resources':len(catalog),'translations':'Complete English cases and English resources available.'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Integrated',len(MODULES),'full cases, two complete learning applications,',len(catalog),'resource groups.')
