const solicitud = document.getElementById('solicitud-presupuesto');
if (solicitud) {
  solicitud.hidden = false;
  solicitud.addEventListener('submit', event => {
    event.preventDefault();
    const lugar = solicitud.elements.lugar.value.trim();
    const detalle = solicitud.elements.detalle.value.trim();
    const mensaje = 'Hola, quisiera un presupuesto en ' + lugar + '.\n\n' + detalle;
    location.assign('https://wa.me/' + solicitud.dataset.phone + '?text=' + encodeURIComponent(mensaje));
  });
}
