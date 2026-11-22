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
  const tramosPorTipo = {
    'Casa o caserío': ['Fachada principal', 'Parte trasera', 'Porche', 'Garaje o anexo'],
    'Comunidad': ['Fachada a la calle', 'Patio interior', 'Varios portales', 'Bajante compartida'],
    'Nave': ['Un lateral', 'Ambos laterales', 'Zona de carga', 'Bajante concreta']
  };
  const tipo = solicitud.elements.tipo_limpieza;
  const grupo = solicitud.querySelector('.tramos-limpieza');
  const acceso = solicitud.querySelector('[data-acceso-patio]');
  function mostrarAcceso() {
    acceso.hidden = !grupo.querySelector('input[value="Patio interior"]:checked');
    if (acceso.hidden) solicitud.elements.acceso_patio.value = '';
  }
  function mostrarTramos() {
    const opciones = tramosPorTipo[tipo.value] || [];
    const lista = grupo.querySelector('[data-tramos]');
    lista.replaceChildren();
    for (const nombre of opciones) {
      const etiqueta = document.createElement('label');
      const casilla = document.createElement('input');
      casilla.type = 'checkbox';
      casilla.name = 'tramo';
      casilla.value = nombre;
      etiqueta.append(casilla, nombre);
      lista.append(etiqueta);
    }
    grupo.hidden = !opciones.length;
    mostrarAcceso();
  }
  if (tipo && grupo && acceso) {
    tipo.addEventListener('change', mostrarTramos);
    grupo.addEventListener('change', event => {
      const actual = event.target;
      if (actual.checked && ['Un lateral', 'Ambos laterales'].includes(actual.value)) {
        for (const otra of grupo.querySelectorAll('input')) {
          if (otra !== actual && ['Un lateral', 'Ambos laterales'].includes(otra.value)) otra.checked = false;
        }
      }
      mostrarAcceso();
    });
    mostrarTramos();
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
    const elegidos = Array.from(solicitud.querySelectorAll('input[name="tramo"]:checked'), campo => campo.value);
    const alcance = [tipo?.value, elegidos.length && 'Tramos: ' + elegidos.join(', '), solicitud.elements.acceso_patio?.value && 'Acceso al patio: ' + solicitud.elements.acceso_patio.value].filter(Boolean).join('\n');
    const mensaje = 'Hola, quisiera un presupuesto en ' + ubicacion + '.\n\n' + detalle + (alcance ? '\n\n' + alcance : '') + (rebose ? '\n\nCuándo rebosa: ' + rebose : '');
    location.assign('https://wa.me/' + solicitud.dataset.phone + '?text=' + encodeURIComponent(mensaje));
  });
}
