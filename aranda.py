RUTA = '/zonas/burgos/aranda-de-duero/'
BASE = '/assets/obras/aranda-de-duero/'
FOTOS = [
    ('hileras', 'Tallos secos y restos entre las hileras de teja curva.'),
    ('pendiente', 'Vista del faldón hacia la calle con vegetación en los canales.'),
    ('cumbrera', 'Piezas de cumbrera y mortero sobre las primeras filas de tejas.'),
    ('solapes', 'Detalle de los solapes y los líquenes en la superficie de las tejas.'),
    ('musgo', 'Pequeños grupos de musgo sobre la teja cerámica.'),
    ('alero', 'Vegetación en el borde de la cubierta gris sobre el patio.'),
]

def tarjeta():
    return f'<section class="obra"><h2>Trabajo en Aranda de Duero</h2><a class="obra-tarjeta" href="{RUTA}#trabajo"><img loading="lazy" src="{BASE}hileras-small.webp" alt="Restos vegetales entre las tejas"><span>Ver las seis fotografías de las cubiertas</span></a></section>'

def reportaje():
    fotos = ''.join(
        f'<figure><a data-foto href="{BASE}{nombre}.webp"><img loading="lazy" src="{BASE}{nombre}-small.webp" alt="{pie}"></a><figcaption>{pie}</figcaption></figure>'
        for nombre, pie in FOTOS
    )
    return (
        '<section class="obra reportaje" id="trabajo"><h2>Cubiertas en Aranda de Duero</h2>'
        '<p>En las fotos de Alero Norte en Aranda se aprecia dónde se acumula la vegetación. En la cubierta de teja curva, los tallos secos siguen los surcos por los que baja la lluvia. En la cubierta gris se ven pequeños grupos de musgo sobre el faldón y una línea de hierba justo en el alero.</p>'
        f'<div class="fotos-obra">{fotos}</div></section>'
    )
