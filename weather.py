"""AEMET municipal forecast, loaded only when requested."""
import re
import json
from pathlib import Path

AEMET=json.loads((Path(__file__).parent/"data/aemet.json").read_text())
from html import escape


def widget(row):
    name = escape(row["nombre"])
    code = str(row["ine"]).zfill(5)
    if not re.fullmatch(r"\d{5}", code):
        raise ValueError("Código INE no válido")
    base = "https://www.aemet.es/es/eltiempo/prediccion/municipios"
    ident = AEMET.get(code)
    if not ident:
        return f'<section class="weather-box"><h2>El tiempo en {name}</h2><a href="{base}">Buscar la previsión municipal en AEMET</a></section>'
    estacion = name
    return f'''<section class="weather-box" aria-labelledby="prevision-local">
<h2 id="prevision-local">El tiempo en {name}</h2>
<p>Consulta las rachas previstas durante la visita y si se esperan lluvias o tormentas. Una noche de helada o una lluvia reciente pueden dejar la cubierta húmeda o con hielo aunque ya luzca el sol. El equipo comprueba el estado del tejado y el acceso antes de empezar.</p>
<p><a href="{base}/{ident}">Ver previsión en AEMET</a></p>
<div class="prevision-dias" data-diaria="{code}" aria-live="polite"></div>
<details class="weather-disclosure" data-codigo="{code if code in AEMET else '48036'}">
<summary>Tiempo por horas y avisos en {estacion}</summary>
<div class="weather-output" aria-live="polite"></div>
</details>
<noscript><a href="{base}/horas/{ident}">Consultar la previsión en AEMET</a></noscript><p><a href="/guias/tiempo-y-acceso-para-limpiar-canalones/">Qué tener en cuenta para elegir el día de la limpieza</a></p>
</section>'''
