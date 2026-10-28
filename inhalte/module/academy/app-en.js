'use strict';
const {chapters,cards}=window.ACADEMY,app=document.querySelector('#app'),KEY='git-academy-catalog-v2';
let saved={seen:[],best:{},runs:0},persistent=true,run=null;
try{saved={...saved,...JSON.parse(localStorage.getItem(KEY)||'{}')};localStorage.setItem(KEY,JSON.stringify(saved))}catch(e){persistent=false}
function persist(){try{localStorage.setItem(KEY,JSON.stringify(saved))}catch(e){persistent=false}document.querySelector('#storage').textContent=persistent?'Progress is stored only in this browser.':'Browser storage unavailable — progress lasts for this session.'}
function shuffle(a){a=[...a];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function button(text,fn,cls=''){let b=document.createElement('button');b.textContent=text;b.className=cls;b.onclick=fn;return b}
function show(html){app.innerHTML=html;window.scrollTo(0,0)}
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function home(){run=null;show(`<div class="eyebrow">Digital editions · Five chapters</div><h1>Good history.<br>In your repository, too.</h1><p class="intro">Recognise risky habits, weigh alternatives and discover when an exception makes sense. From file chaos to Git history.</p><img class="hero-image" src="assets/academy.webp" alt="Git Antipattern Academy: books, learning cards and a Git graph"><div class="row between"><p>${saved.seen.length} of 25 learning cards discovered</p><span class="badge">5 exercises per round · about 5 minutes</span></div><progress value="${saved.seen.length}" max="25" aria-label="Discovered learning cards"></progress><div class="grid" id="chapters"></div><p class="note warning">Based on the original catalogue of 19 October 2026. Smells are clues, not proof. Consequence questions therefore also describe the adopted practice. <a href="Git_Antipatterns_English.md" download>Download English learning catalogue</a> · <a href="Git_Antipatterns_Digitale_Editionen.md" download>German original</a>.</p>`);chapters.forEach((name,i)=>{let el=document.createElement('section');el.className='card chapter';el.innerHTML=`<img class="chapter-image" src="assets/chapter-${i+1}.webp" alt="" loading="lazy"><div class="seal">0${i+1} <span aria-hidden="true">❧</span></div><h3>${name}</h3><p>${['Versions, copies, preservation, backups and responsibility.','Metadata, scholarly versions and publication readiness.','Agreements, access, usage rights and consent.','Limits of analysis, processing purposes and historical data.','Coherent commits, integration, formatting and stable releases.'][i]}</p><p class="note">${saved.best[i]===undefined?'No rounds completed yet':`Best round: ${saved.best[i]} / 5`}</p>`;el.append(button('Start chapter →',()=>start(i),'primary'));document.querySelector('#chapters').append(el)});app.append(button('Reset progress',()=>{if(confirm('Delete all locally stored learning progress?')){saved={seen:[],best:{},runs:0};persist();home()}}))}
function start(ch){saved.runs++;persist();const pool=shuffle(cards.filter(c=>c.chapter===ch)),types=shuffle([0,1,2,3,4]);run={ch,questions:pool.map((c,i)=>({c,type:types[i],exception:Math.random()<.5})),pos:0,score:0};question()}
const typeNames=['Smell Detective','Two paths / one problem','A suitable alternative','Antipattern or legitimate exception?','Causal chain'];
function question(){let q=run.questions[run.pos],c=q.c;show(`<div class="row between"><span class="eyebrow">Chapter ${run.ch+1} · ${chapters[run.ch]}</span><span>Exercise ${run.pos+1} / 5</span></div><progress value="${run.pos}" max="5" aria-label="Round progress"></progress><article class="card question"><div class="eyebrow">${typeNames[q.type]}</div><h2 id="question-title" tabindex="-1">${['What consequence could follow?','Which approach addresses the problem?','Which specific risk does this measure reduce?','How do you assess this action?','Put the explanation in the right order.'][q.type]}</h2><p id="prompt"></p><div class="options" id="options"></div><div id="feedback" aria-live="polite"></div></article>`);document.querySelector('#question-title').focus();let prompt=document.querySelector('#prompt'),opts=document.querySelector('#options');
if(q.type===4){renderChain(q,prompt,opts);return}
let choices=[],right;
if(q.type===0){prompt.textContent=c.smell;right=c.cause;choices=[right,...shuffle(cards.filter(x=>x.id!==c.id&&x.chapter===c.chapter)).slice(0,3).map(x=>x.cause)]}
if(q.type===1){prompt.textContent=c.problem;right=c.good;choices=[right,c.bad]}
if(q.type===2){prompt.textContent=c.good;right=c.cause;choices=[right,...shuffle(cards.filter(x=>x.id!==c.id&&x.chapter===c.chapter)).slice(0,2).map(x=>x.cause)]}
if(q.type===3){prompt.textContent=q.exception?c.exception:c.smell;right=q.exception?'Legitimate exception in this context':'Problematic practice';choices=['Problematic practice','Legitimate exception in this context']}
shuffle(choices).forEach(t=>{let b=button(t,()=>{opts.querySelectorAll('button').forEach(x=>{x.disabled=true;if(x.textContent===right)x.classList.add('correct')});if(t!==right)b.classList.add('wrong');finish(t===right,q)},'option');opts.append(b)})}

// A card occupies exactly one place. Moving onto another card swaps their places.
function moveChain(state,card,target){const from=state.indexOf(card);if(from<0||target<0||target>=state.length)return state;const next=[...state];[next[from],next[target]]=[next[target],next[from]];return next}
function renderChain(q,prompt,opts){
 prompt.textContent='Drag the text cards into the labelled chain links. Move and swap them as often as you like. Alternatively, select a card, then click its destination (also works with Tab and Enter). Only “Check chain” evaluates your answer.';
 const texts=[q.c.smell,q.c.cause,q.c.good],labels=['Situation','Possible consequence','Countermeasure'];
 let state=[null,null,null,...shuffle([0,1,2])],selected=null,dragged=null;
 opts.className='chain-exercise';
 const board=document.createElement('div');board.className='chain-board';
 const tray=document.createElement('div');tray.className='chain-tray';tray.setAttribute('aria-label','Card tray');
 const status=document.createElement('p');status.className='note';status.setAttribute('aria-live','polite');
 const check=button('Check chain',()=>{finish(state.slice(0,3).every((v,i)=>v===i),q);},'primary');check.disabled=true;
 const clear=button('Return all cards',()=>{state=[null,null,null,...shuffle([0,1,2])];selected=null;draw();status.textContent='All cards are back in the tray.'});
 const actions=document.createElement('div');actions.className='row';actions.append(check,clear);
 opts.append(board,tray,status,actions);
 function place(card,index){state=moveChain(state,card,index);selected=null;draw(index);status.textContent='Card moved. '+state.slice(0,3).filter(v=>v!==null).length+' of 3 chain links filled.'}
 function draw(focusIndex){board.innerHTML='';tray.innerHTML='';let focusControl=null;
 state.forEach((card,index)=>{
 const slot=document.createElement('div');slot.className=index<3?'chain-link':'tray-slot';
 if(index<3){const label=document.createElement('div');label.className='chain-label';label.textContent=(index+1)+' · '+labels[index];slot.append(label)}
 const control=button(card===null?(index<3?'Place a card here':'Return to tray'):texts[card],()=>{if(selected!==null){place(selected,index);return}if(card!==null){selected=card;draw(index);status.textContent='Card selected. Choose a destination, or select the same card to deselect it.'}},'chain-tile'+(card===null?' empty':'')+(card!==null&&selected===card?' selected':''));
 control.setAttribute('aria-label',(index<3?labels[index]:'Card tray')+': '+(card===null?'empty':texts[card]));
 control.setAttribute('aria-pressed',String(card!==null&&selected===card));
 if(card!==null){control.draggable=true;control.ondragstart=e=>{dragged=card;e.dataTransfer.setData('text/plain',String(card));e.dataTransfer.effectAllowed='move';};control.ondragend=()=>{dragged=null;};}
 slot.ondragover=e=>{e.preventDefault();e.dataTransfer.dropEffect='move';};
 slot.ondrop=e=>{e.preventDefault();if(dragged!==null)place(dragged,index);dragged=null;};
 slot.append(control);(index<3?board:tray).append(slot);if(index===focusIndex)focusControl=control;
 });check.disabled=state.slice(0,3).some(v=>v===null);if(focusControl)focusControl.focus();
 }
 draw();
}

function finish(ok,q){if(!q.graded){if(ok)run.score++;q.graded=true;}if(!saved.seen.includes(q.c.id))saved.seen.push(q.c.id);persist();let f=document.querySelector('#feedback');f.className='feedback';f.innerHTML=`<strong>${ok?'Correctly assessed.':'Here is something to consider.'}</strong>${q.type===4?'<p class="note">Your first check counts towards the round score. You can keep rearranging and checking the chain.</p>':''}${q.type===3?`<p>${q.exception?'The stated condition limits the risk. An exception is not a blanket recommendation.':'The situation presents a specific risk; context determines the appropriate response.'}</p>`:''}${solution(q.c)}${q.type===4?`<p class="note">The expected chain: ${esc(q.c.smell)} → ${esc(q.c.cause)} → ${esc(q.c.good)}</p>`:''}`;f.append(button(run.pos===4?'Finish round →':'Next exercise →',()=>{run.pos++;if(run.pos===5)result();else question()},'primary'))}
function solution(c){let x=c.tile%5*25,y=Math.floor(c.tile/5)*25;return `<section class="solution"><div class="eyebrow">Learning card · ${c.code}</div><h3>${esc(c.title)}</h3><div class="illustration" role="img" aria-label="Illustration for ${esc(c.title)}" style="background-position:${x}% ${y}%"></div><p><strong>Context:</strong> ${esc(c.context)}</p><p><strong>Problem and adopted practice:</strong> ${esc(c.smell)}</p><p><strong>Why it appeals:</strong> ${esc(c.appeal)}</p><p><strong>Observable smells:</strong> ${esc(c.symptoms)}</p><p><strong>Possible consequences:</strong> ${esc(c.cause)}</p><p><strong>Better approach:</strong> ${esc(c.good)}</p><p><strong>Why?</strong> ${esc(c.reason)}</p><p><strong>Scope and exceptions:</strong> ${esc(c.boundary)}</p></section>`}
function result(){saved.best[run.ch]=Math.max(saved.best[run.ch]||0,run.score);persist();let ch=run.ch;show(`<div class="eyebrow">Round completed</div><h1>${run.score} out of 5 correct.</h1><p class="intro">${run.score===5?'Well considered!':'The learning cards help you distinguish risks and exceptions more precisely.'} Each new round shuffles exercise types and answer order. Every chapter covers all five topics.</p><div class="row" id="actions"></div>`);let a=document.querySelector('#actions');a.append(button('Another round',()=>start(ch),'primary'),button('Chapter overview',home));if(ch<4)a.append(button('Continue to chapter '+(ch+2),()=>start(ch+1)))}
function library(){show(`<h1>All 25 learning cards</h1><p>No round is required to read the cards. Chapter rounds remain an optional challenge.</p><div id="back"></div><div class="grid" id="collection"></div>`);document.querySelector("#back").append(button("← Chapter overview",home));cards.forEach(c=>{let el=document.createElement("article");el.className="card";el.innerHTML=solution(c);document.querySelector("#collection").append(el)})}
document.querySelector('#library').onclick=()=>{if(run&&run.pos<5&&!confirm('Leave the current round? Discovered cards will be kept.'))return;run=null;library()};persist();home();
