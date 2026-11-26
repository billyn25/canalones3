import os, json, re, unicodedata, shutil, math
from html import escape
from pathlib import Path
from urllib.parse import urlencode
from collections import defaultdict
from xml.etree import ElementTree as ET
from provincias import TEXTOS
from obras import trabajo_salvatierra, tarjeta_salvatierra, recorrido, album, CASOS, destacados, galeria, RUTA_LEON, TITULO_LEON, trabajo_leon, tarjeta_leon
from territorio import perfil, indice, inicial
from design import home
from blog import publicar_blog
from editorial import SERVICIOS, GUIAS
from legal import DIRECCION, ORIGEN_RUTA, PAGINAS
from estructura import pie, proceso
from contacto import TELEFONO, TELEFONO_VISIBLE
from consulta import form, presupuesto
from weather import widget

root=Path(__file__).parent.resolve()
out=root/'dist'
base='https://reparaciontejadosaleronorte.com'
provs={'bizkaia':'Bizkaia','alava':'Álava','gipuzkoa':'Gipuzkoa','cantabria':'Cantabria','burgos':'Burgos','leon':'León','palencia':'Palencia','la-rioja':'La Rioja','segovia':'Segovia'}
def slug(s):
    return re.sub('[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-')
rows=json.loads((root/'data/municipios.json').read_text())
localidades=json.loads((root/"data/localidades.json").read_text())
groups=defaultdict(list)
for r in sorted(rows,key=lambda r:slug(r['nombre'])):
    r['nucleos']=localidades[r['ine']]
    groups[r['provincia']].append(r)
    r['path']='/zonas/'+r['provincia']+'/'+slug(r['nombre'])+'/'
def link(url,s): return f'<a href="{escape(url,quote=True)}">{escape(s)}</a>'
def cards(items): return '<div class="grid">'+''.join(f'<a class="card" href="{escape(p)}"><strong>{escape(t)}</strong><p>{escape(d)}</p></a>' for p,t,d in items)+'</div>'
paths=[]
vias_locales = json.loads((root/'data/vias-locales.json').read_text())

def page(path,title,desc,body,parents=(),extra='',direcciones=None,municipio='',seo_title=None,tras_presupuesto=''):
    target=out/path.strip('/')/'index.html'
    target.parent.mkdir(parents=True,exist_ok=True)
    if path in paths:
        raise ValueError("URL municipal duplicada: "+path)
    paths.append(path)
    crumbs=[('/','Inicio'),*parents]
    trail='<nav class="crumb" aria-label="Ruta">'+ ' / '.join(link(p,t) for p,t in crumbs)+'</nav>'
    main=body if path=='/' else '<div class="wrap content">'+trail+'<h1>'+escape(title)+'</h1><p class="lead">'+escape(desc)+'</p>'+body+'</div>'
    schema=''
    if base and path!='/':
        chain=[*crumbs,(path,title)]
        items=[{'@type':'ListItem','position':i,'name':t,'item':base+p} for i,(p,t) in enumerate(chain,1)]
        structured=json.dumps({'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':items},ensure_ascii=False).replace('<','\\u003c')
        schema='<script type="application/ld+json">'+structured+'</script>'
    canonical=f'<link rel="canonical" href="{escape(base+path)}">' if base else ''
    mensaje = 'Hola, quería consultar por un trabajo de canalones o tejado.'
    if municipio:
        mensaje = f'Hola, quería consultar por un trabajo de canalones o tejado en {municipio}.'
    whatsapp = 'https://wa.me/'+TELEFONO+'?'+urlencode({'text':mensaje})
    if path not in ('/comunidades/', '/preparar-consulta/', '/aviso-legal/', '/privacidad/', '/cookies/', '/distancias/'):
        main+=presupuesto(municipio, direcciones)+'<script defer src="/assets/presupuesto.js"></script>'
    if tras_presupuesto:
        main += '<div class="wrap content">'+tras_presupuesto+'</div>'
    if seo_title is None:
        seo_title = f'{title} · Alero Norte'
    target.write_text(f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(seo_title)}</title><meta name="description" content="{escape(desc,quote=True)}">{canonical}{schema}<link rel="icon" type="image/svg+xml" href="/assets/alero-norte-icono.svg"><link rel="stylesheet" href="/assets/style.css?v=alero-2"><link rel="stylesheet" href="/assets/interiores.css?v=granate-1"><link rel="stylesheet" href="/assets/galeria.css">{extra}</head><body><a class="skip" href="#principal">Saltar al contenido</a><header class="site-header"><div class="wrap mast"><a class="brand" href="/">Alero Norte</a><nav aria-label="Principal"><a href="/servicios/">Servicios</a><a href="/zonas/">Zonas</a><a href="/guias/">Guías</a><a href="/galeria/">Trabajos</a><a href="/blog/">Blog</a></nav><div class="contactos"><a class="button" href="tel:+{TELEFONO}" aria-label="Llamar al {TELEFONO_VISIBLE}">Llamar</a><a class="button wa" href="{escape(whatsapp)}">WhatsApp</a></div></div></header><main id="principal">{main}</main>{pie(whatsapp,SERVICIOS,provs)}<script defer src="/assets/galeria.js"></script></body></html>''')
out.mkdir(exist_ok=True)
shutil.copytree(root/'assets',out/'assets',dirs_exist_ok=True)

ruta_comunidades = '/comunidades/'
titulo_comunidades = 'Limpieza de canalones y tejados para comunidades de vecinos'
portada_comunidades = '''<section class="wrap" style="margin-block:clamp(3rem,7vw,6rem);border-top:3px solid currentColor;padding-top:1.5rem;display:grid;justify-items:start;gap:clamp(1rem,2vw,1.5rem)"><h2 style="margin:0">¿Gestionas varios portales?</h2>
<p style="margin:0;max-width:65ch">Una bajante puede recoger agua de dos portales y dar problemas solo en uno. Prepara la visita con un parte que identifique la fachada, el patio y el tramo afectado.</p>
<a class="button" href="/comunidades/">Preparar un parte de comunidad</a></section>'''
parte_comunidad = '''<section><h2>Del aviso del vecino al encargo de la comunidad</h2>
<dl><dt><strong>Rebosa sobre la acera</strong></dt><dd>Indica entre qué portales cae el agua y si se ve una cortina a lo largo del borde o un chorro junto a una unión. Esa diferencia ayuda a escoger el tramo que revisar.</dd>
<dt><strong>Gotea dentro del patio</strong></dt><dd>Dos vecinos pueden estar viendo la misma bajante desde lados opuestos. Identifica el patio por el portal que da acceso y señala una referencia visible, como la ventana de la escalera.</dd>
<dt><strong>Hay una mancha en el último piso</strong></dt><dd>Anota cuándo apareció y en qué habitación. Para situarla en el edificio sirve una referencia como «junto a la fachada que da a la plaza». Guarda una foto del interior tomada tras la lluvia.</dd></dl></section>
<section><h2>Parte para el administrador de fincas</h2><p>Completa los datos que conoces. Al continuar podrás revisar el mensaje en WhatsApp y adjuntar fotografías.</p>
<form action="https://wa.me/PHONE" method="get" class="parte-comunidad"><label for="incidencia-comunidad"><strong>Datos del aviso</strong></label>
<textarea id="incidencia-comunidad" name="text" rows="11" required style="display:block;width:100%;max-width:44rem;padding:1rem;margin:0.7rem 0 1rem;font:inherit">Solicitud de visita para una comunidad
Municipio y calle: 
Portal o bloque: 
Fachada, patio o vivienda afectada: 
Qué se observa cuando llueve: 
Desde cuándo ocurre: 
Acceso al patio o cuarto de cubierta: 
Horario de contacto: </textarea><button class="button" type="submit">Revisar el parte en WhatsApp</button></form></section>
<section><h2>Qué dejar por escrito para la junta</h2><p>Si hay tres portales y el problema aparece en el central, pide que la oferta identifique qué canalones abarca, si incluye la comprobación de sus bajantes y dónde se retirarán los restos. Así la junta puede decidir entre atender la incidencia puntual o encargar el mantenimiento del conjunto.</p>
<p><a href="/guias/comparar-presupuestos-comunidad/">Comparar dos presupuestos de cubierta</a> · <a href="/galeria/">Ver fotografías de trabajos realizados</a></p></section>'''.replace('PHONE', TELEFONO)
page(ruta_comunidades,titulo_comunidades,'Atendemos a presidentes de comunidades y administradores de fincas con desplazamiento desde Bilbao. Describe el aviso y prepara la visita al edificio.',parte_comunidad)

page('/','Limpieza de canalones y tejados y reparación de cubiertas desde Bilbao','Limpieza de canalones y tejados, reparación de goteras y bajantes. Consulta los servicios, el desplazamiento desde Bilbao y la previsión de tu municipio.',(home(rows)+proceso()).replace('<section class="coverage-band"', recorrido()+portada_comunidades+'<section class="coverage-band"'),extra='<link rel="stylesheet" href="/assets/portada-trabajos.css">', seo_title='Limpieza y reparación de tejados y canalones · Alero Norte')
ejemplos = {
    'limpieza-de-canalones': ('¿Qué tramo del canalón hay que limpiar?', 'En el trabajo de Lekeitio se ve cómo el canalón sigue el borde del tejado. Si el agua rebosa, indicar en qué fachada ocurre y si pasa cerca de la bajante ayuda a situar el tramo de la visita.', '/zonas/bizkaia/lekeitio/#trabajo', 'Ver la retirada de hojas en Lekeitio'),
    'limpieza-de-tejados': ('Dónde se acumulaban los helechos en Salvatierra', 'En esta cubierta la vegetación crecía al pie del muro. La vista general y el vídeo permiten localizar esa franja respecto a la chimenea antes de mirar el detalle entre las tejas.', '/zonas/alava/agurain-salvatierra/#trabajo', 'Ver las fotos y el vídeo de Salvatierra'),
    'reparacion-de-goteras': ('El paso del agua junto a una chimenea', 'En Idiazabal fotografiamos fragmentos de teja sobre la chapa que recoge el agua de dos pendientes. Si tienes una mancha en el interior, anota cuándo aparece y en qué habitación. Esa información se puede contrastar con el recorrido del agua en la cubierta.', '/zonas/gipuzkoa/idiazabal/#trabajo', 'Ver el trabajo de goteras en Idiazabal'),
    'reparacion-de-tejados': ('Cómo se localiza una teja partida en las fotografías', 'En Comillas, una foto general permite seguir las hileras hasta el canalón. En el detalle se distingue la fisura en la teja que queda junto al remate metálico.', '/zonas/cantabria/comillas/#trabajo', 'Ver el detalle de la cubierta de Comillas'),
}
for group,title,desc,data in [('servicios','Servicios de canalones y tejados','Elige la intervención según lo que ocurre en tu cubierta.',SERVICIOS),('guias','Guías para viviendas y comunidades','Orientación para describir una incidencia, organizar el mantenimiento y comparar el alcance de una reparación.',GUIAS)]:
    path='/'+group+'/'
    page(path,title,desc,cards((path+k+'/',v['title'],v['intro']) for k,v in data.items())+(portada_comunidades if group=='servicios' else ''))
    for k,v in data.items():
        body = v['body']
        if group == 'servicios' and k in ejemplos:
            pregunta, texto, destino, etiqueta = ejemplos[k]
            body += '<section><h2>'+escape(pregunta)+'</h2><p>'+escape(texto)+'</p><p>'+link(destino, etiqueta)+'</p></section>'
        page(path+k+'/',v['title'],v['intro'],body+'<p>'+link('/preparar-consulta/','Preparar los datos para una consulta')+'</p>',[(path,title)])
import aranda
import comillas
import idiazabal
import llanes
page(llanes.RUTA,llanes.TITULO,'Trabajo de Alero Norte en Llanes (Asturias). Cinco fotografías de la cubierta de teja curva, las ventanas de tejado y el encuentro con la cumbrera.',llanes.reportaje()+perfil('33036','Llanes','Llanes'),[('/galeria/','Trabajos')])
trabajos_galeria = [
    ("Aranda de Duero · Burgos", "Estado de las tejas y vegetación entre las hileras", "aranda-de-duero/hileras", "Hileras de teja curva con restos vegetales", "/zonas/burgos/aranda-de-duero/#trabajo", "Ver 6 fotos"),
    ("Burgos", "Reparación y limpieza de tejado", "burgos/fragmentos", "Tejas partidas junto a la cumbrera", "/zonas/burgos/#trabajo", "Ver 4 fotos"),
    ("Comillas · Cantabria", "Las tejas y el canalón de una cubierta", "comillas/faldon", "Faldón de teja curva junto al canalón", "/zonas/cantabria/comillas/#trabajo", "Ver 7 fotos"),
    ("Idiazabal · Gipuzkoa", "Limpieza de tejas y reparación de goteras", "idiazabal/chimenea", "Fragmentos de teja junto a la chimenea", "/zonas/gipuzkoa/idiazabal/#trabajo", "Ver 6 fotos"),
    ("Llanes · Asturias", "Reparación y limpieza de tejado", "llanes/helechos", "Helechos junto a una ventana del tejado", "/trabajos/reparacion-limpieza-tejado-llanes/", "Ver 5 fotos"),
    ("Agurain/Salvatierra · Álava", "Limpieza de tejado y canalones", "salvatierra/helechos", "Helechos entre la cubierta y el muro", "/zonas/alava/agurain-salvatierra/#trabajo", "Ver 8 fotos y el vídeo"),
]
mosaico = '<div class="mosaico-trabajos">' + ''.join(
    f'<article><a href="{url}"><img loading="lazy" src="/assets/obras/{foto}-small.webp" alt="{alt}">'
    f'<div><p>{lugar}</p><h2>{titulo}</h2><span>{enlace}</span></div></a></article>'
    for lugar, titulo, foto, alt, url, enlace in trabajos_galeria
) + '</div>'
page('/galeria/','Trabajos reales realizados por Alero Norte','Fotografías de nuestros trabajos de limpieza y reparación en distintos pueblos de nuestra zona de cobertura. Desde Bilbao atendemos Bizkaia, Álava, Gipuzkoa, Cantabria, Burgos, León, Palencia, La Rioja y Segovia.',mosaico+album())
page(RUTA_LEON,TITULO_LEON,'Cuatro fotografías de un trabajo en la provincia de León: las tejas, el alero, el tramo lateral y la salida del canalón.',trabajo_leon(),[('/zonas/leon/','León')])
page('/preparar-consulta/','Preparar una consulta','Anota dónde está el inmueble y qué ocurre cuando llueve.',form())
def listing(items, alfabeto=False):
    if alfabeto:
        letras = {}
        for r in items:
            letras.setdefault(inicial(r["nombre"]), []).append(r)
        return indice(letras, "letra", "Municipios por inicial") + "".join(
            f'<section id="letra-{letra}"><h3>{letra}</h3>{listing(grupo)}</section>' for letra,grupo in sorted(letras.items())
        )
    return '<ul class="municipios">'+''.join(f'<li data-localidades="{escape(" | ".join(r.get("nucleos",[])),quote=True)}">{link(r["path"],r["nombre"])}</li>' for r in items)+'</ul>'
def separacion_km(origin, other):
    lat1, lat2 = map(math.radians, (origin['lat'], other['lat']))
    dl = math.radians(other['lon'] - origin['lon'])
    h = math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dl/2)**2
    return 12742 * math.asin(math.sqrt(h))

obras_municipales = [r for r in rows if r['provincia'] == 'bizkaia' and slug(r['nombre']) in CASOS]

def referencia_obra(r):
    if r["path"] == aranda.RUTA:
        return aranda.reportaje()
    if r['path'] == comillas.RUTA:
        return comillas.reportaje()
    if r['path'] == idiazabal.RUTA:
        return idiazabal.reportaje()
    if r['ine'] == '01051':
        return trabajo_salvatierra()
    if r in obras_municipales:
        return ''
    if r['provincia'] == 'leon':
        return '<aside><h2>Una cubierta de la provincia de León, en fotos</h2><p>'+link(RUTA_LEON, 'Ver el alero, el canalón lateral y la salida del agua')+'</p></aside>'
    obra = min(obras_municipales, key=lambda lugar: separacion_km(r, lugar))
    km = separacion_km(r, obra)
    if km > 35:
        ejemplos = {
            'burgos': ('/zonas/burgos/#trabajo', 'Tejas partidas junto a la cumbrera en la provincia de Burgos'),
            'cantabria': (comillas.RUTA+'#trabajo', 'Tejas y canalón en Comillas'),
            'gipuzkoa': (idiazabal.RUTA+'#trabajo', 'Limpieza de tejas y reparación de goteras en Idiazabal'),
            'alava': ('/zonas/alava/agurain-salvatierra/#trabajo', 'Limpieza de tejado y canalones en Agurain/Salvatierra'),
            'bizkaia': ('/zonas/bizkaia/lekeitio/#trabajo', 'Retirada de hojas en Lekeitio'),
        }
        ejemplo = ejemplos.get(r['provincia'])
        return '<aside><h2>Un trabajo en la provincia</h2><p>'+link(*ejemplo)+'</p></aside>' if ejemplo else ''
    nombre, trabajo, _, _ = CASOS[slug(obra['nombre'])]
    return '<aside><h2>Un trabajo cerca de '+escape(r['nombre'])+'</h2><p>'+link(obra['path']+'#trabajo', trabajo+' en '+nombre)+f' · A unos {max(1, round(km))} km en línea recta.</p></aside>'

def proximity(origin,items):
    cercanos=sorted(((separacion_km(origin,a),a) for a in items if a!=origin),key=lambda par:par[0])[:4]
    return '<p>Distancias aproximadas en línea recta desde '+escape(origin['nombre'])+'.</p><ul class="vecinos-km">'+''.join('<li>'+link(a['path'],a['nombre'])+'<strong>'+format(km,'.1f').replace('.',',')+' km</strong></li>' for km,a in cercanos)+'</ul>'
def filt(): return '<label class="filter" hidden>Buscar municipio <input type="search" placeholder="Escribe el nombre del pueblo"></label><p id="resultados" role="status"></p><script src="/assets/filter.js" defer></script>'
minutos_ruta = json.loads((root/'data/minutos-ruta.json').read_text())

def duracion_ruta(r):
    if r['metodo'] == 'local':
        return 'según el barrio'
    minutos = max(5, 5 * round(minutos_ruta[r['ine']] / 5))
    horas, resto = divmod(minutos, 60)
    return ' '.join(parte for parte in (f'{horas} h' if horas else '', f'{resto} min' if resto else '') if parte)

def resumen_rutas(items, nombres):
    elegidos=[r for r in items if r['ine'] in nombres and r['km'] is not None]
    elegidos.sort(key=lambda r:r['km'])
    filas=''.join('<tr><th scope="row">'+link(r['path'],r['nombre'])+'</th><td>'+str(r['km'])+' km<br><small>'+duracion_ruta(r)+'</small></td><td>'+(' · '.join('<span class="via">'+escape(v)+'</span>' for v in r['carreteras']) or ('Recorrido local' if r['metodo']=='local' else 'Consultar itinerario'))+'</td></tr>' for r in elegidos)
    return '<section class="rutas-zona"><h2>Trayectos desde Bilbao</h2><table><caption>Distancias y tiempos aproximados de ida</caption><thead><tr><th>Destino</th><th><span aria-label="Kilómetros y tiempo de ida">Km / tiempo</span></th><th>Vías principales</th></tr></thead><tbody>'+filas+'</tbody></table></section>'

representantes={'48044','01059','20069','39075','09059','24089','34120','26089','40194'}
for ruta,(titulo,intro,texto) in PAGINAS.items():
    page('/'+ruta+'/',titulo,intro,texto)
page('/distancias/','Cómo se calculan las distancias','Los kilómetros publicados son una referencia por carretera desde Bilbao. El enlace de cada ficha calcula la ruta desde Alameda Doctor Areilza, 31. Las distancias entre municipios cercanos se miden en línea recta.',link('https://www.ign.es/web/ign/portal/ane-datos-geograficos','IGN, 2025 · CC BY 4.0')+'<p>Rutas OSRM con datos de '+link('https://www.openstreetmap.org/copyright','© colaboradores de OpenStreetMap, ODbL')+'</p>')
provs_letras = {}
secciones_provincia = []
for clave,nombre in sorted({**provs, 'asturias':'Asturias'}.items()):
    letra = inicial(nombre)
    ancla = '' if letra in provs_letras else f' id="zona-{letra}"'
    provs_letras[letra] = clave
    if clave == 'asturias':
        cabecera = '<h2 id="asturias">Asturias</h2>'
        municipios = [{'path':llanes.RUTA,'nombre':'Llanes · Reparación y limpieza de tejado','nucleos':['Asturias']}]
    else:
        cabecera = '<h2>'+link('/zonas/'+clave+'/',nombre)+'</h2>'
        municipios = groups[clave]
    secciones_provincia.append(f'<section{ancla}>'+cabecera+listing(municipios)+'</section>')
page('/zonas/','Municipios atendidos desde Bilbao','Busca tu localidad para consultar el desplazamiento y la previsión antes de organizar una visita.','<section><h2>Desplazamientos desde Bilbao</h2><p>Salimos de '+escape(DIRECCION)+'. Organizamos las visitas por localidad. Indica el pueblo y la dirección del inmueble para confirmar el recorrido y acordar la visita.</p></section>'+resumen_rutas(rows,representantes)+indice(provs_letras, 'zona', 'Provincias por inicial')+filt()+''.join(secciones_provincia))
def introduccion_municipal(r):
    nombre = r['nombre']
    textos = {
        'vitoria-gasteiz': '¿El canalón rebosa hacia la calle o gotea por una unión? Dinos en qué fachada sucede. Si el aviso es en Abetxuko, Armentia u otra localidad de Vitoria-Gasteiz, indica también el núcleo para preparar el desplazamiento desde Bilbao.',
        'eibar': 'Si el agua cae al patio de tu comunidad en Eibar, indica desde qué viviendas se ve y si el portal da acceso al patio. Una foto general ayuda a situar la bajante antes de presupuestar la visita.',
        'deba': 'Para pedir una limpieza en Deba, señala qué tramo quieres revisar. Una foto desde la calle que incluya el alero y la bajante nos ayuda a distinguir el canalón de la fachada del que vierte hacia el patio.',
        'lerma': 'Para una visita a Lerma desde Bilbao conviene concretar el alcance en el primer mensaje. Indica si quieres limpiar todo el perímetro de la cubierta o revisar un tramo concreto donde se sale el agua.',
        'bonar': 'Si pides una visita en Boñar, envía la ubicación del inmueble y señala cuándo aparece el problema. Que el agua caiga por la fachada durante el chaparrón o que siga goteando después son dos detalles útiles para la revisión.',
        'bilbao': 'Salimos de Alameda Doctor Areilza, en Abando. Para revisar un canalón en Bilbao, dinos la calle y si el tramo afectado da a la vía pública, a un patio interior o a una terraza con acceso desde la vivienda.',
    }
    if slug(nombre) in textos:
        return textos[slug(nombre)]
    nucleos = [v for v in r['nucleos'] if slug(v) != slug(nombre)]
    destino = r.get('cabecera') or nombre
    frases = [f'Organizamos las visitas a {nombre} desde Bilbao.']
    if r['metodo'] in ('osrm', 'carretera', 'consulta') and r['km'] is not None:
        frases = [f'Desde Bilbao hasta {destino} hay aproximadamente {r["km"]} km por carretera.']
    if nucleos:
        lugares = ' o '.join(nucleos[:2])
        frases.append(f'Si el inmueble está en una localidad como {lugares}, indica su nombre al pedir la visita.')
    elif r['carreteras']:
        frases.append('El itinerario de referencia pasa por ' + ' y '.join(r['carreteras'][-2:]) + '.')
    return ' '.join(frases)


for k,title in provs.items():
    parent='/zonas/'+k+'/'
    ambito = 'la provincia de '+title
    destinos_provinciales = {
        'segovia': {'40194','40063','40076','40195'},
        'palencia': {'34120','34004','34080','34083'},
        'la-rioja': {'26089','26071','26036','26102'},
    }.get(k, {r["ine"] for r in sorted((r for r in groups[k] if r['km'] is not None),key=lambda r:r["km"])[::max(1,sum(r['km'] is not None for r in groups[k])//4)][:4]})
    page(parent,'Limpieza de canalones y tejados en '+ambito,'Atendemos los '+str(len(groups[k]))+' municipios de '+title+' con desplazamiento desde Bilbao.',('<section id="trabajo" class="obra reportaje"><h2>Reparación y limpieza de un tejado en Burgos</h2><p>En este trabajo de Alero Norte, los desperfectos se aprecian especialmente bajo la cumbrera, la línea donde se unen las dos pendientes. En la vista general se pueden seguir las hileras de teja curva hasta ese remate. Al ampliar el detalle se distinguen bordes partidos y fragmentos sueltos entre las piezas.</p><div class="fotos-obra"><figure><a data-foto href="/assets/obras/burgos/remate.webp"><img loading="lazy" src="/assets/obras/burgos/remate-small.webp" alt="Encuentro del faldón con el remate de teja y mortero."></a><figcaption>Encuentro del faldón con el remate de teja y mortero.</figcaption></figure><figure><a data-foto href="/assets/obras/burgos/faldon.webp"><img loading="lazy" src="/assets/obras/burgos/faldon-small.webp" alt="Vista general del faldón, con la cumbrera al fondo."></a><figcaption>Vista general del faldón, con la cumbrera al fondo.</figcaption></figure><figure><a data-foto href="/assets/obras/burgos/hileras.webp"><img loading="lazy" src="/assets/obras/burgos/hileras-small.webp" alt="Vista lateral de las hileras y de los huecos entre piezas."></a><figcaption>Vista lateral de las hileras y de los huecos entre piezas.</figcaption></figure><figure><a data-foto href="/assets/obras/burgos/fragmentos.webp"><img loading="lazy" src="/assets/obras/burgos/fragmentos-small.webp" alt="Fragmentos de teja y mortero bajo la línea de cumbrera."></a><figcaption>Fragmentos de teja y mortero bajo la línea de cumbrera.</figcaption></figure></div></section>'+aranda.tarjeta() if k=='burgos' else comillas.tarjeta() if k=='cantabria' else idiazabal.tarjeta() if k=='gipuzkoa' else tarjeta_salvatierra() if k=='alava' else destacados() if k=='bizkaia' else '<section class="archivo-obras"><h2>Trabajo en la provincia</h2><div class="fotos-obra">'+tarjeta_leon()+'</div></section>' if k=='leon' else '')+"<h2>"+TEXTOS[k][0]+"</h2><p>"+TEXTOS[k][1]+"</p>"+'<section><h2>Impermeabilización y cubiertas de pizarra</h2><p><a href="/servicios/impermeabilizacion-de-cubiertas/">Impermeabilización de cubiertas</a> · <a href="/servicios/reparacion-de-tejados-de-pizarra/">Reparación de tejados de pizarra</a></p></section>'+resumen_rutas(groups[k],destinos_provinciales)+filt()+listing(groups[k], alfabeto=True),[('/zonas/','Zonas')], seo_title='Limpieza de canalones y tejados en '+ambito)
    for r in groups[k]:
        n=r['nombre']; dest=str(r['lat'])+','+str(r['lon'])
        maps='https://www.google.com/maps/dir/?'+urlencode(dict(api=1,origin=ORIGEN_RUTA,destination=dest,travelmode='driving'))
        roads=' · '.join(r['carreteras'])
        desplazamiento='<section class="ruta-municipal"><h2>Desplazamiento desde Bilbao</h2>'+('<p>'+escape(str(r['km'])+' km '+{'consulta':'aprox. por carretera hasta el municipio','carretera':'aprox. por carretera desde Bilbao','osrm':'aprox. por carretera hasta el punto de referencia municipal. El recorrido hasta la dirección del inmueble puede variar','local':'· origen del desplazamiento','geodesica':'en línea recta'}.get(r['metodo'],r['metodo']))+'</p>' if r['km'] is not None else '')+('<p>Vías principales: '+escape(roads)+'</p>' if roads else '')+'<p>'+link(maps,'Ver ruta desde Alameda Doctor Areilza, 31')+' · '+link('/distancias/','Cómo se calculan los km')+'</p></section>'
        tiempo = ('Trayecto urbano según el barrio.' if r['metodo'] == 'local' else 'Tiempo aproximado de ida: '+duracion_ruta(r)+' en coche, sin tráfico en tiempo real.')
        desplazamiento = desplazamiento.replace('</p>', ' · '+tiempo+'</p>', 1)
        desplazamiento = desplazamiento.replace('</section>', '<p>Consulta el coste del desplazamiento al pedir presupuesto.</p></section>')
        lugar_aviso = next((v for v in r['nucleos'] if slug(v) != slug(n)), '')
        direccion_aviso = ('Si el aviso es en '+escape(lugar_aviso)+', indica también el núcleo al pedir presupuesto.'
                           if lugar_aviso else 'Para pedir presupuesto en '+escape(n)+', indica la altura del alero y si se accede desde la calle o desde un patio.')
        limpieza = ('<p>Retiramos las hojas y el sedimento de los tramos acordados y revisamos la embocadura de la bajante. '
                    'Si el agua sigue rebosando, comprobamos dónde se retiene antes de proponer una reparación.</p><p>'+direccion_aviso+'</p>')
        enlaces_locales=[
            ('Limpieza de canalones', 'Ver la retirada de hojas y la revisión de las salidas', '/servicios/limpieza-de-canalones/'),
            ('Limpieza de tejados en '+n, 'Consultar la limpieza de faldones y limahoyas', '/servicios/limpieza-de-tejados/'),
            ('Reparación de tejados', 'Consultar la reparación de tejas y remates', '/servicios/reparacion-de-tejados/'),
            ('Impermeabilización de cubiertas', 'Consultar la revisión de juntas, encuentros y desagües', '/servicios/impermeabilizacion-de-cubiertas/'),
            ('Reparación de tejados de pizarra', 'Consultar la sustitución de placas y la revisión de fijaciones', '/servicios/reparacion-de-tejados-de-pizarra/'),
            ('Arreglo de goteras en '+n, 'Ver cómo se localiza y repara una filtración', '/servicios/reparacion-de-goteras/'),
            ('Reparación de canalones y bajantes en '+n, 'Consultar reparaciones de juntas, soportes y tramos', '/servicios/reparacion-de-canalones-y-bajantes/'),
        ]
        consulta_gotera = '/preparar-consulta/?'+urlencode({'municipio': n+', '+title})+'#gotera'
        bloques = []
        for encabezado, etiqueta, url in enlaces_locales:
            accion = '<p>'+link(consulta_gotera, 'Pedir visita por una gotera')+'</p>' if url == '/servicios/reparacion-de-goteras/' else ''
            bloques.append('<section><h2>'+escape(encabezado)+'</h2>'+(limpieza if url == '/servicios/limpieza-de-canalones/' else '')+'<p>'+link(url, etiqueta)+'</p>'+accion+'</section>')
        servicios_locales = '<div class="servicios-locales">'+''.join(bloques)+'</div>'
        body=referencia_obra(r)+perfil(r["ine"],n,r.get("cabecera") or n)+desplazamiento+servicios_locales+widget(r)+'<h2>Municipios próximos</h2>'+proximity(r,rows)
        if k=='bizkaia' and slug(n) in CASOS:
            body='<div id="trabajo">'+galeria(slug(n))+'</div>'+body
            notas = {
                'ugao-miraballes': '<h3>Qué abarcó la limpieza integral</h3><p>Se trabajó en el faldón de teja y en los canalones que reciben el agua de esa cubierta. La vista general sitúa el faldón y la foto de los restos recogidos documenta la retirada de material vegetal.</p><p>Para presupuestar un edificio parecido, señala si quieres incluir los tramos del patio. El perímetro que se ve desde la calle puede ser solo una parte del recorrido.</p>',
                'lekeitio': '<h3>Cómo situar el tramo afectado</h3><p>En este trabajo se retiraron hojas del tejado y del canalón. La vista longitudinal permite seguir el tramo que bordea la cubierta. El detalle del alero muestra dónde termina la teja y empieza la recogida de agua.</p><p>Si consultas por un rebose, indica si el agua cae siempre por el mismo punto o a lo largo de varios metros. Esa observación nos ayuda a delimitar qué tramo revisar al llegar.</p>',
            }
            body = body.replace('</section>', notas.get(slug(n), '') + '</section>', 1)
        localidades_visita = [v for v in r.get('nucleos', []) if slug(v) != slug(n)]
        if r['metodo'] == 'local':
            detalle_fachada = 'En una comunidad de Bilbao, identifica el portal y separa en el aviso la fachada de calle y el patio. Si solo se quiere pintar el patio, indica si entran también los techos de balcones.'
        elif localidades_visita:
            detalle_fachada = 'Si la vivienda está en '+escape(localidades_visita[0])+', indica esa localidad al pedir la visita a '+escape(n)+'. Una foto general ayuda a distinguir la pared de la vivienda de anexos o cierres que también quieras incluir.'
        elif k == 'bizkaia' and slug(n) in CASOS:
            detalle_fachada = 'Si la pintura se levanta bajo el alero, observa desde el suelo si el agua rebosa por el canalón cuando llueve. Al pedir la visita se pueden delimitar por separado la revisión de la salida y el repintado del paño afectado.'
        else:
            detalle_fachada = 'Para preparar la visita desde Bilbao, indica qué lado del edificio necesita atención. Si falta mortero alrededor de una ventana, aclara si quieres reparar solo el borde o igualar después el color de toda la pared.'
        body += ('<section><h2>Pintura y albañilería de fachadas en '+escape(n)+'</h2><p>'+detalle_fachada+'</p><p>'
                 +link('/servicios/pintura-de-fachadas/', 'Pintura exterior')+' · '+link('/servicios/albanileria-de-fachadas/', 'Reparación de revestimientos y remates')+'</p></section>')
        referencias = vias_locales.get(r['ine'], {})
        barrios = referencias.get('barrios', [])
        vias = referencias.get('vias', [])
        if barrios or vias:
            cobertura = '<section><h2>¿En qué zona de '+escape(n)+' necesitas la visita?</h2>'
            if barrios:
                cobertura += '<p>Barrios de referencia: '+escape(' · '.join(barrios[:4]))+'.</p>'
            if vias:
                cobertura += '<p>Calles de referencia: '+escape(' · '.join(vias[:3]))+'.</p>'
            body += cobertura+'<p>'+link('#presupuesto', 'Indicar mi calle o barrio')+'</p></section>'
        if localidades_visita:
            opciones = ''.join('<option value="'+escape(v+', '+n+', '+title, quote=True)+'">'+escape(v)+'</option>' for v in localidades_visita)
            body += ('<section id="localidades"><h2>Localidades de '+escape(n)+'</h2>'
                     '<form action="/preparar-consulta/" method="get"><label for="localidad-visita">¿Dónde está el inmueble?</label> '
                     '<select id="localidad-visita" name="municipio"><option value="'+escape(n+', '+title, quote=True)+'">'+escape(n)+'</option>'+opciones+'</select> '
                     '<button class="button" type="submit">Preparar la visita</button></form></section>')
        body+='<p>'+link(ruta_comunidades,'Preparar un aviso de comunidad o administrador de fincas')+'</p>'
        body+='<p>'+link('/preparar-consulta/?'+urlencode({'municipio':n+', '+title}),'Preparar una consulta para '+n)+'</p>'
        caso=CASOS.get(slug(n)) if k=='bizkaia' else None
        descripcion=(caso[1]+' en '+n+'. Fotografías del trabajo y contacto para una visita.') if caso else introduccion_municipal(r)
        page(r['path'],'Limpieza de canalones, limpieza y reparación de tejados en '+n,descripcion,body,[('/zonas/','Zonas'),(parent,title)],'<link rel="stylesheet" href="/assets/weather.css"><script defer src="/assets/weather.js"></script>', direcciones=vias_locales.get(r['ine'], {}), municipio=n, seo_title='Limpieza de tejados y canalones en '+n)
publicar_blog(page, groups, provs)
if base:
    tree=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for p in paths: ET.SubElement(ET.SubElement(tree,'url'),'loc').text=base+p
    ET.ElementTree(tree).write(out/'sitemap.xml',encoding='utf-8',xml_declaration=True)
(out/'robots.txt').write_text('User-agent: *\nAllow: /\n'+('Sitemap: '+base+'/sitemap.xml\n' if base else ''))
print(len(paths),'páginas')
