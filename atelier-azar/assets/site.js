/* Atelier Azar – shared script for every page. Each block only runs when its markup is on the page. */
{
const $=s=>document.querySelector(s);
const C=[
 {id:'shanghai',name:'Shanghai',d:"Un piédestal laqué noir aux lignes de pagode, ouvert en son cœur, sous un abat-jour rectangulaire doublé d'or.",f:[{n:'Black',img:{XL:'shanghai-xl',XXL:'shanghai-xxl'}}],s:{XL:['L 200 × P 110 cm','110 cm','3,00 m'],XXL:['L 250 × P 150 cm','150 cm','4,00 m']}},
 {id:'kailedo',name:'Kailedo',d:"Trois blocs martelés aux facettes irrégulières, qui accrochent la lumière comme un métal froissé.",f:[{n:'Silver',img:{XL:'kailedo-silver-xl',XXL:'kailedo-silver-xxl'}},{n:'Champagne',img:{XL:'kailedo-champagne-xl',XXL:'kailedo-champagne-xxl'}}],s:{XL:['L 200 × P 200 cm','100 cm','3,00 m'],XXL:['L 250 × P 250 cm','150 cm','4,00 m']},led:'XXL'},
 {id:'omaya',name:'Omaya',d:"Une colonne miroir creusée d'alvéoles, rythmée par des joints de lumière LED.",f:[{n:'Silver',img:{XL:'omaya-silver-xl',XXL:'omaya-silver-xxl'}},{n:'Champagne',img:{XL:'omaya-champagne-xl',XXL:'omaya-champagne-xxl'}}],s:{XL:['L 200 × P 200 cm','100 cm','3,00 m'],XXL:['L 250 × P 250 cm','150 cm','4,00 m']},led:'XL, XXL'},
 {id:'saint-moritz',name:'Saint-Moritz',d:"Le bois brut des chalets, posé sur un socle de marbre noir et souligné de LED.",f:[{n:'Woodee',img:{XL:'saint-moritz-xl',XXL:'saint-moritz-xxl'}}],s:{XL:['L 200 × P 200 cm','100 cm','3,00 m'],XXL:['L 250 × P 250 cm','150 cm','4,00 m']},led:'XL, XXL'},
 {id:'bali',name:'Bali',d:"Laque blanche sculptée et abat-jour rond en fibre tressée, pour les terrasses et les jardins.",f:[{n:'White lacquered',img:{XL:'bali-xl',XXL:'bali-xxl'}}],s:{XL:['Ø 200 cm','100 cm','3,00 m'],XXL:['Ø 250 cm','150 cm','4,00 m']},led:'XL, XXL'}
];
const G=[['scene-riviera','Shanghai Black au bord d\'une piscine à débordement, Riviera'],['scene-desert-silver','Omaya Silver dans un jardin de palmiers, la nuit'],['scene-terrasse','Omaya Silver sur une terrasse en béton au couchant'],['scene-bali-terrasse','Bali White sur une terrasse au crépuscule'],['scene-desert-champagne','Omaya Champagne entre les braseros'],['scene-salon','Kailedo dans un salon ouvert sur l\'océan'],['scene-bali-console','Deux lampes Bali sur une console ancienne']];
const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
const root=document.documentElement;

/* header: transparent over the top image, solid once scrolled past it */
const hd=$('#top'),top=$('.hero,.page-hero');
const onS=()=>hd.classList.toggle('solid',!top||scrollY>top.offsetHeight*.55);
addEventListener('scroll',onS,{passive:true});addEventListener('resize',onS);onS();

/* menu drawer */
const dr=$('#drawer'),mb=$('#menuBtn');
const closeD=()=>{dr.hidden=true;mb.setAttribute('aria-expanded','false');document.body.style.overflow=''};
mb.onclick=()=>{dr.hidden=false;mb.setAttribute('aria-expanded','true');document.body.style.overflow='hidden';$('#drawerClose').focus()};
$('#drawerClose').onclick=closeD;dr.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeD));
addEventListener('keydown',e=>{if(e.key=='Escape'&&!dr.hidden)closeD()});

/* images fade in once decoded */
const fadeIn=img=>{const on=()=>img.classList.add('in');img.complete&&img.naturalWidth?on():img.addEventListener('load',on,{once:true});img.addEventListener('error',on,{once:true})};
const fadeAll=()=>document.querySelectorAll('img.fx:not(.in)').forEach(fadeIn);

/* lightbox (collections + films pages) */
const lb=$('#lb'),lbImg=$('#lbImg'),lbInfo=$('#lbInfo');let last=null;
const openLB=()=>{last=document.activeElement;lb.hidden=false;document.body.style.overflow='hidden';$('#lbClose').focus()};
const closeLB=()=>{lb.hidden=true;document.body.style.overflow='';last&&last.focus()};
if(lb){$('#lbClose').onclick=closeLB;lb.addEventListener('click',e=>{if(e.target==lb)closeLB()});addEventListener('keydown',e=>{if(e.key=='Escape'&&!lb.hidden)closeLB()})}

/* collections grid with finish / size switches and product sheet */
const grid=$('#grid'),st={};
if(grid){
 const card=c=>{st[c.id]={f:0,s:'XL'};return `<article class="card" id="${c.id}" data-id="${c.id}">
 <button class="ph" aria-label="Ouvrir la fiche ${c.name}"><img class="fx" decoding="async" width="693" height="866" src="img/${c.f[0].img.XL}.webp" alt="${c.name} ${c.f[0].n} XL à côté d'une personne de 1,80 m" loading="lazy"></button>
 <div class="meta"><h3>${c.name}</h3><span>XL 3 m · XXL 4 m</span></div>
 <p class="desc">${c.d}</p>
 <div class="opts">${c.f.map((f,i)=>`<button data-f="${i}" aria-pressed="${i==0}">${f.n}</button>`).join('')}${['XL','XXL'].map(s=>`<button data-s="${s}" aria-pressed="${s=='XL'}">${s}</button>`).join('')}</div></article>`};
 grid.innerHTML=C.map(card).join('')+`<div class="card intro"><p class="label">Deux échelles</p><h3 style="margin:10px 0 12px">Chaque modèle existe en deux hauteurs</h3><p>Abat-jour noir doublé, socle massif, éclairage LED intégré selon les finitions.</p><dl><dt>XL</dt><dd>3,00 m de hauteur totale</dd><dt>XXL</dt><dd>4,00 m de hauteur totale</dd></dl></div>`;
 const swap=(img,src)=>{if(img.getAttribute('src')==src)return;const pre=new Image();pre.src=src;const go=()=>{img.style.opacity=.35;setTimeout(()=>{img.src=src;img.style.opacity=''},160)};pre.decode?pre.decode().then(go,go):pre.onload=go};
 const upd=el=>{const c=C.find(x=>x.id==el.dataset.id),s=st[c.id],img=el.querySelector('img');swap(img,`img/${c.f[s.f].img[s.s]}.webp`);img.alt=`${c.name} ${c.f[s.f].n} ${s.s} à côté d'une personne de 1,80 m`;el.querySelectorAll('[data-f]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.f==s.f));el.querySelectorAll('[data-s]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.s==s.s))};
 const drawP=id=>{const c=C.find(x=>x.id==id),s=st[id],f=c.f[s.f],sp=c.s[s.s];lbImg.src=`img/${f.img[s.s]}.webp`;lbImg.alt=`${c.name} ${f.n} ${s.s}, fiche à l'échelle`;
  lbInfo.innerHTML=`<p class="label">Collection</p><h2 style="margin:8px 0 14px">${c.name} ${s.s}</h2><p style="color:var(--soft)">${c.d}</p>
  <div class="opts">${c.f.map((x,i)=>`<button data-f="${i}" aria-pressed="${i==s.f}">${x.n}</button>`).join('')}${['XL','XXL'].map(z=>`<button data-s="${z}" aria-pressed="${z==s.s}">${z}</button>`).join('')}</div>
  <table><tr><td>Abat-jour</td><td>${sp[0]}</td></tr><tr><td>Hauteur abat-jour</td><td>${sp[1]}</td></tr><tr><td>Hauteur totale</td><td>${sp[2]}</td></tr><tr><td>Finition</td><td>${f.n}</td></tr>${c.led?`<tr><td>Éclairage LED</td><td>${c.led}</td></tr>`:''}</table>
  <p style="margin-top:24px"><a class="btn fill" href="contact.html?modele=${encodeURIComponent(c.name+' '+s.s)}">Demander un devis</a></p>`;lbInfo.dataset.id=id};
 grid.addEventListener('click',e=>{const el=e.target.closest('.card[data-id]'),b=e.target.closest('button');if(!el||!b)return;const s=st[el.dataset.id];if(b.dataset.f!=null)s.f=+b.dataset.f;else if(b.dataset.s)s.s=b.dataset.s;else{lb.classList.remove('pic');drawP(el.dataset.id);openLB();return}upd(el)});
 lbInfo.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const id=lbInfo.dataset.id,s=st[id];if(b.dataset.f!=null)s.f=+b.dataset.f;if(b.dataset.s)s.s=b.dataset.s;drawP(id);upd(grid.querySelector(`[data-id="${id}"]`))});
 const warm=()=>C.forEach(c=>c.f.forEach(f=>['XL','XXL'].forEach(z=>{const i=new Image();i.decoding='async';i.src=`img/${f.img[z]}.webp`})));
 addEventListener('load',()=>('requestIdleCallback' in window?requestIdleCallback(warm,{timeout:2500}):setTimeout(warm,1200)));
}

/* inspiration mosaic */
const mos=$('#mosaic');
if(mos){
 mos.innerHTML=G.map((g,i)=>`<button class="m${i+1}" data-i="${i}" aria-label="Agrandir : ${g[1]}"><img class="fx" src="img/${g[0]}.webp" alt="${g[1]}" loading="lazy" decoding="async"></button>`).join('');
 mos.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const g=G[b.dataset.i];lb.classList.add('pic');lbImg.src=`img/${g[0]}.webp`;lbImg.alt=g[1];openLB()});
}
fadeAll();

/* videos: play only near the viewport, respect reduced motion */
const vids=[...document.querySelectorAll('video.v')],ht=$('#heroToggle'),heroV=$('.hero video');
if(rm){vids.forEach(v=>{v.removeAttribute('autoplay');v.pause()});if(ht){ht.textContent='Lecture';ht.setAttribute('aria-pressed','true')}}
const paused=v=>v==heroV&&ht&&ht.getAttribute('aria-pressed')=='true';
const vio=new IntersectionObserver(es=>es.forEach(en=>{const v=en.target;if(en.isIntersecting&&!rm&&!paused(v)){const p=v.play();p&&p.catch(()=>{})}else v.pause()}),{threshold:.01,rootMargin:'250px 0px'});
vids.forEach(v=>vio.observe(v));
if(ht)ht.onclick=()=>{if(ht.getAttribute('aria-pressed')=='true'){heroV.play().catch(()=>{});ht.textContent='Pause';ht.setAttribute('aria-pressed','false')}else{heroV.pause();ht.textContent='Lecture';ht.setAttribute('aria-pressed','true')}};

/* home intro: monogram wipe, name written, then hand over to header + headline */
const intro=$('#intro');
if(intro){
 const endIntro=()=>{if(!root.classList.contains('intro-on'))return;intro.classList.add('out');root.classList.remove('intro-on');try{sessionStorage.setItem('azarIntro','1')}catch(e){}};
 if(root.classList.contains('intro-on')){setTimeout(endIntro,5600);addEventListener('wheel',endIntro,{once:true,passive:true});addEventListener('touchmove',endIntro,{once:true,passive:true});addEventListener('keydown',endIntro,{once:true})}else intro.hidden=true;
}

/* scale drawing */
const fig=$('#fig');
if(fig){
 const ceil=$('#ceil'),out=$('#ceilOut'),ver=$('#verdict');
 const fmt=n=>n.toFixed(2).replace('.',',')+' m';
 const lamp=(x,base,k,h,w,lbl)=>{const sh=(h==3?1:1.5)*k,sw=w*k,col=.46*w*k/2,t=base-h*k;return `<g>
  <rect x="${x-sw*.22}" y="${base-.12*k}" width="${sw*.44}" height="${.12*k}" fill="var(--ink)"/>
  <rect x="${x-col/2}" y="${t+sh+.18*k}" width="${col}" height="${base-.12*k-(t+sh+.18*k)}" fill="var(--gold)"/>
  <rect x="${x-1.5}" y="${t+sh}" width="3" height="${.18*k}" fill="var(--ink)"/>
  <rect x="${x-sw/2}" y="${t}" width="${sw}" height="${sh}" fill="var(--ink)"/>
  <rect x="${x-sw/2}" y="${t+sh-3}" width="${sw}" height="3" fill="var(--gold)"/>
  <text x="${x}" y="${t-10}" text-anchor="middle">${lbl}</text></g>`};
 const person=(x,base,k)=>{const h=1.8*k;return `<g fill="var(--soft)"><circle cx="${x}" cy="${base-h+.11*k}" r="${.11*k}"/><rect x="${x-.2*k}" y="${base-h+.25*k}" width="${.4*k}" height="${.7*k}" rx="${.06*k}"/><rect x="${x-.17*k}" y="${base-h+.9*k}" width="${.15*k}" height="${.9*k}"/><rect x="${x+.02*k}" y="${base-h+.9*k}" width="${.15*k}" height="${.9*k}"/><text x="${x}" y="${base-h-10}" text-anchor="middle" style="fill:var(--ink)">1,80 m</text></g>`};
 const draw=()=>{const W=fig.clientWidth,H=fig.clientHeight,c=+ceil.value,mt=34,mbot=34,ml=58,mr=20;
  const k=Math.min((H-mt-mbot)/Math.max(c,4.2),(W-ml-mr)/6.6),base=H-mbot,cy=base-c*k;
  const x0=ml+((W-ml-mr)-6.6*k)/2,fit=h=>c>=h+.3;
  let ticks='';for(let m=0;m<=Math.floor(Math.max(c,4.2));m++){const y=base-m*k;ticks+=`<line x1="${ml-8}" x2="${ml-2}" y1="${y}" y2="${y}" stroke="var(--soft)"/><text x="${ml-14}" y="${y+5}" text-anchor="end" style="font-size:13px;fill:var(--soft)">${m} m</text>`}
  fig.innerHTML=`<svg viewBox="0 0 ${W} ${H}" aria-hidden="true">
  <line x1="${ml-2}" x2="${ml-2}" y1="${base}" y2="${base-Math.max(c,4.2)*k}" stroke="var(--soft)"/>${ticks}
  <rect x="${ml}" y="${Math.max(cy-14,4)}" width="${W-ml-mr}" height="14" fill="var(--line)"/>
  <line x1="${ml}" x2="${W-mr}" y1="${cy}" y2="${cy}" stroke="var(--ink)" stroke-dasharray="${c<4.3?'5 4':'0'}"/>
  <text x="${ml+6}" y="${cy+20}">Plafond ${fmt(c)}</text>
  <line x1="${ml}" x2="${W-mr}" y1="${base}" y2="${base}" stroke="var(--ink)"/>
  ${person(x0+.35*k,base,k)}
  <g opacity="${fit(3)?1:.28}">${lamp(x0+1.95*k,base,k,3,2,'XL · 3 m')}</g>
  <g opacity="${fit(4)?1:.28}">${lamp(x0+5.15*k,base,k,4,2.5,'XXL · 4 m')}</g></svg>`;
  out.textContent=fmt(c);
  ver.innerHTML=fit(4)?`<b>Les deux versions trouvent leur place.</b> Au-delà de 4,30 m, la XXL donne toute sa mesure ; la XL reste l'option la plus aérienne.`:fit(3)?`<b>La version XL est idéale.</b> Il manque ${fmt(4.3-c)} pour accueillir la XXL avec 30 cm de dégagement.`:`<b>Plafond bas pour une pièce monumentale.</b> Parlons d'une hauteur sur mesure, ou d'une installation en extérieur.`};
 ceil.addEventListener('input',draw);const ro=new ResizeObserver(draw);ro.observe(fig);
}

/* contact form: model list, preselect from ?modele=, prepare the e-mail */
const form=$('#form');
if(form){
 const sel=$('#f-model');
 C.forEach(c=>['XL','XXL'].forEach(s=>{const o=document.createElement('option');o.textContent=c.name+' '+s;sel.appendChild(o)}));
 try{const m=new URLSearchParams(location.search).get('modele');if(m&&[...sel.options].some(o=>o.value==m))sel.value=m}catch(e){}
 form.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(form),n=(d.get('name')||'').trim(),m=(d.get('email')||'').trim();
  form.querySelector('.ok')?.remove();const ok=document.createElement('p');ok.className='ok';
  if(!n||!/.+@.+\..+/.test(m)){ok.textContent='Merci d\'indiquer votre nom et une adresse e-mail valide.';form.appendChild(ok);return}
  const body=`Nom : ${n}\nE-mail : ${m}\nTéléphone : ${d.get('tel')||''}\nModèle : ${d.get('model')}\n\n${d.get('msg')||''}`;
  const a=document.createElement('a');a.href=`mailto:info@redzone.ch?subject=${encodeURIComponent('Projet Atelier Azar – '+d.get('model'))}&body=${encodeURIComponent(body)}`;a.textContent='ouvrir le message dans votre messagerie';
  ok.append('Votre demande est prête. Dernière étape : ',a,' et l\'envoyer à info@redzone.ch.');form.appendChild(ok)});
}
}
