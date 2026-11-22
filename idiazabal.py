RUTA = '/zonas/gipuzkoa/idiazabal/'
BASE = '/assets/obras/idiazabal/'
TITULO = 'Limpieza de tejas y reparación de goteras en Idiazabal'
FOTOS = [
    ('chimenea', 'Fragmentos de teja sobre la limahoya, junto al pie de la chimenea.'),
    ('encuentro', 'Detalle de la chapa que recoge el agua entre las dos pendientes.'),
    ('muro', 'Remate metálico al pie del muro, entre dos alturas de cubierta.'),
    ('remate', 'Piezas curvas de remate y mortero a la vista junto a la limahoya.'),
    ('faldon', 'Vista hacia el patio desde una hilera de tejas con un hueco entre piezas.'),
    ('vegetacion', 'Franja de musgo y helechos entre dos hileras de tejas.'),
]

def tarjeta():
    return f'<section class="obra"><h2>Trabajo en Idiazabal, Gipuzkoa</h2><a class="obra-tarjeta" href="{RUTA}#trabajo"><img loading="lazy" src="{BASE}chimenea-small.webp" alt="Fragmentos de teja en la limahoya junto a la chimenea"><div><strong>{TITULO}</strong><span>Ver las seis fotografías</span></div></a></section>'

def reportaje():
    fotos = ''.join(
        f'<figure><a data-foto href="{BASE}{nombre}.webp"><img loading="lazy" src="{BASE}{nombre}-small.webp" alt="{pie}"></a><figcaption>{pie}</figcaption></figure>'
        for nombre, pie in FOTOS
    )
    return (
        f'<section class="obra reportaje" id="trabajo"><h2>{TITULO}</h2>'
        '<p>En esta intervención de Alero Norte en Idiazabal hicimos trabajos de limpieza de tejas y reparación de goteras. Junto a la chimenea, dos pendientes del tejado vierten sobre una misma canal de chapa, la limahoya. En la fotografía se distinguen varios fragmentos de teja dentro del paso del agua.</p>'
        '<p>En otro tramo, la vegetación seguía una línea estrecha entre dos hileras de tejas. El primer plano permite distinguir los helechos y el musgo de las manchas claras que se ven sobre las piezas en la vista general.</p>'
        f'<div class="fotos-obra">{fotos}</div></section>'
    )
