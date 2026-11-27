for (const panel of document.querySelectorAll('[data-codigo]')) {
  const output = panel.querySelector('.weather-output');
  let busy = false;
  let loaded = 0;
  panel.addEventListener('toggle', async () => {
    if (!panel.open || busy || Date.now() - loaded < 300000) return;
    busy = true;
    output.textContent = 'Consultando AEMET…';
    try {
      const response = await fetch('/.netlify/functions/tiempo?codigo=' + panel.dataset.codigo);
      if (!response.ok) throw Error();
      const {xml, avisos} = await response.json();
      const doc = new DOMParser().parseFromString(xml, 'application/xml');
      const now = new Intl.DateTimeFormat('sv-SE', {timeZone:'Europe/Madrid', year:'numeric', month:'2-digit', day:'2-digit', hour:'2-digit', hourCycle:'h23'}).format(new Date()).replace(/[^0-9]/g, '');
      const table = document.createElement('table');
      table.createCaption().textContent = 'Horas peninsulares · AEMET';
      const head = table.createTHead().insertRow();
      for (const label of ['Día / hora','Lluvia (mm)','Viento (km/h)','Racha (km/h)']) {
        const th = document.createElement('th'); th.textContent = label; head.append(th);
      }
      const body = table.createTBody();
      for (const dia of doc.querySelectorAll('prediccion > dia')) {
        const date = dia.getAttribute('fecha');
        for (const temp of dia.querySelectorAll('temperatura[periodo]')) {
          const hour = temp.getAttribute('periodo');
          if (date.replaceAll('-', '') + hour < now || body.rows.length >= 12) continue;
          const val = selector => dia.querySelector(selector)?.textContent.trim() || '—';
          const attr = '[periodo="' + hour + '"]';
          const row = body.insertRow();
          for (const value of [date.slice(8) + '/' + date.slice(5,7) + ' ' + hour + ' h', val('precipitacion'+attr), val('viento'+attr+' velocidad'), val('racha_max'+attr)]) row.insertCell().textContent = value;
        }
      }
      output.replaceChildren();
      if (body.rows.length) output.append(table);
      else output.append('Previsión horaria no disponible en este momento.');
      const note = document.createElement('p');
      const dias = {hoy:'Hoy', mna:'Mañana', pmna:'Pasado mañana'};
      note.textContent = avisos.length ? 'Avisos AEMET · ' + avisos.map(a => dias[a.periodo] + ': ' + a.titulo).join(' · ') : 'Avisos de la zona no disponibles en este momento.';
      output.append(note);
      if (avisos.length && body.rows.length) loaded = Date.now();
    } catch {
      output.textContent = 'No se ha podido consultar AEMET. Cierra y abre este apartado para volver a intentarlo.';
    } finally { busy = false; }
  });
}

async function cargarDias(panel) {
  try {
    const res = await fetch('/.netlify/functions/tiempo?vista=diaria&codigo=' + panel.dataset.diaria);
    if (!res.ok) throw Error();
    const doc = new DOMParser().parseFromString(await res.text(), 'application/xml');
    const hoy = new Intl.DateTimeFormat('sv-SE',{timeZone:'Europe/Madrid'}).format(new Date());
    const dias = [...doc.querySelectorAll('prediccion > dia')].filter(d => d.getAttribute('fecha') >= hoy).slice(0,3);
    if (!dias.length) throw Error();
    for (const d of dias) {
      const card = document.createElement('article');
      const line = (tag, value) => { const el=document.createElement(tag); el.textContent=value; card.append(el); };
      line('h3',new Intl.DateTimeFormat('es-ES',{weekday:'long',day:'numeric',month:'short',timeZone:'UTC'}).format(new Date(d.getAttribute('fecha')+'T12:00:00Z')));
      const val = s => d.querySelector(s)?.textContent.trim() || '—';
      line('p','Mín. '+val('temperatura > minima')+' °C · Máx. '+val('temperatura > maxima')+' °C');
      const cielos = [...d.querySelectorAll('estado_cielo')].filter(e=>e.getAttribute('descripcion'));
      const partes = cielos.some(e=>e.getAttribute('periodo')==='00-24') ? cielos.filter(e=>e.getAttribute('periodo')==='00-24') : cielos.filter(e=>!cielos.some(o=>o!==e && o.getAttribute('periodo') && e.getAttribute('periodo') && o.getAttribute('periodo').slice(0,2)>=e.getAttribute('periodo').slice(0,2) && o.getAttribute('periodo').slice(-2)<=e.getAttribute('periodo').slice(-2)));
      for(const e of partes){
        const periodo=e.getAttribute('periodo');
        const attr=periodo?'[periodo="'+periodo+'"]':':not([periodo])';
        line('strong',(periodo && periodo!=='00-24'?periodo+' h · ':'')+e.getAttribute('descripcion'));
        line('p','Lluvia: '+val('prob_precipitacion'+attr)+' % · Viento: '+val('viento'+attr+' velocidad')+' km/h');
      }
      panel.append(card);
    }
  } catch { panel.textContent='Previsión diaria no disponible. Puedes consultarla en el enlace de AEMET.'; }
}
document.querySelectorAll('[data-diaria]').forEach(cargarDias);
