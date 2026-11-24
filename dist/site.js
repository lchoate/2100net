document.documentElement.classList.add('js');
const menu=document.querySelector('.menu');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));document.querySelector('#navigation').classList.toggle('open',open)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.getAttribute('aria-expanded')==='true'){menu.click();menu.focus()}});
const clock=document.querySelector('[data-arizona-time]');
function updateClock(){if(clock)clock.textContent=new Intl.DateTimeFormat('en-US',{timeZone:'America/Phoenix',hour:'2-digit',minute:'2-digit',hour12:false}).format(new Date())+' MST'}
updateClock();if(clock)setInterval(updateClock,30000);
