const field=document.querySelector('.filter');
field.hidden=false;
const norm=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const aliases={vitoria:'gasteiz',san:'', 'san sebastian':'donostia', 'san sebastián':'donostia', bilbo:'bilbao', guernica:'gernika'};
field.querySelector('input').addEventListener('input',event=>{
 const q=norm(event.target.value.trim()), keys=[q,aliases[q]].filter(Boolean);
 let count=0;
 document.querySelectorAll('li[data-localidades]').forEach(item => {
   const principal = item.querySelector('a');
   item.querySelector('.coincidencias')?.remove();
   const municipal = !q || keys.some(k => norm(principal.textContent).includes(k));
   const nucleos = q.length >= 2 ? item.dataset.localidades.split(' | ').filter(nombre =>
     norm(nombre) !== norm(principal.textContent) && keys.some(k => norm(nombre).includes(k))) : [];
   item.hidden = !municipal && !nucleos.length;
   if (!item.hidden) count++;
   if (nucleos.length) {
     const lista = document.createElement('div');
     lista.className = 'coincidencias';
     for (const nombre of nucleos) {
       const enlace = document.createElement('a');
       enlace.href = principal.pathname + '#' + new URLSearchParams({localidad: nombre});
       enlace.textContent = nombre + ' (' + principal.textContent + ')';
       lista.append(enlace, document.createElement('br'));
     }
     item.append(lista);
   }
 });
 document.querySelectorAll('section:has(.municipios)').forEach(s=>s.hidden=!s.querySelector('li:not([hidden])'));
 document.querySelector('#resultados').textContent=q?count+' municipios encontrados':'';
});
