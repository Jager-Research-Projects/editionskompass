from pathlib import Path
import json,html
R=Path(__file__).resolve().parents[1]
MODULES=json.loads((R/'inhalte/module-manifest.json').read_text(encoding='utf-8'))
EN={
 'anna':('Small project and individual edition','Anna · The forgotten text'),
 'albrecht':('Large project and long-term edition','The Albrecht historical-critical edition'),
 'korpus':('Corpus and publication repository','Rätselhaft!'),
 'stadt':('Grant-funded project with a small team','Die andere Stadt'),
 'emre':('Joining a project','Emre Kaya'),
 'christine':('Reviewing a scholarly project','Christine Fühlhaber'),
 'dorothee':('Researching editorial practice','Dorothée Meisner'),
 'agenten':('When agents explore repositories','Nora and Sami')}
def add_routes(routes):
 for m in MODULES:
  routes['full_'+m['id']]={'de':m['route'][4:].rstrip('/'),'en':('projects/' if m['kind']=='project' else 'perspectives/')+m['id']+'/full'}
 routes['academy']={'de':'git-verstehen/antipatterns','en':'understanding-git/antipatterns'}
 routes['discovery']={'de':'git-verstehen/entdeckungsreise','en':'understanding-git/discovery'}

def overview(m,lang,url):
 de=lang=='de';title,subtitle=(m['title'],m['subtitle']) if de else EN[m['id']]
 return '<section class="page-head"><p class="eyebrow">'+('Vollständiger Fall' if de else 'Full case · German reading edition')+'</p><h1>'+title+'</h1><p class="lead">'+subtitle+'</p></section><section class="section narrow"><p>'+('Die vollständige Fallgeschichte mit allen Interaktionen und Materialien ist in den gemeinsamen Rahmen integriert.' if de else 'The complete original case is now available within this portal, including all scenes, interactive tools and materials. It is currently in German. Its full English translation is still in preparation; the earlier short English learning routes remain available separately.')+'</p><a class="button" href="'+m['route']+'" hreflang="de">'+('Vollständigen Fall öffnen →' if de else 'Open the complete German case →')+'</a><div class="actions"><a href="'+url('projects' if m['kind']=='project' else 'perspectives',lang)+'">'+('Zur Übersicht' if de else 'Back to overview')+'</a><a href="'+url('strategy',lang)+'">'+('Für das eigene Vorhaben festhalten' if de else 'Record an action for your project')+'</a></div></section>'

def perspectives_index(lang,url):
 de=lang=='de';out='<section class="section"><div class="project-grid">'
 descriptions={
 'emre':['Ein neuer Mitarbeiter liest Dateien und Geschichte, um ohne direkte Übergabe arbeitsfähig zu werden. Was erklärt das Repo – und was muss das Team klären?','A newcomer reads files and history to work without a direct handover. What does the repository explain, and what must the team clarify?'],
 'christine':['Eine externe Gutachterin prüft Leistung und Fortschritt. Welche Belege tragen ihr Urteil, und welche vermeintlich präzisen Kennzahlen führen in die Irre?','An external reviewer examines achievements and progress. Which evidence supports a judgement, and which apparently precise metrics mislead?'],
 'dorothee':['Eine Forscherin untersucht editorische Prozesse. Wann wird die Arbeitsgeschichte zu einer wertvollen Quelle – und wann zur Beobachtung einzelner Menschen?','A researcher studies editorial processes. When does working history become a valuable source, and when does it turn into scrutiny of individuals?'],
 'agenten':['Nora und Sami beauftragen Agenten mit fachlichen Fragen. Die Recherche erschließt auch unerwartete Arbeitsspuren, Kontakte und Angriffspfade.','Nora and Sami ask agents scholarly questions. Their research uncovers unexpected working traces, contacts and attack paths.']}
 for m in MODULES:
  if m['kind']!='perspective':continue
  title,sub=(m['title'],m['subtitle']) if de else EN[m['id']]
  out+='<article class="project-card"><p class="eyebrow">'+sub+'</p><h2>'+title+'</h2><p>'+descriptions[m['id']][0 if de else 1]+'</p><a href="'+url('full_'+m['id'],lang)+'">'+('Vollständigen Perspektivwechsel erkunden →' if de else 'Explore the complete perspective →')+'</a></article>'
 return out+'</div></section>'

def resource_catalog(lang):
 de=lang=='de';file=R/'inhalte'/('materialkatalog.json' if de else 'materialkatalog-en.json');catalog=json.loads(file.read_text(encoding='utf-8')) if file.exists() else []
 out='<section class="section" id="gesamtkatalog"><h2>'+('Materialien aller vollständigen Fälle' if de else 'Resources from all complete cases')+'</h2><p>'+('Die vorhandenen Druckfassungen, Vorlagen, Graphen und Beispielpakete sind hier zusammengeführt. Sprache der bisherigen Fallmaterialien: Deutsch. Die zweisprachigen Portal-Arbeitsblätter und Wissensfassungen stehen weiter oben.' if de else 'English print editions, templates, graphs, illustrated workshop overviews and example packages are collected here. Use the filters to choose a case or format. Historical source texts, technical identifiers and example filenames retain their original form.')+'</p><form class="catalog-filters" id="catalog-filters"><label>'+('Fall' if de else 'Case')+'<select id="catalog-case"><option value="all">'+('Alle Fälle' if de else 'All cases')+'</option>'+''.join('<option value="'+m['id']+'">'+(m['title'] if de else EN[m['id']][0])+'</option>' for m in MODULES)+'</select></label><label>Format<select id="catalog-format"><option value="all">'+('Alle Formate' if de else 'All formats')+'</option>'+''.join('<option>'+x+'</option>' for x in ['PDF','HTML','Markdown','SVG','PNG','ZIP'])+'</select></label><label>'+('Suchen' if de else 'Search')+'<input id="catalog-search" type="search"></label></form><p id="catalog-count" role="status">'+str(len(catalog))+' '+('Materialien' if de else 'resources')+'</p><div class="material-grid">'
 for item in catalog:
  out+='<article class="material-card catalog-item" data-case="'+item['module']+'" data-formats="'+' '.join(item['formats'])+'"><p class="eyebrow">'+html.escape(item['case'])+(' · DE</p><h3>' if de else ' · EN</p><h3>')+html.escape(item['title'])+'</h3><div class="resource-actions">'+''.join('<a href="'+u+'"'+(' download' if f!='HTML' else '')+'>'+f+'</a>' for f,u in item['formats'].items())+'</div></article>'
 return out+'</div></section>'
