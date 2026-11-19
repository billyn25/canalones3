"""Casos documentados con fotografías de trabajo aportadas por el propietario."""
import json
from pathlib import Path
from html import escape

FOTOS=json.loads((Path(__file__).parent/'data/fotos.json').read_text())
ORIGINALES='https://raw.githubusercontent.com/billyn25/canalones2/ecb4ce8d38b41e6e6cf7791809537162f66a9548/assets/trabajos/'
CASOS = {
    'ugao-miraballes': ('Ugao-Miraballes', 'Limpieza integral de cubierta y canalones',
        'La intervención abarcó la cubierta y los canalones. Las fotografías permiten ver el faldón y el material vegetal recogido durante la limpieza.',
        [('ugao-vista-faldon', 'Vista del faldón de teja en Ugao-Miraballes.'),
         ('ugao-restos-hojas', 'Hojas y restos recogidos durante la limpieza integral.')]),
    'lekeitio': ('Lekeitio', 'Retirada de hojas del tejado y los canalones',
        'La limpieza incluyó la retirada de hojas del tejado y del canalón. En las fotos se aprecia cómo discurre el canalón por el borde de la cubierta y su posición respecto al alero.',
        [('lekeitio-tramo-canalon', 'Recorrido del canalón a lo largo del borde del tejado de Lekeitio.'),
         ('lekeitio-alero', 'Detalle del alero en la misma intervención.')]),
}

for clave,prefijo in [('ugao-miraballes','ugao-'),('lekeitio','lekeitio-')]:
    fotos=CASOS[clave][3]
    existentes={nombre for nombre,_ in fotos}
    fotos.extend((f['id'],f['alt']) for f in FOTOS if f['id'].startswith(prefijo) and f['id'] not in existentes)

def foto(nombre, pie):
    mini=nombre+'-small.webp'
    local=Path(__file__).parent/'assets'/'obras'/mini
    src='/assets/obras/'+mini if local.exists() else ORIGINALES+mini
    return f'<figure><a data-foto href="{ORIGINALES}{nombre}.webp"><img loading="lazy" src="{src}" alt="{escape(pie,quote=True)}"></a><figcaption>{escape(pie)}</figcaption></figure>'

def album():
    usados=set()
    bloques=[]
    def grupo(titulo,texto,seleccion,url=None):
        usados.update(f['id'] for f in seleccion)
        enlace=f'<p><a href="{url}">Ver el trabajo completo</a></p>' if url else ''
        bloques.append('<section class="obra"><h2>'+titulo+'</h2><p>'+texto+'</p>'+enlace+'<div class="fotos-obra">'+''.join(foto(f['id'],f['alt']) for f in seleccion)+'</div></section>')
    for slug,(lugar,titulo,texto,fotos) in CASOS.items():
        ids={nombre for nombre,_ in fotos}
        grupo(lugar+' · '+titulo,texto,[f for f in FOTOS if f['id'] in ids],'/zonas/bizkaia/'+slug+'/#trabajo')
    grupo('Provincia de León · Del tejado a la bajante','Cuatro vistas del mismo trabajo sitúan las tejas, el alero, el canalón y su salida.',[f for f in FOTOS if f['id'] in {'tejas-suciedad','canalon-alero','leon-canalon-lateral','leon-salida-canalon'}],RUTA_LEON)
    grupo('Detalles de otros trabajos','Tejas, uniones, canalones y humedades fotografiados durante nuestras intervenciones.',[f for f in FOTOS if f['id'] not in usados])
    return ''.join(bloques)


def galeria(slug):
    lugar,titulo,texto,fotos=CASOS[slug]
    return f'<section class="obra"><h2>{titulo} en {lugar}</h2><p>{texto}</p><div class="fotos-obra">'+''.join(foto(*f) for f in fotos)+'</div><p><a href="/guias/que-incluir-limpieza-cubierta-comunidad/">Qué incluir en una limpieza de cubierta de comunidad</a></p></section>'

def destacados(incluir_leon=False):
    tarjetas=''
    for slug,(lugar,titulo,texto,fotos) in CASOS.items():
        nombre,pie=fotos[1]
        tarjetas+=f'<a class="obra-tarjeta" href="/zonas/bizkaia/{slug}/#trabajo"><img loading="lazy" src="/assets/obras/{nombre}-small.webp" alt="{pie}"><div><small>{lugar}</small><strong>{titulo}</strong><span>Ver el trabajo</span></div></a>'
    titulo='Trabajos en Bizkaia'
    if incluir_leon:
        tarjetas+=tarjeta_leon()
        titulo='Trabajos de canalones y cubiertas'
    return '<section class="wrap archivo-obras"><h2>'+titulo+'</h2><div class="fotos-obra">'+tarjetas+'</div><p><a href="/galeria/">Abrir la galería de fotografías</a></p></section>'

RUTA_LEON = '/trabajos/canalon-y-tejado-en-leon/'
TITULO_LEON = 'El recorrido del agua en una cubierta de León'

def trabajo_leon():
    fotos = [
        ('tejas-suciedad', 'Las tejas: detalle de los depósitos sobre las piezas de la cubierta.'),
        ('canalon-alero', 'El alero: encuentro entre la última fila de tejas y el canalón.'),
        ('leon-canalon-lateral', 'El tramo lateral: recorrido del canalón junto al borde del tejado.'),
        ('leon-salida-canalon', 'La salida: punto en el que el agua abandona el canalón.'),
    ]
    return '<section class="obra reportaje"><h2>Del faldón a la salida del canalón</h2><p>Las cuatro fotos pertenecen al mismo trabajo. La vista del alero permite situar el canalón respecto a la teja; el detalle de la salida permite identificar dónde termina ese recorrido. Son dos puntos distintos que conviene incluir al describir un rebose.</p><div class="fotos-obra">'+''.join(foto(*f) for f in fotos)+'</div></section><p><a href="/zonas/leon/">Consultar cobertura en la provincia de León</a></p>'

def tarjeta_leon():
    return f'<a class="obra-tarjeta" href="{RUTA_LEON}"><img loading="lazy" src="/assets/obras/leon-salida-canalon-small.webp" alt="Detalle de la salida del canalón"><div><small>Provincia de León</small><strong>{TITULO_LEON}</strong><span>Ver las cuatro fotografías</span></div></a>'

def recorrido():
    puntos = [
        ('El agua cae por el borde del canalón', 'leon-salida-canalon', 'Salida de agua de un canalón en la provincia de León.', 'Observa desde el suelo si rebosa solo junto a la bajante o a lo largo de la fachada. En este trabajo puedes seguir el recorrido hasta la salida.', RUTA_LEON, 'Ver el recorrido en León'),
        ('Hay hojas acumuladas en el tejado', 'ugao-restos-hojas', 'Restos vegetales recogidos en Ugao-Miraballes.', 'Estas hojas se recogieron durante la limpieza integral en Ugao-Miraballes. Para valorar una limpieza parecida, señala si los restos se concentran en un faldón, en el alero o en ambos.', '/zonas/bizkaia/ugao-miraballes/#trabajo', 'Ver la limpieza de Ugao-Miraballes'),
        ('Quiero identificar qué tramo hay que limpiar', 'lekeitio-alero', 'Detalle del borde de cubierta en Lekeitio.', 'Una vista general ayuda a reconocer la fachada. Una segunda foto de la esquina o de la bajante permite concretar hasta dónde llega el tramo. Así se ve en la cubierta de Lekeitio.', '/zonas/bizkaia/lekeitio/#trabajo', 'Ver el alero de Lekeitio'),
    ]
    partes=[]
    for titulo,imagen,pie,texto,url,enlace in puntos:
        partes.append(f'<details><summary>{titulo}</summary><div class="detalle-trabajo">{foto(imagen,pie)}<div><p>{texto}</p><a href="{url}">{enlace}</a></div></div></details>')
    return '<section class="wrap consulta-visual"><h2>¿Qué ves en tu tejado?</h2>'+''.join(partes)+'</section>'
