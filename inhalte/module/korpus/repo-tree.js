const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const REPO_NODES=[
 {name:'README.md',note:'Einstieg und erste Untersuchung',depth:0,file:true},
 {name:'LICENSE',note:'Nutzungsrechte',depth:0,file:true},
 {name:'CITATION.cff',note:'Angaben zum Zitieren',depth:0,file:true},
 {name:'CHANGELOG.md',note:'Änderungen und bekannte Fehler',depth:0,file:true},
 {name:'data/',note:'Maßgeblicher Datenbestand',depth:0},
 {name:'tei/',note:'Buchdateien im TEI-Format',depth:1},
 {name:'rk_1786_b0001.xml',note:'Eine Datei je Buch oder Sammlung',depth:2,file:true},
 {name:'schema/',note:'Datenmodell und Prüfregeln',depth:0},
 {name:'docs/',note:'Auszeichnung und Publikationskonzept',depth:0},
 {name:'examples/',note:'Kleiner lokal ausführbarer Einstieg',depth:0},
 {name:'tests/',note:'Technische und fachliche Prüffälle',depth:0}
];
const KEYS=['readme','license','citation','changelog','data','tei','book','schema','docs','examples','tests'];
REPO_NODES.forEach((n,i)=>n.key=KEYS[i]);
const SAMPLES={schema:['korpus.odd','korpus.rng','README.md'],docs:['publikationskonzept.md','auszeichnung.md','dateinamen.md','releaseablauf.md'],examples:[{name:'nutzungsstart/',depth:1,file:false},{name:'README.md',depth:2,file:true},{name:'untersuchen.py',depth:2,file:true}],tests:['README.md','pruefe_dateinamen.py','fixtures/']};
export function repoTreeSVG({interactive=false,selected='readme',expanded=['data','tei']}={}){
 const nodes=[];
 for(const n of REPO_NODES){if(interactive&&((n.key==='tei'&&!expanded.includes('data'))||(n.key==='book'&&(!expanded.includes('data')||!expanded.includes('tei')))))continue;nodes.push(n);if(interactive&&expanded.includes(n.key)&&SAMPLES[n.key])for(const item of SAMPLES[n.key]){const sample=typeof item==='string'?{name:item,depth:1,file:!item.endsWith('/')}:item;nodes.push({...sample,note:'Beispielausschnitt',sample:true});}}
 const height=122+nodes.length*78,suffix=interactive?'interactive':'static';
 const folder=(x,y)=>`<path d="M${x} ${y+5}h9l4 5h17v14H${x}Z" fill="#dae3d0" stroke="#597462" stroke-width="1.5"/>`;
 const file=(x,y)=>`<path d="M${x+4} ${y+3}h16l7 7v14H${x+4}Z M${x+20} ${y+3}v8h7" fill="#fffdf7" stroke="#62766b" stroke-width="1.5"/>`;
 let result=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 ${height}" role="${interactive?'group':'img'}" aria-labelledby="repo-tree-title-${suffix} repo-tree-desc-${suffix}"><title id="repo-tree-title-${suffix}">Ordnerstruktur des Korpusrepos</title><desc id="repo-tree-desc-${suffix}">Im Hauptverzeichnis liegen README, Lizenz, Zitationsangaben und Änderungsprotokoll. Die Ordner schema, docs, examples und tests liegen daneben. data enthält tei und darin eine XML-Datei pro Buch oder Sammlung.</desc><style>.repo-select{cursor:pointer}.repo-select:focus .node-bg{stroke:#a94a32;stroke-width:4}.repo-selected .node-bg{stroke:#a94a32;stroke-width:2.5}</style><rect width="520" height="${height}" fill="#fffdf7"/><rect x="14" y="16" width="492" height="66" rx="8" fill="#243d43"/>${folder(28,30)}<text x="74" y="58" font-family="Consolas,monospace" font-size="24" fill="#fffdf7">raetsel-korpus/</text>`;
 const parents=[{x:42,y:82}];
 nodes.forEach((n,i)=>{
  const x=76+n.depth*40,y=110+i*78,parent=parents[n.depth];
  const attrs=interactive&&!n.sample?`class="repo-select${n.key===selected?' repo-selected':''}" data-repo-select="${n.key}" role="button" tabindex="0" aria-label="${escape(n.name)}: Inhalt und Pflegehinweise" aria-pressed="${n.key===selected}"${!n.file?` aria-expanded="${expanded.includes(n.key)}"`:''}`:'';
  result+=`<path d="M${parent.x} ${parent.y}V${y+29}H${x}" fill="none" stroke="#829885" stroke-width="2"/><g ${attrs}><rect class="node-bg" x="${x}" y="${y}" width="${430-n.depth*40}" height="65" rx="6" fill="${n.depth>0?'#e9eee1':'#f1f3eb'}" stroke="#c3cdbd"/>${n.file?file(x+10,y+8):folder(x+10,y+8)}<text x="${x+52}" y="${y+27}" font-family="Consolas,monospace" font-size="${n.sample?19:24}" fill="#243d43">${escape(n.name)}</text><text x="${x+12}" y="${y+53}" font-family="Arial,sans-serif" font-size="20" fill="#42594b">${escape(n.note)}${interactive&&!n.file&&!n.sample?' '+(expanded.includes(n.key)?'−':'+'):''}</text></g>`;
  if(!n.sample||!n.file)parents[n.depth+1]={x:x+20,y:y+65};
 });
 return result+'</svg>';
}
export function repoTreeText(){return '<ul>'+REPO_NODES.filter(n=>n.depth===0).map(n=>`<li><strong>${escape(n.name)}</strong> – ${escape(n.note)}${n.name==='data/'?'<ul><li><strong>tei/</strong> – Buchdateien im TEI-Format<ul><li><strong>rk_1786_b0001.xml</strong> – eine Datei je Buch oder Sammlung</li></ul></li></ul>':''}</li>`).join('')+'</ul>';}
