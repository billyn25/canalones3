const solicitud = document.getElementById('solicitud-presupuesto');
if (solicitud) {
  const localidad = new URLSearchParams(location.hash.slice(1)).get('localidad');
  const valida = localidad && Array.from(document.querySelectorAll('#localidades li')).some(li => li.textContent === localidad);
  if (valida) {
    const lugar = localidad + ' (' + solicitud.elements.lugar.value + ')';
    solicitud.elements.lugar.value = lugar;
    for (const enlace of document.querySelectorAll('a[href*="municipio="], a[href^="https://wa.me/"]')) {
      const url = new URL(enlace.href);
      if (url.searchParams.has('municipio')) url.searchParams.set('municipio', lugar);
      else if (url.hostname === 'wa.me') url.searchParams.set('text', 'Hola, quería consultar por un trabajo de canalones o tejado en ' + lugar + '.');
      enlace.href = url.href;
    }
  }
  solicitud.hidden = false;
  solicitud.addEventListener('submit', event => {
    event.preventDefault();
    const lugar = solicitud.elements.lugar.value.trim();
    const barrio = solicitud.elements.barrio?.value.trim();
    const calle = solicitud.elements.calle?.value.trim();
    const ubicacion = [lugar, barrio, calle].filter(Boolean).join(', ');
    const detalle = solicitud.elements.detalle.value.trim();
    const rebose = solicitud.elements.rebose?.value;
    const mensaje = 'Hola, quisiera un presupuesto en ' + ubicacion + '.\n\n' + detalle + (rebose ? '\n\nCuándo rebosa: ' + rebose : '');
    location.assign('https://wa.me/' + solicitud.dataset.phone + '?text=' + encodeURIComponent(mensaje));
  });
}
