const solicitud = document.getElementById('solicitud-presupuesto');
if (solicitud) {
  solicitud.hidden = false;
  solicitud.addEventListener('submit', event => {
    event.preventDefault();
    const lugar = solicitud.elements.lugar.value.trim();
    const detalle = solicitud.elements.detalle.value.trim();
    const rebose = solicitud.elements.rebose?.value;
    const mensaje = 'Hola, quisiera un presupuesto en ' + lugar + '.\n\n' + detalle + (rebose ? '\n\nCuándo rebosa: ' + rebose : '');
    location.assign('https://wa.me/' + solicitud.dataset.phone + '?text=' + encodeURIComponent(mensaje));
  });
}
