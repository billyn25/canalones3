"""Consulta local para preparar una visita de cubiertas."""
from contacto import TELEFONO
import os
import re
from html import escape


def form():
    phone = re.sub(r'[\s()+-]', '', os.getenv('WHATSAPP_NUMBER', TELEFONO))
    if not re.fullmatch(r'[1-9]\d{8,14}', phone):
        phone = ''
    return f"""<section>
<p>Reúne los datos de la vivienda o comunidad para explicar qué ocurre y dónde se aprecia. Puedes copiar el resumen o descargarlo. Los datos se quedan en tu dispositivo hasta que decidas compartirlos.</p>
<form id="consulta" data-phone="{escape(phone)}" hidden>
<p><label>Municipio y provincia<br><input name="lugar" required maxlength="140" placeholder="Por ejemplo, Boñar, León"></label></p>
<p><label>Tipo de inmueble<br><select name="inmueble"><option>Vivienda unifamiliar</option><option>Comunidad de vecinos</option><option>Local o nave</option><option>Otro inmueble</option></select></label></p>
<p><label>Motivo de la consulta<br><select name="motivo"><option>Limpieza de canalones</option><option>Limpieza de tejado</option><option>Gotera o filtración</option><option>Reparación de canalón o bajante</option><option>Reparación de tejado</option><option>Otro motivo</option></select></label></p>
<p><label>¿Qué has observado?<br><textarea name="detalle" required rows="4" maxlength="1800" placeholder="Por ejemplo, el canalón rebosa junto al portal cuando llueve."></textarea></label></p>
<p><label>Acceso y disponibilidad (opcional)<br><textarea name="acceso" rows="2" maxlength="500" placeholder="Patio interior, número de plantas o persona que puede abrir el portal."></textarea></label></p>
<button class="button" type="submit">Crear resumen</button></form>
<noscript><p>Para preparar el resumen a mano, anota municipio, tipo de inmueble, problema observado y acceso al edificio.</p></noscript>
<section id="consulta-resultado" hidden><h2 tabindex="-1">Resumen de tu consulta</h2><p><label>Texto para compartir<br><textarea readonly rows="8"></textarea></label></p>
<button type="button" class="button" data-copy>Copiar texto</button>
<button type="button" class="button" data-save>Descargar texto</button>
<a class="button" data-share hidden target="_blank" rel="noopener noreferrer">Abrir en WhatsApp</a><p role="status"></p></section>
<script defer src="/assets/consulta.js"></script></section>"""
