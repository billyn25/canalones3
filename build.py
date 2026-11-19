import os, json, re, unicodedata, shutil, math
from html import escape
from pathlib import Path
from urllib.parse import urlencode
from collections import defaultdict
from xml.etree import ElementTree as ET
from provincias import TEXTOS
from obras import CASOS, destacados, galeria
from design import home
from editorial import SERVICIOS, GUIAS
from estructura import pie, proceso
from contacto import TELEFONO, TELEFONO_VISIBLE
from consulta import form
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
    mensaje = 'Hola, quería consultar por un trabajo de canalones o tejado.'
    if path.count('/') == 4 and path.startswith('/zonas/'):
        municipio = title.removeprefix('Limpieza de canalones y tejados en ')
        mensaje = f'Hola, quería consultar por un trabajo de canalones o tejado en {municipio}.'
    whatsapp = 'https://wa.me/'+TELEFONO+'?'+urlencode({'text':mensaje})
    target.write_text(f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} · Alero Norte</title><meta name="description" content="{escape(desc,quote=True)}">{canonical}{schema}<link rel="icon" href="/assets/simbolo.svg"><link rel="stylesheet" href="/assets/style.css"><link rel="stylesheet" href="/assets/interiores.css">{extra}</head><body><a class="skip" href="#principal">Saltar al contenido</a><header class="site-header"><div class="wrap mast"><a class="brand" href="/">Alero Norte</a><nav aria-label="Principal"><a href="/servicios/">Servicios</a><a href="/zonas/">Zonas</a><a href="/guias/">Guías</a></nav><div class="contactos"><a class="button" href="tel:+{TELEFONO}" aria-label="Llamar al {TELEFONO_VISIBLE}">Llamar</a><a class="button wa" href="{escape(whatsapp)}">WhatsApp</a></div></div></header><main id="principal">{main}</main>{pie(whatsapp,SERVICIOS,provs)}</body></html>''')
out.mkdir(exist_ok=True)
shutil.copytree(root/'assets',out/'assets',dirs_exist_ok=True)
page('/','Limpieza de canalones y tejados desde Bilbao','Limpieza de canalones y tejados, reparación de goteras y bajantes. Consulta los servicios, el desplazamiento desde Bilbao y la previsión de tu municipio.',(home()+proceso()).replace('<section class="coverage-band"', destacados()+'<section class="coverage-band"'))
for group,title,desc,data in [('servicios','Servicios de canalones y tejados','Elige la intervención según lo que ocurre en tu cubierta.',SERVICIOS),('guias','Guías para viviendas y comunidades','Orientación para describir una incidencia, organizar el mantenimiento y comparar el alcance de una reparación.',GUIAS)]:
    path='/'+group+'/'
    page(path,title,desc,cards((path+k+'/',v['title'],v['intro']) for k,v in data.items()))
    for k,v in data.items(): page(path+k+'/',v['title'],v['intro'],v['body']+'<p>'+link('/preparar-consulta/','Preparar los datos para una consulta')+'</p>',[(path,title)])
page('/preparar-consulta/','Preparar una consulta','Anota dónde está el inmueble y qué ocurre cuando llueve.',form())
def listing(items):
    return '<ul class="municipios">'+''.join(f'<li data-localidades="{escape(" | ".join(r.get("nucleos",[])),quote=True)}">{link(r["path"],r["nombre"])}</li>' for r in items)+'</ul>'
def proximity(origin,items):
    def separation(other):
        lat1,lat2=map(math.radians,[origin['lat'],other['lat']])
        dl=math.radians(other['lon']-origin['lon'])
        h=math.sin((lat2-lat1)/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dl/2)**2
        return round(12742*math.asin(math.sqrt(h)))
    return '<p>Distancias aproximadas en línea recta entre puntos de referencia municipales.</p><ul>'+''.join('<li>'+link(a['path'],a['nombre'])+' · '+str(separation(a))+' km</li>' for a in items)+'</ul>'
def filt(): return '<label class="filter" hidden>Buscar municipio <input type="search" placeholder="Escribe el nombre del pueblo"></label><p id="resultados" role="status"></p><script src="/assets/filter.js" defer></script>'
page('/zonas/','Municipios atendidos desde Bilbao','Busca tu localidad para consultar el desplazamiento y la previsión antes de organizar una visita.',filt()+''.join('<section><h2>'+link('/zonas/'+k+'/',v)+'</h2>'+listing(groups[k])+'</section>' for k,v in provs.items()))
for k,title in provs.items():
    parent='/zonas/'+k+'/'
    page(parent,'Limpieza de canalones y tejados en '+title,'Directorio de los '+str(len(groups[k]))+' municipios de '+title+' con desplazamiento desde Bilbao.',(destacados() if k=='bizkaia' else '')+"<h2>"+TEXTOS[k][0]+"</h2><p>"+TEXTOS[k][1]+"</p>"+filt()+listing(groups[k]),[('/zonas/','Zonas')])
    for r in groups[k]:
        n=r['nombre']; dest=str(r['lat'])+','+str(r['lon'])
        maps='https://www.google.com/maps/dir/?'+urlencode(dict(api=1,origin='43.264219,-2.923459',destination=dest,travelmode='driving'))
        roads=' · '.join(r['carreteras'])
        near=sorted((a for a in groups[k] if a!=r),key=lambda a:(a['lat']-r['lat'])**2+((a['lon']-r['lon'])*math.cos(math.radians(r['lat'])))**2)[:4]
        desplazamiento='<section><h2>Desplazamiento desde Bilbao</h2>'+('<p>'+escape(str(r['km'])+' km '+{'osrm':'aprox. por carretera hasta el punto de referencia municipal','local':'· origen del desplazamiento','geodesica':'en línea recta'}.get(r['metodo'],r['metodo']))+'</p>' if r['km'] is not None else '')+('<p>Vías principales: '+escape(roads)+'</p>' if roads else '')+'<p>'+link(maps,'Ver itinerario por carretera hasta '+n)+'</p></section>'
        body='<section><h2>¿Qué ocurre en el inmueble?</h2>'+cards([('/servicios/limpieza-de-canalones/','El agua rebosa por el alero','Limpieza del canalón y revisión de la salida a la bajante.'),('/servicios/reparacion-de-goteras/','Hay una mancha interior','Localización de la entrada de agua y revisión de encuentros.'),('/servicios/limpieza-de-tejados/','Se acumulan restos en el tejado','Revisión de faldones, limahoyas y puntos de evacuación.')])+'</section><p>'+link('/preparar-consulta/?'+urlencode({'municipio':n+', '+title}),'Preparar presupuesto en '+n)+'</p>'+desplazamiento+widget(r)+'<h2>Municipios próximos</h2>'+proximity(r,near)
        if k=='bizkaia' and slug(n) in CASOS:
            body='<div id="trabajo">'+galeria(slug(n))+'</div>'+body
        if r.get('nucleos'):
            body+='<section><h2>Localidades del municipio</h2><p>Indica la localidad al preparar la visita. El kilometraje de referencia puede variar hasta el inmueble.</p><ul class="municipios">'+''.join('<li>'+escape(v)+'</li>' for v in r['nucleos'])+'</ul></section>'
        cab=r.get('cabecera') if r.get('cabecera')!=n else None
        if cab:
            body=body.replace('<h2>Desplazamiento desde Bilbao</h2>','<h2>Desplazamiento desde Bilbao</h2><p>La capital municipal es '+escape(cab)+'. Si la vivienda está en otro núcleo de '+escape(n)+', indica el barrio o la pedanía para concretar el último tramo.</p>')
        body+='<p><small>Capitales municipales y cartografía de referencia: '+link('https://www.ign.es/web/ign/portal/ane-datos-geograficos','IGN, 2025 · CC BY 4.0')+'. Rutas OSRM con datos de '+link('https://www.openstreetmap.org/copyright','© colaboradores de OpenStreetMap, ODbL')+'.</small></p>'
        body+='<p>'+link('/preparar-consulta/?'+urlencode({'municipio':n+', '+title}),'Preparar una consulta para '+n)+'</p>'
        page(r['path'],'Limpieza de canalones y tejados en '+n,'Goteras, bajantes y mantenimiento de cubiertas en '+n+' ('+title+'). Consulta el trayecto desde Bilbao y el tiempo previsto para organizar la visita.',body,[('/zonas/','Zonas'),(parent,title)],'<link rel="stylesheet" href="/assets/weather.css"><script defer src="/assets/weather.js"></script>')
if base:
    tree=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for p in paths: ET.SubElement(ET.SubElement(tree,'url'),'loc').text=base+p
    ET.ElementTree(tree).write(out/'sitemap.xml',encoding='utf-8',xml_declaration=True)
(out/'robots.txt').write_text('User-agent: *\nAllow: /\n'+('Sitemap: '+base+'/sitemap.xml\n' if base else ''))
print(len(paths),'páginas')
