"""Rebuild the bilingual workshop planner and static planning guide."""
from pathlib import Path
import sys,json,html,shutil
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'inhalte'))
from workshop import TEXT
from integration import resource_catalog
D=R/'dist';E=lambda x:html.escape(str(x),quote=True)
P=lambda x:'<p>'+E(x)+'</p>'
def guide(t):
 return '<article class="ws-guide"><h1>'+E(t['ui']['guide'])+'</h1>'+''.join('<section><h2>'+E(h)+'</h2>'+P(p)+'</section>' for h,p in [(t['heads'][0],t['intro']),('Verantwortung' if t is TEXT['de'] else 'Responsibility',t['responsibility']),(t['heads'][1],t['opportunity']),('Ergebnis' if t is TEXT['de'] else 'Outcome',t['outcome'])])+'<h2>'+E(t['ui']['preparation'])+'</h2><ol>'+''.join('<li>'+E(x)+'</li>' for x in t['prep'])+'</ol><h2>'+E(t['ui']['agenda'])+'</h2><ol>'+''.join('<li><strong>'+E(a)+'</strong>: '+E(b)+'</li>' for a,b in t['phase'])+'</ol><h2>'+E(t['ui']['participants'])+'</h2><ul>'+''.join('<li><strong>'+E(a)+'</strong>: '+E(b)+'</li>' for a,b in t['roles'].values())+'</ul><h2>'+E(t['ui']['protocol'])+'</h2>'+P(t['ui']['protocol_text'])+P(t['ui']['meta'])+'</article>'
def shell(source,lang,body,path,title,data=None,guide_page=False):
 s=BeautifulSoup(source,'html.parser');s.title.string=title+' · Editionskompass';s.find('main').clear();s.find('main').append(BeautifulSoup(body,'html.parser'))
 s.head.append(s.new_tag('link',rel='stylesheet',href='/assets/workshop.css'))
 noscript=s.new_tag('noscript');style=s.new_tag('style');style.string='#ws-profile{display:none!important}';noscript.append(style);s.head.append(noscript)
 if data:
  el=s.new_tag('script',type='application/json',id='ws-data');el.string=json.dumps(data,ensure_ascii=False).replace('</',r'<\/');s.head.append(el);s.head.append(s.new_tag('script',src='/assets/workshop.js',defer=''))
 if guide_page:
  other='en' if lang=='de' else 'de'
  for x in s.select('[data-language],link[rel="alternate"]'):x['href']=f'/{other}/resources/workshop/guide.html'
 build_button=s.select_one('#ws-profile button[type="submit"]')
 if build_button:build_button['type']='button';build_button['id']='ws-build'
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(str(s),encoding='utf-8')
for lang,t in TEXT.items():
 u=t['ui'];de=lang=='de';catalog_path=R/'inhalte'/('materialkatalog.json' if de else 'materialkatalog-en.json');cat=json.loads(catalog_path.read_text(encoding='utf-8'));cat=[x for x in cat if x['module']!='workshop'];materials=[]
 for case in ['anna','albrecht','korpus','stadt']:
  for kind,stem in [('persona','familie-projekt.html'),('rules','familie-regeln.html'),('graph','familie-entscheidungen.html')]:
   item=next(x for x in cat if x['module']==case and x['formats'].get('HTML','').endswith(stem));materials.append({'id':case+'-'+kind,'case':case,'kind':kind,'title':item['case']+' · '+({'persona':'Persona','rules':'Arbeitsregeln' if de else 'Working rules','graph':'Entscheidungsgraph' if de else 'Decision graph'}[kind]),'formats':item['formats']})
 for ident in ['emre','christine','dorothee']:
  item=next(x for x in cat if x['module']==ident and 'PNG' in x['formats']);materials.append({'id':ident,'case':'all','kind':ident,'title':{'emre':'Emre · '+('Einstieg ins Projekt' if de else 'Joining a project'),'christine':'Christine · '+('Begutachtung' if de else 'Reviewing a project'),'dorothee':'Dorothée · '+('Arbeitsgeschichte' if de else 'Working history')}[ident],'formats':item['formats']})
 item=next(x for x in cat if x['module']=='databases' and x['formats'].get('HTML','').endswith('/worksheet.html'));materials.append({'id':'db','case':'all','kind':'db','title':'Git und Datenbanken' if de else 'Git and databases','formats':item['formats']})
 item=next(x for x in cat if x['module']=='korpus' and x['formats'].get('HTML','').endswith('/publication.html'));materials.append({'id':'corpus','case':'all','kind':'corpus','title':'Korpus als Publikation' if de else 'The corpus as a publication','formats':item['formats']})
 for ident,title,formats in [('sheet','Entscheidungsblatt' if de else 'Decision worksheet',{'PDF':f'/assets/sheet-{lang}.pdf','Markdown':f'/assets/sheet-{lang}.md','HTML':('/de/materialien/entscheidungsblatt/' if de else '/en/resources/decision-sheet/')}),('knowledge','Git-Wissen kompakt' if de else 'Compact Git knowledge',{'PDF':f'/assets/wissen-{lang}.pdf','Markdown':f'/assets/wissen-{lang}.md'})]:materials.append({'id':ident,'case':'all','kind':ident,'title':title,'formats':formats})
 # Use the actual registered worksheet route.
 routes=json.loads((D/'assets/data.json').read_text(encoding='utf-8'))['routes'];next(x for x in materials if x['id']=='sheet')['formats']['HTML']=routes[lang]['sheet']
 data={'text':t,'materials':materials,'language':lang}
 path=D/lang/'workshop/index.html';source=path.read_text(encoding='utf-8')
 body='<article class="ws-page"><section class="page-head"><p class="eyebrow">Workshop</p><h1>'+E(t['title'])+'</h1><p class="lead">'+E(t['lead'])+'</p><a class="button" href="#ws-planner">'+E(t['heads'][2])+' ↓</a></section><section class="section narrow"><h2>'+E(t['heads'][0])+'</h2>'+P(t['intro'])+P(t['responsibility'])+'<h2>'+E(t['heads'][1])+'</h2>'+P(t['opportunity'])+'<aside class="ws-note">'+P(t['outcome'])+'</aside></section><section class="section" id="ws-planner"><h2>'+E(t['heads'][2])+'</h2>'+P(u['storage'])+'<p id="ws-storage" role="status"></p><form id="ws-profile"><div class="ws-fields">'+''.join('<label for="ws-'+ident+'">'+E(label)+'<select id="ws-'+ident+'" name="'+ident+'">'+''.join('<option value="'+v+'"'+(' selected' if ident=='duration' and v=='120' else '')+'>'+E(label_)+'</option>' for v,label_ in options)+'</select></label>' for ident,label,options in t['fields'])+'</div><fieldset><legend>'+E(u['topics'])+'</legend>'+''.join('<label class="ws-check"><input type="checkbox" name="focus" value="'+ident+'"'+(' checked' if ident=='workflow' else '')+'>'+E(label)+'</label>' for ident,label in t['focus'])+'</fieldset>'+''.join('<label for="ws-'+ident+'">'+E(label)+'<textarea id="ws-'+ident+'" name="'+ident+'" rows="2"></textarea></label>' for ident,label in t['notes'])+'<button type="submit">'+E(u['create'])+'</button></form><p id="ws-status" role="status"></p></section><section class="section" id="ws-result"><h2>'+E(u['result'])+'</h2><div id="ws-output"><noscript>'+P(u['noscript'])+'</noscript>'+P(t['outcome'])+'<a href="/'+lang+'/resources/workshop/guide.html">'+E(u['guide'])+'</a></div></section><section class="section narrow"><h2>'+E(t['heads'][4])+'</h2><div class="resource-actions">'+''.join('<a href="/'+lang+'/resources/workshop/guide.'+ext+'"'+(' download' if ext!='html' else '')+'>'+fmt+'</a>' for fmt,ext in [('HTML','html'),('Markdown','md'),('PDF','pdf')])+'</div><p class="small">'+E(u['meta'])+'</p></section></article>'
 shell(source,lang,body,path,t['title'],data)
 base=D/lang/'resources/workshop';shell(source,lang,guide(t),base/'guide.html',u['guide'],guide_page=True)
 soup=BeautifulSoup(guide(t),'html.parser')
 for x in soup.select('h1,h2'):x.replace_with('\n'+'#'*int(x.name[1])+' '+x.get_text(' ',strip=True)+'\n')
 (base/'guide.md').write_text(soup.get_text('\n',strip=True)+'\n',encoding='utf-8')
 cache=R/'inhalte/workshop/pdf'/lang/'guide.pdf'
 if cache.exists():shutil.copy2(cache,base/'guide.pdf')
 cat.append({'module':'workshop','case':'Workshop','title':u['guide'],'formats':{'HTML':f'/{lang}/resources/workshop/guide.html','PDF':f'/{lang}/resources/workshop/guide.pdf','Markdown':f'/{lang}/resources/workshop/guide.md'}});catalog_path.write_text(json.dumps(cat,ensure_ascii=False,indent=2),encoding='utf-8')
 resource_page=D/('de/materialien' if de else 'en/resources')/'index.html';s=BeautifulSoup(resource_page.read_text(encoding='utf-8'),'html.parser');markup=resource_catalog(lang).replace('Materialien aller vollständigen Fälle','Materialien zu Themen und Projektfällen').replace('Resources from all complete cases','Resources by topic and project case').replace('</select></label><label>Format','<option value="databases">'+('Git und Datenbanken' if de else 'Git and databases')+'</option><option value="workshop">Workshop</option></select></label><label>Format',1);s.select_one('#gesamtkatalog').replace_with(BeautifulSoup(markup,'html.parser'));resource_page.write_text(str(s),encoding='utf-8')
 privacy=D/('de/datenschutz' if de else 'en/privacy')/'index.html';s=BeautifulSoup(privacy.read_text(encoding='utf-8'),'html.parser')
 if not s.select_one('.ws-privacy'):s.find('main').append(BeautifulSoup('<section class="section narrow ws-privacy"><h2>Workshop</h2>'+P(u['storage'])+'</section>','html.parser'));privacy.write_text(str(s),encoding='utf-8')
 manifest=D/'assets/integrationsmanifest.json';m=json.loads(manifest.read_text(encoding='utf-8'));m['resources']=len(cat);m['topics']=['databases','workshop'];manifest.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
print('Built bilingual workshop planner and planning guide; 127 resource groups.')
