'use strict';
const grid=document.querySelector('#projects');
const counter=document.querySelector('#result-count');
const search=document.querySelector('#search');
const dialog=document.querySelector('#project-dialog');
let projects=[],filter='전체',lastTrigger=null;
const escapeHtml=value=>String(value).replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
function render(){
 const query=search.value.trim().toLocaleLowerCase();
 const visible=projects.filter(p=>(filter==='전체'||p.category===filter)&&[p.name,p.title,p.summary,p.stack,p.category].join(' ').toLocaleLowerCase().includes(query));
 counter.textContent=`${String(visible.length).padStart(2,'0')} PROJECTS / ${filter}`;
 grid.innerHTML=visible.length?visible.map(p=>`<article class="project"><div class="project-visual" aria-hidden="true"><span class="mono">${escapeHtml(p.id.toUpperCase())} / ${escapeHtml(p.category)}</span><span class="visual-shape"></span><span class="visual-type">${escapeHtml(p.name)}</span></div><div class="project-body"><div class="project-meta"><span>${escapeHtml(p.category)}</span><span>↗</span></div><h3>${escapeHtml(p.name)}</h3><p class="project-subtitle">${escapeHtml(p.title)}</p><p class="project-summary">${escapeHtml(p.summary)}</p><button class="project-link" data-project="${p.id}" aria-label="${escapeHtml(p.name)} 상세 보기"><span>프로젝트 노트 읽기</span><span aria-hidden="true">＋</span></button></div></article>`).join(''):'<p class="empty">검색 결과가 없습니다. 다른 단어나 분류로 찾아보세요.</p>';
}
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{filter=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));render()}));
search.addEventListener('input',render);
grid.addEventListener('click',event=>{const trigger=event.target.closest('[data-project]');if(!trigger)return;const p=projects.find(p=>p.id===trigger.dataset.project);if(!p)return;lastTrigger=trigger;document.querySelector('#dialog-content').innerHTML=`<p class="eyebrow">${escapeHtml(p.category)} / PROJECT NOTE</p><h2 id="dialog-title">${escapeHtml(p.name)}</h2><p>${escapeHtml(p.title)}</p><span class="tag">${escapeHtml(p.stack)}</span><h3>무엇을 다뤘나요?</h3><p>${escapeHtml(p.body)}</p><h3>작업 범위와 현재 상태</h3><p class="scope">${escapeHtml(p.scope)}</p>${p.url?`<div class="dialog-actions"><a class="text-link" href="${escapeHtml(p.url)}" target="_blank" rel="noopener noreferrer">코드와 실행 안내 보기 ↗</a></div>`:'<p>로컬 학습·실험 기록을 바탕으로 작성한 소개입니다. 원자료 다운로드는 제공하지 않습니다.</p>'}`;dialog.showModal()});
document.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}});
dialog.addEventListener('close',()=>lastTrigger?.focus());
const themeButton=document.querySelector('.theme-toggle');
function setTheme(theme){document.documentElement.dataset.theme=theme;themeButton.setAttribute('aria-label',theme==='dark'?'밝은 테마로 전환':'어두운 테마로 전환');themeButton.setAttribute('aria-pressed',String(theme==='dark'));try{localStorage.setItem('hojoon-theme',theme)}catch{}}
let theme='light';try{theme=localStorage.getItem('hojoon-theme')||'light'}catch{}setTheme(theme);
themeButton.addEventListener('click',()=>setTheme(document.documentElement.dataset.theme==='dark'?'light':'dark'));
document.querySelector('#year').textContent=new Date().getFullYear();
fetch('data/projects.json').then(r=>{if(!r.ok)throw new Error('HTTP '+r.status);return r.json()}).then(data=>{projects=data;render()}).catch(()=>{grid.innerHTML='<p class="empty">프로젝트 목록을 불러오지 못했습니다. <a class="text-link" href="https://github.com/JOON0512?tab=repositories">GitHub에서 프로젝트 보기 ↗</a></p>';counter.textContent=''});
// Set video ids and titles in data/videos.json. Only YouTube ids are accepted.
fetch('data/videos.json').then(r=>{if(!r.ok)throw new Error('videos');return r.json()}).then(videos=>{const safe=videos.filter(v=>/^[a-zA-Z0-9_-]{11}$/.test(v.id)&&v.title);if(!safe.length)return;document.querySelector('#videos').innerHTML='<div class="video-grid">'+safe.map(v=>`<article><iframe loading="lazy" src="https://www.youtube-nocookie.com/embed/${v.id}" title="${escapeHtml(v.title)}" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe><h3>${escapeHtml(v.title)}</h3><a class="text-link" href="https://www.youtube.com/watch?v=${v.id}" target="_blank" rel="noopener noreferrer">YouTube에서 보기 ↗</a></article>`).join('')+'</div>'}).catch(()=>{});
