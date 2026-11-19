const fotos = Array.from(document.querySelectorAll('a[data-foto]'));
if (fotos.length && typeof HTMLDialogElement !== 'undefined') {
  const visor = document.createElement('dialog');
  visor.className = 'visor';
  visor.setAttribute('aria-label', 'Galería de fotografías');
  visor.innerHTML = '<button type="button" class="cerrar" aria-label="Cerrar galería">×</button><img alt=""><div class="controles"><button type="button" aria-label="Foto anterior">‹</button><p aria-live="polite"></p><button type="button" aria-label="Foto siguiente">›</button></div>';
  document.body.append(visor);
  const [cerrar, anterior, siguiente] = visor.querySelectorAll('button');
  let indice = 0;
  function mostrar(i) {
    indice = (i + fotos.length) % fotos.length;
    const enlace = fotos[indice];
    const imagen = visor.querySelector('img');
    imagen.alt = enlace.querySelector('img').alt;
    imagen.src = enlace.href;
    visor.querySelector('p').textContent = (indice+1)+' / '+fotos.length+' · '+imagen.alt;
  }
  fotos.forEach((enlace,i)=>enlace.addEventListener('click',e=>{
    if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;
    e.preventDefault();
    mostrar(i);
    visor.showModal();
    cerrar.focus();
  }));
  cerrar.onclick=()=>visor.close();
  anterior.onclick=()=>mostrar(indice-1);
  siguiente.onclick=()=>mostrar(indice+1);
  visor.addEventListener('click',e=>{if(e.target===visor) visor.close()});
  visor.addEventListener('keydown',e=>{
    if(e.key==='ArrowLeft') mostrar(indice-1);
    if(e.key==='ArrowRight') mostrar(indice+1);
  });
}
