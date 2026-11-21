(() => {
  const form = document.getElementById('consulta');
  if (!form) return;
  const result = document.getElementById('consulta-resultado');
  const output = result.querySelector('textarea');
  const status = result.querySelector('[role=status]');
  form.hidden = false;
  if (location.hash === '#comunidad') form.elements.inmueble.value = 'Comunidad de vecinos';
  form.elements.lugar.value = (new URLSearchParams(location.search).get('municipio') || '').slice(0, 140);
  if (location.hash === '#gotera') form.elements.motivo.value = 'Gotera o filtración';
  const sintomas = {
    'junto-bajante': ['Limpieza de canalones', 'El canalón rebosa junto a la bajante.'],
    fachada: ['Limpieza de canalones', 'El canalón rebosa a lo largo de la fachada.'],
    hojas: ['Limpieza de tejado', 'Hay hojas acumuladas en el tejado.'],
    tramo: ['Limpieza de canalones', 'Quiero presupuesto para limpiar un tramo del canalón.']
  };
  const clave = new URLSearchParams(location.hash.slice(1)).get('sintoma');
  if (Object.hasOwn(sintomas, clave)) {
    [form.elements.motivo.value, form.elements.detalle.value] = sintomas[clave];
  }
  form.addEventListener('input', () => { result.hidden = true; });
  form.addEventListener('submit', event => {
    event.preventDefault();
    const fields = new FormData(form);
    const labels = {lugar: 'Ubicación', inmueble: 'Inmueble', motivo: 'Servicio', detalle: 'Observaciones', rebose: 'Cuándo rebosa', acceso: 'Acceso y disponibilidad'};
    const summary = ['Consulta para Alero Norte'];
    for (const [key, label] of Object.entries(labels)) {
      const value = (fields.get(key) || '').trim();
      if (value) summary.push(label + ': ' + value);
    }
    output.value = summary.join('\n\n');
    const share = result.querySelector('[data-share]');
    if (form.dataset.phone) {
      share.href = 'https://wa.me/' + form.dataset.phone + '?text=' + encodeURIComponent(output.value);
      share.hidden = false;
      if (event.submitter?.value !== 'resumen') {
        location.assign(share.href);
        return;
      }
    }
    status.textContent = '';
    result.hidden = false;
    result.querySelector('h2').focus();
  });
  result.querySelector('[data-copy]').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(output.value);
      status.textContent = 'Resumen copiado.';
    } catch {
      output.focus();
      output.select();
      status.textContent = 'Texto seleccionado. Usa la opción Copiar de tu dispositivo.';
    }
  });
  result.querySelector('[data-save]').addEventListener('click', () => {
    const url = URL.createObjectURL(new Blob([output.value], {type: 'text/plain;charset=utf-8'}));
    const link = document.createElement('a');
    link.href = url;
    link.download = 'consulta-alero-norte.txt';
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
})();
