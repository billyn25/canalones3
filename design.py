"""Landing page for Alero Norte."""

def home():
    provinces = [
        ("Bizkaia", "bizkaia"), ("Álava", "alava"), ("Gipuzkoa", "gipuzkoa"),
        ("Cantabria", "cantabria"), ("Burgos", "burgos"), ("León", "leon"),
    ]
    area_links = "".join(
        f'<li><a href="/zonas/{slug}/">{name}</a></li>' for name, slug in provinces
    )
    return '''<section class="home-hero"><div class="wrap hero-grid">
<div class="hero-copy"><p class="eyebrow"><span class="datum"></span> Cubiertas y evacuación de lluvia</p>
<h1>Limpieza de canalones <em>y tejados.</em></h1>
<p class="hero-description">Limpieza de bajantes, reparación de goteras y mantenimiento de cubiertas para viviendas y comunidades. Nos desplazamos desde Bilbao.</p>
<div class="actions"><a class="button" href="/preparar-consulta/">Preparar mi consulta</a><a class="text-link" href="/zonas/">Consultar mi municipio</a></div></div>
<figure class="hero-figure"><div class="plate"><img width="620" height="450" fetchpriority="high" src="/assets/detalle-alero.svg" alt="Dibujo en perspectiva del borde del tejado, con tejas, canalón y bajante."></div><figcaption><span>Detalle constructivo</span> Encuentro de cubierta y canalón</figcaption></figure>
</div></section>
<section class="wrap home-section"><div class="section-head"><div><p class="eyebrow">Servicios</p><h2>¿Dónde está el problema?</h2></div><a class="text-link" href="/servicios/">Ver todos los servicios</a></div>
<div class="service-strip">
<a class="service-item" href="/servicios/limpieza-de-canalones/"><span class="service-icon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M5 14h28v8a7 7 0 0 1-7 7H12a7 7 0 0 1-7-7zm22 15v7h8v7m-2-26h8v6a6 6 0 0 1-6 6M9 9l4-4m4 4 4-4"/></svg></span><h3>Canalones y bajantes</h3><p>Si el agua cae por el borde o moja la fachada, conviene localizar en qué punto deja de evacuar.</p><span class="service-link">Limpieza de canalones</span></a>
<a class="service-item" href="/servicios/limpieza-de-tejados/"><span class="service-icon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="m4 32 17-23h17L22 32zm18 0h21L28 10M8 26h17M13 20h15M17 15h14M9 36h32"/></svg></span><h3>Tejados y limahoyas</h3><p>Las hojas se reúnen donde confluyen dos faldones. La limpieza debe atender también la salida hacia el alero.</p><span class="service-link">Limpieza de tejados</span></a>
<a class="service-item" href="/servicios/reparacion-de-goteras/"><span class="service-icon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="m4 26 16-17 18 16M9 27l11-11 12 11m6 0s-6 8-6 11a6 6 0 0 0 12 0c0-3-6-11-6-11zM15 30v8h9"/></svg></span><h3>Goteras y filtraciones</h3><p>Una mancha puede aparecer lejos de la entrada de agua. Importan su posición y las condiciones en que vuelve.</p><span class="service-link">Reparación de goteras</span></a>
</div></section>
<section class="coverage-band"><div class="wrap coverage-layout"><div><p class="eyebrow">Desplazamientos desde Bilbao</p><h2>Encuentra tu municipio.</h2><p>Consulta la cobertura por provincia y prepara la visita a tu vivienda, caserío o comunidad.</p></div><ul class="area-links">''' + area_links + '''</ul></div></section>
<section class="wrap home-section guide-teaser"><div><p class="eyebrow">Antes de una visita</p><h2>¿Qué ocurre cuando llueve?</h2></div><div><p>Anota si el agua rebosa durante el chaparrón, si sigue goteando después o si la humedad aparece con viento de una dirección concreta. Una foto tomada desde el suelo ayuda a situar el punto.</p><a class="text-link" href="/guias/">Leer las guías de mantenimiento</a></div></section>'''
