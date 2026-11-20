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
