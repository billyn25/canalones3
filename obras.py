"""Casos documentados con fotografías de trabajo aportadas por el propietario."""
CASOS = {
    'ugao-miraballes': ('Ugao-Miraballes', 'Limpieza integral de cubierta y canalones',
        'La intervención abarcó la cubierta y los canalones. Las dos imágenes permiten ver el faldón y el material vegetal recogido durante la limpieza.',
        [('ugao-vista-faldon', 'Vista del faldón de teja en Ugao-Miraballes.'),
         ('ugao-restos-hojas', 'Hojas y restos recogidos durante la limpieza integral.')]),
    'lekeitio': ('Lekeitio', 'Retirada de hojas del tejado y los canalones',
        'La limpieza incluyó la retirada de hojas del tejado y del canalón. En las fotos se aprecia cómo discurre el canalón por el borde de la cubierta y su posición respecto al alero.',
        [('lekeitio-tramo-canalon', 'Recorrido del canalón a lo largo del borde del tejado de Lekeitio.'),
         ('lekeitio-alero', 'Detalle del alero en la misma intervención.')]),
}

def foto(nombre, pie):
    return f'<figure><a href="/assets/obras/{nombre}-small.webp"><img loading="lazy" src="/assets/obras/{nombre}-small.webp" alt="{pie}"></a><figcaption>{pie}</figcaption></figure>'

def galeria(slug):
    lugar,titulo,texto,fotos=CASOS[slug]
    return f'<section class="obra"><h2>{titulo} en {lugar}</h2><p>{texto}</p><div class="fotos-obra">'+''.join(foto(*f) for f in fotos)+'</div></section>'

def destacados():
    tarjetas=''
    for slug,(lugar,titulo,texto,fotos) in CASOS.items():
        nombre,pie=fotos[1]
        tarjetas+=f'<a class="obra-tarjeta" href="/zonas/bizkaia/{slug}/#trabajo"><img loading="lazy" src="/assets/obras/{nombre}-small.webp" alt="{pie}"><div><small>{lugar}</small><strong>{titulo}</strong><span>Ver el trabajo</span></div></a>'
    return '<section class="wrap archivo-obras"><h2>Trabajos en Bizkaia</h2><div class="fotos-obra">'+tarjetas+'</div></section>'
