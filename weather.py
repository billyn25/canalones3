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
        return f'<section><h2>Previsión cerca de {name}</h2><p>AEMET ofrece como referencia cercana la <a href="{base}/{AEMET["48036"]}">previsión de Galdakao</a>.</p></section>'
    return f'''<section class="weather-box" aria-labelledby="prevision-local">
<h2 id="prevision-local">El tiempo en {name}</h2>
<p>Previsión de lluvia y viento.</p>
<details hidden class="weather-disclosure" data-forecast="{base}/mostrarwidget/{ident}">
<summary>Ver previsión de AEMET para {name}</summary>
<div class="weather-output"></div>
</details>
<a href="{base}/{ident}">Ver viento, rachas y previsión completa de {name} en AEMET</a>
</section>'''
