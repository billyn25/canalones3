import os, json, re, unicodedata, shutil, math
from html import escape
from pathlib import Path
from urllib.parse import urlencode
from collections import defaultdict
from xml.etree import ElementTree as ET
from provincias import TEXTOS
from obras import recorrido, album, CASOS, destacados, galeria, RUTA_LEON, TITULO_LEON, trabajo_leon, tarjeta_leon
from design import home
from editorial import SERVICIOS, GUIAS
from legal import DIRECCION, ORIGEN_RUTA, PAGINAS
from estructura import pie, proceso
from contacto import TELEFONO, TELEFONO_VISIBLE
from consulta import form, presupuesto
from weather import widget

root=Path(__file__).parent.resolve()
out=root/'dist'
base=(os.getenv('SITE_URL') or os.getenv('URL') or '').rstrip('/')
provs={'bizkaia':'Bizkaia','alava':'Álava','gipuzkoa':'Gipuzkoa','cantabria':'Cantabria','burgos':'Burgos','leon':'León'}
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
def page(path,title,desc,body,parents=(),extra=''):
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
    municipio = ''
    mensaje = 'Hola, quería consultar por un trabajo de canalones o tejado.'
    if path.count('/') == 4 and path.startswith('/zonas/'):
        municipio = title.removeprefix('Limpieza de canalones en ')
        mensaje = f'Hola, quería consultar por un trabajo de canalones o tejado en {municipio}.'
    whatsapp = 'https://wa.me/'+TELEFONO+'?'+urlencode({'text':mensaje})
    if path not in ('/preparar-consulta/', '/aviso-legal/', '/privacidad/', '/cookies/', '/distancias/'):
        main+=presupuesto(municipio)+'<script defer src="/assets/presupuesto.js"></script>'
    target.write_text(f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} · Alero Norte</title><meta name="description" content="{escape(desc,quote=True)}">{canonical}{schema}<link rel="icon" type="image/svg+xml" href="/assets/alero-norte-icono.svg"><link rel="stylesheet" href="/assets/style.css?v=alero-2"><link rel="stylesheet" href="/assets/interiores.css?v=granate-1"><link rel="stylesheet" href="/assets/galeria.css">{extra}</head><body><a class="skip" href="#principal">Saltar al contenido</a><header class="site-header"><div class="wrap mast"><a class="brand" href="/">Alero Norte</a><nav aria-label="Principal"><a href="/servicios/">Servicios</a><a href="/zonas/">Zonas</a><a href="/guias/">Guías</a><a href="/galeria/">Fotos</a></nav><div class="contactos"><a class="button" href="tel:+{TELEFONO}" aria-label="Llamar al {TELEFONO_VISIBLE}">Llamar</a><a class="button wa" href="{escape(whatsapp)}">WhatsApp</a></div></div></header><main id="principal">{main}</main>{pie(whatsapp,SERVICIOS,provs)}<script defer src="/assets/galeria.js"></script></body></html>''')
out.mkdir(exist_ok=True)
shutil.copytree(root/'assets',out/'assets',dirs_exist_ok=True)
page('/','Limpieza de canalones y tejados desde Bilbao','Limpieza de canalones y tejados, reparación de goteras y bajantes. Consulta los servicios, el desplazamiento desde Bilbao y la previsión de tu municipio.',(home(rows)+proceso()).replace('<section class="coverage-band"', recorrido()+destacados(incluir_leon=True)+'<section class="coverage-band"'))
for group,title,desc,data in [('servicios','Servicios de canalones y tejados','Elige la intervención según lo que ocurre en tu cubierta.',SERVICIOS),('guias','Guías para viviendas y comunidades','Orientación para describir una incidencia, organizar el mantenimiento y comparar el alcance de una reparación.',GUIAS)]:
    path='/'+group+'/'
    page(path,title,desc,cards((path+k+'/',v['title'],v['intro']) for k,v in data.items()))
    for k,v in data.items(): page(path+k+'/',v['title'],v['intro'],v['body']+'<p>'+link('/preparar-consulta/','Preparar los datos para una consulta')+'</p>',[(path,title)])
page('/galeria/','Trabajos reales realizados por Alero Norte','Fotografías de nuestros trabajos de limpieza y reparación en distintos pueblos de nuestra zona de cobertura. Desde Bilbao atendemos Bizkaia, Álava, Gipuzkoa, Cantabria, Burgos y León.',album())
page(RUTA_LEON,TITULO_LEON,'Cuatro fotografías de un trabajo en la provincia de León: las tejas, el alero, el tramo lateral y la salida del canalón.',trabajo_leon(),[('/zonas/leon/','León')])
page('/preparar-consulta/','Preparar una consulta','Anota dónde está el inmueble y qué ocurre cuando llueve.',form())
def listing(items):
    return '<ul class="municipios">'+''.join(f'<li data-localidades="{escape(" | ".join(r.get("nucleos",[])),quote=True)}">{link(r["path"],r["nombre"])}</li>' for r in items)+'</ul>'
def proximity(origin,items):
    def separation(other):
        lat1,lat2=map(math.radians,[origin['lat'],other['lat']])
        dl=math.radians(other['lon']-origin['lon'])
        h=math.sin((lat2-lat1)/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dl/2)**2
        return 12742*math.asin(math.sqrt(h))
    cercanos=sorted(((separation(a),a) for a in items if a!=origin),key=lambda par:par[0])[:4]
    return '<p>Distancias aproximadas en línea recta desde '+escape(origin['nombre'])+'.</p><ul class="vecinos-km">'+''.join('<li>'+link(a['path'],a['nombre'])+'<strong>'+format(km,'.1f').replace('.',',')+' km</strong></li>' for km,a in cercanos)+'</ul>'
def filt(): return '<label class="filter" hidden>Buscar municipio <input type="search" placeholder="Escribe el nombre del pueblo"></label><p id="resultados" role="status"></p><script src="/assets/filter.js" defer></script>'
def resumen_rutas(items, nombres):
    elegidos=[r for r in items if r['ine'] in nombres]
    elegidos.sort(key=lambda r:r['km'])
    filas=''.join('<tr><th scope="row">'+link(r['path'],r['nombre'])+'</th><td>'+str(r['km'])+' km</td><td>'+(' · '.join('<span class="via">'+escape(v)+'</span>' for v in r['carreteras']) or 'Recorrido local')+'</td></tr>' for r in elegidos)
    return '<section class="rutas-zona"><h2>Trayectos desde Bilbao</h2><table><caption>Distancias aproximadas por carretera</caption><thead><tr><th>Destino</th><th>Distancia</th><th>Vías principales</th></tr></thead><tbody>'+filas+'</tbody></table></section>'

representantes={'48044','01059','20069','39075','09059','24089'}
for ruta,(titulo,intro,texto) in PAGINAS.items():
    page('/'+ruta+'/',titulo,intro,texto)
page('/distancias/','Cómo se calculan las distancias','Los kilómetros publicados son una referencia por carretera desde Bilbao. El enlace de cada ficha calcula la ruta desde Alameda Doctor Areilza, 31. Las distancias entre municipios cercanos se miden en línea recta.',link('https://www.ign.es/web/ign/portal/ane-datos-geograficos','IGN, 2025 · CC BY 4.0')+'<p>Rutas OSRM con datos de '+link('https://www.openstreetmap.org/copyright','© colaboradores de OpenStreetMap, ODbL')+'</p>')
page('/zonas/','Municipios atendidos desde Bilbao','Busca tu localidad para consultar el desplazamiento y la previsión antes de organizar una visita.','<section><h2>Desplazamientos desde Bilbao</h2><p>Salimos de '+escape(DIRECCION)+'. Atendemos estas seis provincias por desplazamiento. Indica el pueblo y la dirección del inmueble para confirmar el recorrido y acordar la visita.</p></section>'+resumen_rutas(rows,representantes)+filt()+''.join('<section><h2>'+link('/zonas/'+k+'/',v)+'</h2>'+listing(groups[k])+'</section>' for k,v in provs.items()))
for k,title in provs.items():
    parent='/zonas/'+k+'/'
    page(parent,'Limpieza de canalones y tejados en '+title,'Directorio de los '+str(len(groups[k]))+' municipios de '+title+' con desplazamiento desde Bilbao.',(destacados() if k=='bizkaia' else '<section class="archivo-obras"><h2>Trabajo en la provincia</h2><div class="fotos-obra">'+tarjeta_leon()+'</div></section>' if k=='leon' else '')+"<h2>"+TEXTOS[k][0]+"</h2><p>"+TEXTOS[k][1]+"</p>"+resumen_rutas(groups[k],{r["ine"] for r in sorted(groups[k],key=lambda r:r["km"])[::max(1,len(groups[k])//4)][:4]})+filt()+listing(groups[k]),[('/zonas/','Zonas')])
    for r in groups[k]:
        n=r['nombre']; dest=str(r['lat'])+','+str(r['lon'])
        maps='https://www.google.com/maps/dir/?'+urlencode(dict(api=1,origin=ORIGEN_RUTA,destination=dest,travelmode='driving'))
        roads=' · '.join(r['carreteras'])
        desplazamiento='<section class="ruta-municipal"><h2>Desplazamiento desde Bilbao</h2>'+('<p>'+escape(str(r['km'])+' km '+{'osrm':'aprox. por carretera hasta el punto de referencia municipal','local':'· origen del desplazamiento','geodesica':'en línea recta'}.get(r['metodo'],r['metodo']))+'</p>' if r['km'] is not None else '')+('<p>Vías principales: '+escape(roads)+'</p>' if roads else '')+'<p>'+link(maps,'Ver ruta desde Alameda Doctor Areilza, 31')+' · '+link('/distancias/','Cómo se calculan los km')+'</p></section>'
        enlaces_locales=[
            ('Limpieza de tejados en '+n, 'Consultar la limpieza de faldones y limahoyas', '/servicios/limpieza-de-tejados/'),
            ('Arreglo de goteras en '+n, 'Ver cómo se localiza y repara una filtración', '/servicios/reparacion-de-goteras/'),
            ('Reparación de canalones y bajantes en '+n, 'Consultar reparaciones de juntas, soportes y tramos', '/servicios/reparacion-de-canalones-y-bajantes/'),
        ]
        servicios_locales='<div class="servicios-locales">'+''.join('<section><h2>'+escape(encabezado)+'</h2><p>'+link(url,etiqueta)+'</p></section>' for encabezado,etiqueta,url in enlaces_locales)+'</div>'
        body=servicios_locales+desplazamiento+widget(r)+'<h2>Municipios próximos</h2>'+proximity(r,rows)
        if k=='bizkaia' and slug(n) in CASOS:
            body='<div id="trabajo">'+galeria(slug(n))+'</div>'+body
        if r.get('nucleos'):
            body+='<section><h2>Localidades del municipio</h2><ul class="municipios">'+''.join('<li>'+escape(v)+'</li>' for v in r['nucleos'])+'</ul></section>'
        body+='<p>'+link('/preparar-consulta/?'+urlencode({'municipio':n+', '+title}),'Preparar una consulta para '+n)+'</p>'
        caso=CASOS.get(slug(n)) if k=='bizkaia' else None
        descripcion=(caso[1]+' en '+n+'. Fotografías del trabajo y contacto para una visita.') if caso else ('Servicio desde Bilbao hasta '+n+' ('+title+'). '+str(r['km'])+' km de referencia. Consulta el itinerario, las localidades atendidas y la previsión.')
        page(r['path'],'Limpieza de canalones en '+n,descripcion,body,[('/zonas/','Zonas'),(parent,title)],'<link rel="stylesheet" href="/assets/weather.css"><script defer src="/assets/weather.js"></script>')
if base:
    tree=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for p in paths: ET.SubElement(ET.SubElement(tree,'url'),'loc').text=base+p
    ET.ElementTree(tree).write(out/'sitemap.xml',encoding='utf-8',xml_declaration=True)
(out/'robots.txt').write_text('User-agent: *\nAllow: /\n'+('Sitemap: '+base+'/sitemap.xml\n' if base else ''))
print(len(paths),'páginas')
