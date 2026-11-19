const field=document.querySelector('.filter');
field.hidden=false;
const norm=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const aliases={vitoria:'gasteiz',san:'', 'san sebastian':'donostia', 'san sebastián':'donostia', bilbo:'bilbao', guernica:'gernika'};
field.querySelector('input').addEventListener('input',event=>{
 const q=norm(event.target.value.trim()), keys=[q,aliases[q]].filter(Boolean);
 let count=0;
 document.querySelectorAll('.municipios li').forEach(item=>{item.hidden=!!q&&!keys.some(k=>norm(item.textContent+' '+(item.dataset.localidades||'')).includes(k));if(!item.hidden)count++;});
 document.querySelectorAll('section:has(.municipios)').forEach(s=>s.hidden=!s.querySelector('li:not([hidden])'));
 document.querySelector('#resultados').textContent=q?count+' municipios encontrados':'';
});
