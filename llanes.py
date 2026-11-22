RUTA = '/trabajos/reparacion-limpieza-tejado-llanes/'
TITULO = 'Reparación y limpieza de tejado en Llanes'
BASE = '/assets/obras/llanes/'
FOTOS = [
    ('ventanas', 'Dos ventanas de cubierta situadas a distinta altura en el mismo faldón.'),
    ('helechos', 'Helechos y restos vegetales junto al lateral de la ventana inferior.'),
    ('alero', 'Vista desde la ventana hacia el alero, con vegetación entre dos hileras de tejas.'),
    ('solapes', 'Detalle del hueco entre piezas de teja curva bajo la cumbrera.'),
    ('cumbrera', 'Vista de las hileras de tejas y su encuentro con el remate superior.'),
]

def tarjeta():
    return f'<section class="obra"><h2>Trabajo en Llanes, Asturias</h2><a class="obra-tarjeta" href="{RUTA}"><img loading="lazy" src="{BASE}helechos-small.webp" alt="Helechos junto a una ventana de tejado"><div><strong>{TITULO}</strong><span>Ver las cinco fotografías</span></div></a></section>'

def reportaje():
    fotos = ''.join(
        f'<figure><a data-foto href="{BASE}{nombre}.webp"><img loading="lazy" src="{BASE}{nombre}-small.webp" alt="{pie}"></a><figcaption>{pie}</figcaption></figure>'
        for nombre, pie in FOTOS
    )
    return (
        '<section class="obra reportaje"><h2>Dos ventanas en una cubierta de teja curva</h2>'
        '<p>Alero Norte realizó este trabajo de reparación y limpieza en Llanes, Asturias. En la ventana inferior se habían acumulado tallos y hojas entre el marco y las tejas. Siguiendo la pendiente hacia el alero se ve otro grupo de helechos, separado de la ventana por varias filas de teja.</p>'
        '<p>Las fotos de la parte alta muestran otro detalle de la misma cubierta. Bajo la cumbrera se distingue un hueco entre piezas. La vista general sitúa esa zona y el primer plano permite ver cómo apoyan unas tejas sobre otras.</p>'
        f'<div class="fotos-obra">{fotos}</div></section>'
    )
