"""Build the bilingual database topic; preserve all original case narratives."""
from pathlib import Path
import sys,json,html,re,textwrap,shutil,hashlib
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'inhalte'))
from databases import TEXT,ROUTES,SOURCES
D=R/'dist';E=lambda s:html.escape(str(s),quote=True)
ANCHORS=['tasks','benefits','models','history','decision','completion','worksheet']
KINDS=['guide','summary','worksheet','architecture','decision','preservation']
def p(s):return '<p>'+E(s)+'</p>'
def meta(t):return '<p class="db-meta">'+E(t['meta'])+'</p>'
def details(title,text):return '<details><summary>'+E(title)+'</summary>'+p(text)+'</details>'
def callout(title,text):return '<aside class="db-note"><h3>'+E(title)+'</h3>'+p(text)+'</aside>'
def box(x,y,w,h,label,accent=False):
 lines=textwrap.wrap(label,width=max(12,int(w/8)))
 yy=y+h/2-(len(lines)-1)*10
 return f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="'+('#e7ecdf' if accent else '#fffdf7')+'" stroke="#52685e"/>'+''.join(f'<text x="{x+w/2}" y="{yy+i*20}" text-anchor="middle" font-size="15">{E(t)}</text>' for i,t in enumerate(lines))+'</g>'
def line(x1,y1,x2,y2):return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="#52685e" stroke-width="2" marker-end="url(#arrow)"/>'
def svg(kind,lang):
 t=TEXT[lang];de=lang=='de';height={'architecture':600,'decision':760,'preservation':560}[kind]
 title=t['ui'][kind];desc={'architecture':'Die drei Modelle zeigen maßgebliche Bearbeitung und kontrollierte Übergaben.' if de else 'The three models show authoritative editing locations and controlled transfers.','decision':'Vom praktischen Abfragebedarf zum Arbeitsmodell und zur Betriebsvereinbarung.' if de else 'From tested query needs to a workflow model and an operational agreement.','preservation':'Ein bezeichneter Stand verbindet Daten, Veröffentlichung und Prozessgeschichte.' if de else 'An identified version links data, publication and process history.'}[kind]
 content=''
 if kind=='architecture':
  for i,m in enumerate(t['models']):
   y=90+i*170;content+=f'<text x="30" y="{y-22}" font-size="19" font-weight="bold">{m["id"]} · {E(m["title"])}</text>'
   for j,label in enumerate(m['flow']):
    x=30+j*176;content+=box(x,y,154,80,label,j==0)
    if j<4:content+=line(x+154,y+40,x+174,y+40)
   content+=f'<text x="30" y="{y+109}" font-size="14">'+E((['Änderungen in Git festhalten; XML-Werkzeuge lesen den bezeichneten Stand.','Korrekturen zurück nach Git; nach Prüfung erneut importieren.','Export an vereinbarten Punkten; Umfang der erhaltenen Geschichte festlegen.'] if de else ['Record changes in Git; XML tools read the identified version.','Corrections return to Git; import again after checking.','Export at agreed stages; define the scope of the preserved history.'])[i])+'</text>'
 elif kind=='decision':
  labels=(['Drei reale Abfragen und zwei Webfunktionen prüfen','Dateiabfragen genügen','Ein indizierter Dienst bringt Nutzen','A · Git + XML-Werkzeuge','Bearbeitung in Git','Bearbeitung in der DB','B · Geprüfter Import','C · Definierter Export nach Git','Betrieb und XML-Kompetenz verbindlich klären','Öffentlichen Weiterbetrieb oder eigenständige Abschlussausgabe vereinbaren'] if de else ['Test three real queries and two web functions','File queries are sufficient','An indexed service brings benefits','A · Git + XML tools','Editing in Git','Editing in database','B · Checked import','C · Defined export to Git','Agree operation and XML expertise','Agree continued public operation or an independent final output'])
  coords=[(180,65,540,65),(30,185,340,70),(465,185,400,70),(30,330,270,75),(370,330,235,75),(630,330,235,75),(335,465,285,75),(640,465,235,75),(280,600,595,60),(30,690,845,55)]
  for c,label in zip(coords,labels):content+=box(*c,label,accent=label.startswith(('A ·','B ·','C ·')))
  for a in [(360,130,200,185),(540,130,665,185),(200,255,165,330),(600,255,490,330),(750,255,750,330),(490,405,475,465),(750,405,750,465),(475,540,475,600),(750,540,750,600),(450,660,450,690),(165,405,165,690)]:content+=line(*a)
 else:
  timeline=['TEI · '+('unsichere Datierung' if de else 'uncertain date'),'TEI + '+('Prüfregel geändert' if de else 'checking rule revised'),'Release · '+('bezeichneter Stand' if de else 'identified version')]
  for i,label in enumerate(timeline):content+=box(30+i*295,80,255,80,label,i==2)
  content+=line(285,120,325,120)+line(580,120,620,120)
  for i,(title_,body) in enumerate(t['packages']):
   x=30+i*295;content+=line(745,160,x+127,280)+box(x,280,255,110,title_,True)
  content+=box(90,450,720,70,'Zugang und unabhängige Archivierung mit Zuständigkeit planen' if de else 'Plan access and independent archiving with responsible roles')
  for i in range(3):content+=line(157+i*295,390,230+i*220,450)
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}" role="img" aria-labelledby="title desc" xml:lang="{lang}"><title id="title">{E(title)}</title><desc id="desc">{E(desc)}</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#52685e"/></marker></defs><rect width="900" height="{height}" fill="#fffdf7"/><g font-family="Segoe UI,Arial,sans-serif" fill="#243d43"><text x="30" y="32" font-size="24" font-weight="bold">{E(title)}</text>{content}</g></svg>'
def graphic(kind,lang):
 t=TEXT[lang];base=f'/{lang}/resources/databases/'
 text=('<ol>'+''.join('<li><strong>'+E(m['title'])+'</strong>: '+E(' → '.join(m['flow']))+'. '+E(m['text'])+'</li>' for m in t['models'])+'</ol>' if kind=='architecture' else '<ol>'+''.join('<li>'+E(q[1])+': '+E(' / '.join(o[1] for o in q[2]))+'</li>' for q in t['questions'])+'</ol>' if kind=='decision' else '<ol>'+''.join('<li><strong>'+E(h)+'</strong>: '+E(b)+'</li>' for h,b in t['packages'])+'</ol>')
 return '<figure class="db-figure"><img src="'+base+kind+'.svg" alt="'+E(t['ui'][kind])+'" width="900" height="'+str({'architecture':600,'decision':760,'preservation':560}[kind])+'"><figcaption>'+E(t['ui']['diagram'])+' · '+E(t['ui'][kind])+'</figcaption></figure>'+details(t['ui']['alt'],'' ).replace('<p></p>',text)
def resources(lang):
 t=TEXT[lang];return '<div class="db-downloads">'+''.join('<article><h3>'+E(t['ui'][k])+'</h3><div class="resource-actions">'+''.join('<a '+('download ' if fmt!='HTML' else '')+'href="/'+lang+'/resources/databases/'+k+'.'+ext+'">'+fmt+'</a>' for fmt,ext in ([('HTML','html'),('Markdown','md'),('PDF','pdf')] if k in KINDS[:3] else [('HTML','html'),('SVG','svg'),('PDF','pdf')]))+'</div></article>' for k in KINDS)+'</div>'
def worksheet(lang):
 t=TEXT[lang];return p(t['ui']['memory'])+'<p id="db-storage" role="status"></p><form id="db-worksheet">'+''.join('<label class="db-field" for="db-'+ident+'">'+E(label)+'<textarea id="db-'+ident+'" name="'+ident+'" rows="3"></textarea></label>' for ident,label in t['fields'])+'<div class="actions db-screen"><button type="button" id="db-export">'+E(t['ui']['export'])+'</button><button type="button" id="db-clear">'+E(t['ui']['clear'])+'</button><button type="button" data-db-print>'+E(t['ui']['print'])+'</button></div></form><p id="db-message" role="status"></p>'+details(t['ui']['proposal'],'').replace('<p></p>',''.join('<h4>'+E(t['proposal'][i])+'</h4>'+p(t['proposal'][i+1]) for i in [0,2]))
def body(lang,kind='guide'):
 t=TEXT[lang];u=t['ui'];de=lang=='de'
 if kind in ['architecture','decision','preservation']:return '<article class="db-document"><h1>'+E(u[kind])+'</h1>'+graphic(kind,lang)+meta(t)+'</article>'
 if kind=='worksheet':return '<article class="db-document"><h1>'+E(t['worksheet_title'])+'</h1>'+worksheet(lang)+meta(t)+'</article>'
 if kind=='summary':return '<article class="db-document db-summary"><h1>'+E(u['summary'])+'</h1>'+callout(t['default_title'],t['default'])+'<div class="db-cards">'+''.join('<section><h2>'+E(m['title'])+'</h2>'+p(m['text'])+'</section>' for m in t['models'])+'</div>'+p(t['version_note'])+'<h2>'+E(t['end_title'])+'</h2><ul>'+''.join('<li><strong>'+E(h)+'</strong>: '+E(b)+'</li>' for h,b in t['packages'])+'</ul>'+p(t['end_note'])+meta(t)+'</article>'
 h='<article class="db-document"><section class="page-head"><p class="eyebrow">'+E(t['label'])+'</p><h1>'+E(t['title'])+'</h1><p class="lead">'+E(t['lead'])+'</p>'+p(t['intro'])+'<nav class="db-local" aria-label="'+('Auf dieser Seite' if de else 'On this page')+'">'+''.join('<a href="#'+a+'">'+E(label)+'</a>' for a,label in zip(ANCHORS,t['nav']))+'</nav></section>'
 h+='<section class="section narrow" id="tasks"><blockquote>'+p(t['scene'])+'</blockquote><h2>'+E(t['nav'][0])+'</h2><div class="db-cards">'+''.join('<section><h3>'+E(a)+'</h3>'+p(b)+details(u['more'],c)+'</section>' for a,b,c in t['duties'])+'</div></section>'
 h+='<section class="section narrow" id="benefits"><h2>'+E(t['benefit_title'])+'</h2>'+''.join(p(x) for x in t['benefit'])+callout(u['action'],t['benefit_tip'])+'</section>'
 h+='<section class="section" id="models"><h2>'+E(t['default_title'])+'</h2>'+p(t['default'])+graphic('architecture',lang)+'<div class="db-model-controls db-screen" role="group" aria-label="'+E(u['choose'])+'">'+''.join('<button type="button" class="db-model-button" data-model="'+m['id']+'" aria-controls="db-model-'+m['id']+'" aria-pressed="false">'+E(m['id']+' · '+m['title'])+'</button>' for m in t['models'])+'</div><div class="db-model-panels">'+''.join('<section id="db-model-'+m['id']+'" class="db-model-panel"><h3>'+E(m['id']+' · '+m['title'])+'</h3>'+p(m['text'])+details(u['more'],'').replace('<p></p>',p(u['example']+': '+m['example'])+p(u['tip']+': '+m['tip']))+'</section>' for m in t['models'])+'</div>'+details(t['access_title'],t['access'])+''.join(details(a,b) for a,b in t['terms'])+'</section>'
 h+='<section class="section narrow" id="history"><h2>'+E(t['history_title'])+'</h2>'+p(t['history'])+p(t['version_note'])+callout(u['action'],t['history_tip'])+'<div class="actions"><a href="'+('/de/perspektiven/editorische-praxis/' if de else '/en/perspectives/dorothee/full/')+'">'+('Dorothée: Die Arbeitsgeschichte als Quelle →' if de else 'Dorothée: working history as a source →')+'</a><a href="'+('/de/perspektiven/emre/vollstaendig/' if de else '/en/perspectives/emre/full/')+'">'+('Emre: Wie arbeiten wir weiter? →' if de else 'Emre: how do we continue? →')+'</a></div></section>'
 h+='<section class="section" id="decision"><h2>'+E(t['decision_title'])+'</h2>'+graphic('decision',lang)+'<div class="db-decision db-screen"><form id="db-choices">'+''.join('<label for="db-choice-'+ident+'">'+E(label)+'<select id="db-choice-'+ident+'" name="'+ident+'">'+''.join('<option value="'+value+'">'+E(label_)+'</option>' for value,label_ in options)+'</select></label>' for ident,label,options in t['questions'])+'</form><section id="db-result" aria-live="polite" aria-atomic="true"></section></div><noscript>'+p(t['outcomes']['unknown'][1])+'</noscript></section>'
 h+='<section class="section narrow" id="completion"><h2>'+E(t['end_title'])+'</h2>'+p(t['end_intro'])+graphic('preservation',lang)+'<div class="db-cards">'+''.join('<section><h3>'+E(a)+'</h3>'+p(b)+'</section>' for a,b in t['packages'])+'</div>'+callout('Merken' if de else 'Remember',t['end_note'])+'</section>'
 h+='<section class="section narrow" id="worksheet"><h2>'+E(t['worksheet_title'])+'</h2>'+worksheet(lang)+'<a class="button" href="'+('/de/strategie/' if de else '/en/strategy/')+'">'+E(u['next'])+'</a></section><section class="section" id="db-materials"><h2>'+E(u['downloads'])+'</h2>'+resources(lang)+'</section>'
 h+='<section class="section narrow" id="db-sources"><h2>'+E(t['sources_title'])+'</h2>'+p(t['sources_note'])+'<ul>'+''.join('<li><a href="'+url+'">'+E(title)+'</a></li>' for title,url in SOURCES)+'</ul>'+meta(t)+'</section></article>'
 return h.replace('class="db-decision db-screen"','class="db-decision"').replace('<form id="db-choices">','<form id="db-choices" class="db-screen">')
def markdown(lang,kind):
 soup=BeautifulSoup(body(lang,kind),'html.parser')
 for x in soup.select('nav,button,.db-screen,script,noscript'):x.decompose()
 for x in soup.select('img'):x.replace_with('[SVG: '+x['src']+']')
 for x in soup.select('a[href]'):x.replace_with('['+x.get_text(' ',strip=True)+']('+x['href']+')')
 for x in soup.select('h1,h2,h3,h4'):x.replace_with('\n'+'#'*int(x.name[1])+' '+x.get_text(' ',strip=True)+'\n')
 for x in soup.select('li'):x.insert_before('- ')
 for x in soup.select('textarea'):x.replace_with('\n\n…\n\n')
 return re.sub(r'\n{3,}','\n\n',soup.get_text('\n',strip=True))+'\n'
def write_page(template,lang,content,title,target,key='databases'):
 soup=BeautifulSoup(template,'html.parser');soup.html['lang']=lang;soup.body['data-page']=key;soup.body['data-lang']=lang;soup.title.string=title+' · Editionskompass'
 soup.find('main').clear();soup.find('main').append(BeautifulSoup(content,'html.parser'))
 other='en' if lang=='de' else 'de';other_url=ROUTES[other] if target.name=='index.html' else '/'+other+'/resources/databases/'+target.name
 for x in soup.select('[data-language]'):x['href']=other_url;x['lang']=other;x['hreflang']=other
 for x in soup.select('link[rel="alternate"]'):x['href']=other_url
 link=soup.new_tag('link',rel='stylesheet',href='/assets/databases.css');soup.head.append(link)
 script=soup.new_tag('script',src='/assets/databases.js',defer='');soup.head.append(script)
 noscript=soup.new_tag('noscript');style=soup.new_tag('style');style.string='.db-screen{display:none!important}';noscript.append(style);soup.head.append(noscript)
 script=soup.new_tag('script',type='application/json',id='db-data');script.string=json.dumps(TEXT[lang],ensure_ascii=False).replace('</',r'<\/');soup.head.append(script)
 target.parent.mkdir(parents=True,exist_ok=True);target.write_text(str(soup),encoding='utf-8')
def inject(path,content,anchor=None):
 soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
 if soup.select_one('.db-crosslink'):return
 target=soup.select_one('#'+anchor) if anchor else soup.find('main')
 if not target:target=soup.find('main')
 if not target:return
 target.append(BeautifulSoup('<aside class="db-crosslink">'+content+'</aside>','html.parser'))
 soup.head.append(soup.new_tag('link',rel='stylesheet',href='/assets/databases.css'))
 path.write_text(str(soup),encoding='utf-8')
for lang,t in TEXT.items():
 template=(D/lang/'index.html').read_text(encoding='utf-8');base=D/lang/'resources/databases';base.mkdir(parents=True,exist_ok=True)
 write_page(template,lang,body(lang),t['title'],D/ROUTES[lang].strip('/')/'index.html')
 for kind in KINDS:
  if kind in KINDS[3:]:(base/(kind+'.svg')).write_text(svg(kind,lang),encoding='utf-8')
  write_page(template,lang,body(lang,kind),t['ui'][kind],base/(kind+'.html'))
  if kind in KINDS[:3]:(base/(kind+'.md')).write_text(markdown(lang,kind),encoding='utf-8')
  cached=R/'inhalte/databases/pdf'/lang/(kind+'.pdf')
  if cached.exists():shutil.copy2(cached,base/(kind+'.pdf'))
 # Register topic in search, route mapping and the existing catalog.
 data=json.loads((D/'assets/data.json').read_text(encoding='utf-8'));data['routes'][lang]['databases']=ROUTES[lang];data['search'][lang]=[x for x in data['search'][lang] if x['url']!=ROUTES[lang]];data['search'][lang].append({'title':t['label'],'text':t['lead'],'url':ROUTES[lang]});(D/'assets/data.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
 catpath=R/'inhalte'/('materialkatalog.json' if lang=='de' else 'materialkatalog-en.json');cat=json.loads(catpath.read_text(encoding='utf-8'));cat=[x for x in cat if x['module']!='databases']
 for kind in KINDS:
  root=f'/{lang}/resources/databases/{kind}';formats={'HTML':root+'.html','PDF':root+'.pdf'};formats.update({'Markdown':root+'.md'} if kind in KINDS[:3] else {'SVG':root+'.svg'})
  cat.append({'module':'databases','case':t['label'],'title':t['ui'][kind],'formats':formats})
 catpath.write_text(json.dumps(cat,ensure_ascii=False,indent=2),encoding='utf-8')
 material_path=D/(('de/materialien/' if lang=='de' else 'en/resources/'))/'index.html';soup=BeautifulSoup(material_path.read_text(encoding='utf-8'),'html.parser')
 from integration import resource_catalog
 catalog_html=resource_catalog(lang).replace('Materialien aller vollständigen Fälle','Materialien zu Themen und Projektfällen').replace('Resources from all complete cases','Resources by topic and project case').replace('>Fall<select','>Thema oder Fall<select').replace('>Case<select','>Topic or case<select').replace('Alle Fälle','Alle Themen und Fälle').replace('All cases','All topics and cases').replace('</select></label><label>Format','<option value="databases">'+E(t['label'])+'</option></select></label><label>Format',1)
 soup.select_one('#gesamtkatalog').replace_with(BeautifulSoup(catalog_html,'html.parser'))
 material_path.write_text(str(soup),encoding='utf-8')
 # Contextual links: all additions are outside the original narrative text.
 places=[('de/git-verstehen/uebergabe/' if lang=='de' else 'en/understanding-git/handover/',None,'models',t['label'],t['lead']),('de/strategie/' if lang=='de' else 'en/strategy/',None,'decision',t['decision_title'],t['benefit_tip']),('de/quellen/' if lang=='de' else 'en/sources/',None,'db-sources',t['sources_title'],t['sources_note']),('de/workshop/' if lang=='de' else 'en/workshop/',None,'worksheet',t['worksheet_title'],('15–20 Minuten: Drei Abfragen, zwei Webfunktionen und den Änderungsweg gemeinsam klären.' if lang=='de' else '15–20 minutes: agree three queries, two web functions and the change process.'))]
 cases=[('anna','kleinprojekt','publikation','benefits','XML-Abfragen ohne eigenen Datenbankdienst','XML queries without your own database service'),('albrecht','langzeitedition','proposal','models','Git und institutionellen XML-Dienst verbinden','Connect Git and an institutional XML service'),('korpus','publikationsrepositorium','publikation','completion','Datenbankdienst und unabhängig nutzbares Korpus','A database service and an independently usable corpus'),('stadt','drittmittelprojekt','frontend-plan','completion','Frontend, Datenbank und Weiterbetrieb getrennt planen','Plan frontend, database and continued operation separately')]
 context={
 'anna':['Für Annas Nachschlagen und Prüfen können XML-Werkzeuge auf den versionierten Dateien genügen. Ein eigener laufender Datenbankdienst braucht einen zusätzlichen Nutzen und gesicherte Betreuung.','XML tools working on versioned files may be sufficient for Anna’s reference and checking tasks. A separate running database service needs an additional benefit and reliable support.'],
 'albrecht':['Ein gemeinsamer indizierter XML-Dienst kann die Arbeit über Institute hinweg erleichtern. Das Proposal sollte auch festlegen, wo Änderungen verbindlich entstehen und wie die Git-Historie erhalten wird.','A shared indexed XML service can support work across institutions. The proposal should also define where authoritative changes are made and how Git history is preserved.'],
 'korpus':['Ein Abfragedienst kann das Korpus ergänzen. Forschende brauchen weiterhin bezeichnete, lokal nutzbare Daten und nachvollziehbare Transformationen – unabhängig davon, ob gerade ein Projektserver läuft.','A query service can complement the corpus. Researchers still need identified, locally usable data and traceable transformations, independently of a running project server.'],
 'stadt':['Eine Datenbank kann die Entwicklung und Erschließung unterstützen. Ob sie nach Förderende Teil des öffentlichen Frontends bleiben muss, wird nach den benötigten Funktionen und der Betriebszusage entschieden.','A database can support development and access. Whether it must remain part of the public frontend after funding ends depends on the required functions and the operational commitment.']}
 for ident,slug,anchor,section,de,en in cases:places.append((f'de/projekte/{slug}/' if lang=='de' else f'en/projects/{ident}/full/',anchor,section,de if lang=='de' else en,context[ident][0 if lang=='de' else 1]))
 for path,anchor,section,title,text in places:
  file=D/path/'index.html'
  if file.exists():inject(file,'<h2>'+E(title)+'</h2>'+p(text)+'<a href="'+ROUTES[lang]+'#'+section+'">'+('Vertiefung öffnen →' if lang=='de' else 'Open this topic →')+'</a>',anchor)
 # Navigable overview card instead of an extra global menu item.
 page=D/('de/git-verstehen/' if lang=='de' else 'en/understanding-git/')/'index.html'
 # Privacy disclosure for the new session-only worksheet.
 inject(D/('de/datenschutz/' if lang=='de' else 'en/privacy/')/'index.html',p(t['ui']['memory']))
 provenance={'version':'1.0','date':'2026-10-28','languages':['de','en'],'sourceDocuments':['entscheidungshilfe_git_existdb_digitale_editionen.md','git_existdb_digitale_editionen_vergleich.md'],'assistance':'AI-assisted drafting, translation, schematic SVG authoring and implementation','sources':SOURCES,'pdfReview':'See tests/databases-results.json; no formal accessibility conformance claim.'}
 (R/'inhalte/databases').mkdir(exist_ok=True);(R/'inhalte/databases/provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2),encoding='utf-8')
print('Built Git/database resource: two languages, six materials per language, contextual links and catalog entries.')
manifest=D/'assets/integrationsmanifest.json';data=json.loads(manifest.read_text(encoding='utf-8'));data['resources']=len(cat);data['topics']=['databases'];manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
