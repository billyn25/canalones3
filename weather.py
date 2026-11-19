"""AEMET municipal forecast, loaded only when requested."""
import re
import unicodedata
from html import escape


def widget(row):
    name = escape(row["nombre"])
    code = str(row["ine"]).zfill(5)
    if not re.fullmatch(r"\d{5}", code):
        raise ValueError("Código INE no válido")
    ascii_name = unicodedata.normalize("NFKD", row["nombre"]).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")
    base = "https://www.aemet.es/es/eltiempo/prediccion/municipios"
    ident = f"{slug}-id{code}"
    return f'''<section class="weather-box" aria-labelledby="prevision-local">
<h2 id="prevision-local">El tiempo en {name}</h2>
<p>Para acordar una visita, consulta la probabilidad de lluvia y el viento previstos. Una cubierta puede seguir mojada después de la lluvia. El equipo valorará el acceso y el estado del tejado antes de empezar.</p>
<details hidden class="weather-disclosure" data-forecast="{base}/mostrarwidget/{ident}">
<summary>Ver previsión de AEMET para {name}</summary>
<div class="weather-output"></div>
</details>
<a href="{base}/{ident}">Ver viento, rachas y previsión completa de {name} en AEMET</a>
</section>'''
