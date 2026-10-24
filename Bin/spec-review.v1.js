(function(){var rows=document.querySelectorAll('.seg');if(!rows.length)return;
function selection(){var sel={};document.querySelectorAll('.seg button[aria-pressed=true]').forEach(function(b){sel[b.dataset.f]=1;});return sel;}
function statusOf(el){return el.classList.contains('added')?'added':el.classList.contains('modified')?'modified':el.classList.contains('unchanged')?'unchanged':'removed';}
function apply(){var sel=selection(),any=Object.keys(sel).length>0;
function hide(el,h){el.classList.toggle('hid',any&&h);}
document.querySelectorAll('section.file').forEach(function(sec){var whole=sel.files&&sec.dataset.kind==='added';
function isCard(k){return k.classList.contains('item')||(k.tagName==='P'&&k.classList.contains('modified'));}
var groups=[],cur={head:null,kids:[],shown:0},total=0;
Array.prototype.forEach.call(sec.children,function(k){if(k.tagName==='H2')return;if(k.tagName==='H3'){groups.push(cur);cur={head:k,kids:[],shown:0};}else cur.kids.push(k);});groups.push(cur);
groups.forEach(function(g){g.kids.forEach(function(k){if(!isCard(k))return;var show=whole||sel[statusOf(k)]||(sel.gaps&&k.classList.contains('has-gap'));hide(k,!show);if(show)g.shown++;});total+=g.shown;});
groups.forEach(function(g,n){var keep=whole||(g.head?g.shown>0:total>0);g.kids.forEach(function(k){if(!isCard(k))hide(k,!keep);});if(g.head)hide(g.head,!keep);});
hide(sec,!(whole||total>0));});
document.querySelectorAll('section.discussion details.discussion').forEach(function(d){var g=d.classList.contains('gap'),r=d.classList.contains('resolved');var show=(sel.open&&!r&&!g)||(sel.gaps&&g)||(sel.resolved&&r);hide(d,!show);});
document.querySelectorAll('section.discussion h3.section').forEach(function(h){var n=h.nextElementSibling,vis=0;while(n&&n.tagName==='DETAILS'){if(!n.classList.contains('hid'))vis++;n=n.nextElementSibling;}hide(h,!vis);});
var disc=document.querySelector('section.discussion');if(disc)hide(disc,!disc.querySelector('details.discussion:not(.hid)'));}
function clearFilters(){document.querySelectorAll('.seg button[aria-pressed=true]').forEach(function(b){b.setAttribute('aria-pressed','false');});apply();}
rows.forEach(function(row){row.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;b.setAttribute('aria-pressed',b.getAttribute('aria-pressed')!=='true');apply();});});
window.__clearFilters=clearFilters;})();
(function(){var pop=document.getElementById('pop'),timer;
function show(a){var t=document.getElementById(a.dataset.tip);if(!t)return;pop.innerHTML='';pop.appendChild(t.content.cloneNode(true));
var rule=a.dataset.rule;if(rule){var rid=a.textContent.trim();var li=pop.querySelector('[data-rid="'+rid+'"]');if(li)li.classList.add('hit');}
var r=a.getBoundingClientRect();pop.style.display='block';var top=r.bottom+window.scrollY+6,left=Math.min(r.left+window.scrollX,window.scrollX+document.documentElement.clientWidth-pop.offsetWidth-16);
pop.style.top=top+'px';pop.style.left=Math.max(8,left)+'px';}
var wait;
document.addEventListener('mouseover',function(e){if(pop.contains(e.target))return;var a=e.target.closest('[data-tip]');if(a){clearTimeout(timer);clearTimeout(wait);wait=setTimeout(function(){show(a);},400);}});
document.addEventListener('mouseout',function(e){if(pop.contains(e.target))return;if(e.target.closest('[data-tip]')){clearTimeout(wait);timer=setTimeout(function(){pop.style.display='none';},150);}});
document.addEventListener('focusin',function(e){if(pop.contains(e.target))return;var a=e.target.closest('[data-tip]');if(a){clearTimeout(timer);clearTimeout(wait);show(a);}});
document.addEventListener('focusout',function(e){if(!pop.contains(e.target)&&e.target.closest('[data-tip]'))pop.style.display='none';});
pop.addEventListener('mouseenter',function(){clearTimeout(timer);});pop.addEventListener('mouseleave',function(){pop.style.display='none';});
})();
function openTarget(){var el=location.hash&&document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!el)return;
if(el.closest('.hid')&&window.__clearFilters)window.__clearFilters();
var d=el.closest('details');while(d){d.open=true;d=d.parentElement&&d.parentElement.closest('details');}el.scrollIntoView();}
addEventListener('hashchange',openTarget);openTarget();
