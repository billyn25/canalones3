RUTA = '/zonas/cantabria/comillas/'
BASE = '/assets/obras/comillas/'
FOTOS = [
    ('faldon', 'Vista del faldón y del canalón lateral entre las dos alturas de cubierta.'),
    ('fisura', 'Teja fisurada junto a restos vegetales y al remate metálico.'),
    ('cumbrera', 'Vista hacia la cumbrera que sitúa la pieza fisurada en el lado derecho.'),
    ('fragmentos', 'Fragmentos de cerámica sueltos entre varias hileras de tejas.'),
    ('encuentros', 'Encuentro entre varios faldones con remates de teja y mortero.'),
    ('alero', 'Última fila de tejas sobre el canalón, vista desde arriba.'),
    ('solape', 'Borde roto de una teja en el solape frente a la fachada.'),
]

def tarjeta():
    return f'<section class="obra"><h2>Trabajo en Comillas, Cantabria</h2><a class="obra-tarjeta" href="{RUTA}#trabajo"><img loading="lazy" src="{BASE}faldon-small.webp" alt="Faldón de teja curva junto al canalón"><div><strong>Las tejas y el canalón de una cubierta en Comillas</strong><span>Ver las siete fotos</span></div></a></section>'

def reportaje():
    fotos = ''.join(
        f'<figure><a data-foto href="{BASE}{nombre}.webp"><img loading="lazy" src="{BASE}{nombre}-small.webp" alt="{pie}"></a><figcaption>{pie}</figcaption></figure>'
        for nombre, pie in FOTOS
    )
    return (
        '<section class="obra reportaje" id="trabajo"><h2>Una cubierta de teja curva en Comillas</h2>'
        '<p>En las fotos de este trabajo de Alero Norte se aprecia una teja con el borde partido junto al canalón. La vista desde la cumbrera ayuda a situarla. En el primer plano se distingue la fisura y, a su lado, los restos vegetales encajados entre las piezas.</p>'
        '<p>Otra imagen sigue el canalón que discurre entre dos alturas de cubierta. Se ve tanto la última fila de tejas que vierte sobre él como la chapa que enlaza ambos tramos.</p>'
        f'<div class="fotos-obra">{fotos}</div></section>'
    )
