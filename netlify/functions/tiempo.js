const municipios = require('../../data/aemet.json');

async function texto(url, charset) {
  const res = await fetch(url, {signal: AbortSignal.timeout(8000)});
  if (!res.ok) throw Error('AEMET');
  return new TextDecoder(charset).decode(await res.arrayBuffer());
}

exports.handler = async event => {
  const codigo = event.queryStringParameters?.codigo;
  if (!/^\d{5}$/.test(codigo) || !municipios[codigo]) return {statusCode: 404, body: ''};
  const base = 'https://www.aemet.es';
  if (event.queryStringParameters?.vista === 'diaria') {
    try {
      const xml = await texto(base + '/xml/municipios/localidad_' + codigo + '.xml', 'iso-8859-1');
      return {statusCode:200, headers:{'Content-Type':'application/xml; charset=utf-8','Cache-Control':'public, max-age=900'}, body:xml};
    } catch { return {statusCode:503, body:''}; }
  }
  const [xml, pagina] = await Promise.allSettled([
    texto(base + '/xml/municipios_h/localidad_h_' + codigo + '.xml', 'iso-8859-1'),
    texto(base + '/es/eltiempo/prediccion/municipios/' + municipios[codigo], 'iso-8859-1')
  ]);
  const avisos = [];
  for (const tag of (pagina.value || '').match(/<a\b[^>]*>/gi) || []) {
    const periodo = tag.match(/avisos\?w=(hoy|mna|pmna)&/);
    const titulo = tag.match(/title="([^"]+)"/);
    if (periodo && titulo) avisos.push({periodo: periodo[1], titulo: titulo[1]});
  }
  return {statusCode: 200, headers: {'Content-Type':'application/json', 'Cache-Control':'public, max-age=' + (xml.value && avisos.length ? 300 : 30)}, body: JSON.stringify({xml:xml.value || '', avisos})};
};
