"""Landing page for Alero Norte."""

from html import escape

def home(rows):
    provinces = [
        ("Bizkaia", "bizkaia"), ("Álava", "alava"), ("Gipuzkoa", "gipuzkoa"),
        ("Cantabria", "cantabria"), ("Burgos", "burgos"), ("León", "leon"), ("Palencia", "palencia"), ("La Rioja", "la-rioja"),
    ]
    selecciones = {
        "bizkaia": ("48020","48013","48044","48057","48065","48027","48046"),
        "alava": ("01059","01036","01002","01051","01031","01047"),
        "gipuzkoa": ("20069","20045","20030","20079","20029","20071","20009"),
        "cantabria": ("39075","39087","39020","39059","39035","39079"),
        "burgos": ("09059","09219","09018","09410","09194","09056"),
        "palencia": ("34120","34004","34080","34047","34157"),
        "la-rioja": ("26089","26071","26036","26102","26011","26018"),
        "leon": ("24089","24115","24008","24021","24010","24014"),
    }
    por_codigo = {r["ine"]:r for r in rows}
    bloques=[]
    for name,slug in provinces:
        enlaces=[]
        for codigo in selecciones[slug]:
            r=por_codigo[codigo]
            assert r['provincia']==slug
            enlaces.append(f'<li><a href="{r["path"]}">{escape(r["nombre"])}</a></li>')
        bloques.append(f'<section><h3><a href="/zonas/{slug}/">{name}</a></h3><ul>{"".join(enlaces)}</ul></section>')
    area_links="".join(bloques)
    return '''<section class="portada-obra"><div class="wrap escena">
<a class="escena-foto" href="/zonas/bizkaia/lekeitio/#trabajo"><img src="/assets/obras/lekeitio-borde-tejado.webp" alt="Borde de la cubierta y alero en el trabajo de limpieza de Lekeitio" fetchpriority="high"><span>Lekeitio · Ver intervención</span></a>
<div class="escena-texto"><h1>Limpieza de canalones y tejados</h1><p>Goteras, bajantes y reparaciones de cubierta para viviendas y comunidades. Servicio desde Bilbao.</p><a href="/zonas/">Buscar mi localidad</a></div>
</div></section>
<section class="wrap home-section"><div class="section-head"><div><p class="eyebrow">Servicios</p><h2>¿Dónde está el problema?</h2></div><a class="text-link" href="/servicios/">Ver todos los servicios</a></div>
<div class="service-strip">
<a class="service-item" href="/servicios/limpieza-de-canalones/"><span class="service-icon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M5 14h28v8a7 7 0 0 1-7 7H12a7 7 0 0 1-7-7zm22 15v7h8v7m-2-26h8v6a6 6 0 0 1-6 6M9 9l4-4m4 4 4-4"/></svg></span><h3>Canalones y bajantes</h3><p>Si el agua cae por el borde o moja la fachada, conviene localizar en qué punto deja de evacuar.</p><span class="service-link">Limpieza de canalones</span></a>
<a class="service-item" href="/servicios/limpieza-de-tejados/"><span class="service-icon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="m4 32 17-23h17L22 32zm18 0h21L28 10M8 26h17M13 20h15M17 15h14M9 36h32"/></svg></span><h3>Tejados y limahoyas</h3><p>Las hojas se reúnen donde confluyen dos faldones. La limpieza debe atender también la salida hacia el alero.</p><span class="service-link">Limpieza de tejados</span></a>
<a class="service-item" href="/servicios/reparacion-de-goteras/"><span class="service-icon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="m4 26 16-17 18 16M9 27l11-11 12 11m6 0s-6 8-6 11a6 6 0 0 0 12 0c0-3-6-11-6-11zM15 30v8h9"/></svg></span><h3>Goteras y filtraciones</h3><p>Una mancha puede aparecer lejos de la entrada de agua. Importan su posición y las condiciones en que vuelve.</p><span class="service-link">Reparación de goteras</span></a>
<a class="service-item" href="/servicios/pintura-de-fachadas/"><h3>Pintura de fachadas</h3><p>Repintado de muros exteriores, patios y balcones.</p><span class="service-link">Ver pintura exterior</span></a>
<a class="service-item" href="/servicios/albanileria-de-fachadas/"><h3>Albañilería de fachadas</h3><p>Reparación de juntas, revestimientos y remates deteriorados.</p><span class="service-link">Ver reparaciones</span></a>
</div></section>
<section class="wrap home-section guide-teaser"><div><h2>Comunidades de propietarios y administradores de fincas</h2></div><div><p>¿Rebosa una bajante compartida o toca limpiar los canalones de varios portales? Cuéntanos qué fachadas dan a la calle y cuáles al patio para preparar una visita al edificio.</p><a class="text-link" href="/servicios/mantenimiento-de-tejados-para-comunidades/">Ver mantenimiento de tejados para comunidades</a></div></section>
<section class="coverage-band"><div class="wrap coverage-layout"><div><p class="eyebrow">Desplazamientos desde Bilbao</p><h2>Encuentra tu municipio.</h2><p>Consulta la cobertura por provincia y prepara la visita a tu vivienda, caserío o comunidad.</p></div><div class="pueblos-portada">''' + area_links + '''</div></div></section>
<section class="wrap home-section guide-teaser"><div><p class="eyebrow">Antes de una visita</p><h2>¿Qué ocurre cuando llueve?</h2></div><div><p>Anota si el agua rebosa durante el chaparrón, si sigue goteando después o si la humedad aparece con viento de una dirección concreta. Una foto tomada desde el suelo ayuda a situar el punto.</p><a class="text-link" href="/guias/">Leer las guías de mantenimiento</a></div></section>'''
