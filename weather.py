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
    estacion = name if ident else "Galdakao (referencia cercana)"
    ident = ident or AEMET["48036"]
    return f'''<section class="weather-box" aria-labelledby="prevision-local">
<h2 id="prevision-local">El tiempo en {name}</h2>
<p>Consulta las rachas previstas durante la visita y si se esperan lluvias o tormentas. Una noche de helada o una lluvia reciente pueden dejar la cubierta húmeda o con hielo aunque ya luzca el sol. El equipo comprueba el estado del tejado y el acceso antes de empezar.</p>
<details hidden class="weather-disclosure" data-forecast="{base}/mostrarwidget/{ident}">
<summary>Ver previsión de AEMET para {estacion}</summary>
<div class="weather-output"></div>
</details>
<p><a href="{base}/horas/{ident}">Previsión por horas de {estacion}</a> · <a href="https://www.aemet.es/es/eltiempo/prediccion/avisos">Consultar avisos de AEMET</a></p>
<p>Compara los milímetros de lluvia previstos y las rachas durante la visita. Si hay aviso, comprueba la zona y su horario.</p>
<a href="{base}/{ident}">Previsión completa de {estacion}</a><p><a href="/guias/tiempo-y-acceso-para-limpiar-canalones/">Qué tener en cuenta para elegir el día de la limpieza</a></p>
</section>'''
