"""Consulta local para preparar una visita de cubiertas."""
from contacto import TELEFONO
import os
import re
from html import escape


REBOSE = """<label>¿Cuándo rebosa el canalón? (opcional)<br><select name="rebose"><option value="">Elige si procede</option><option>También con lluvia suave</option><option>Solo con chaparrones fuertes</option><option>No lo sé</option></select></label>"""

def form():
    phone = re.sub(r'[\s()+-]', '', os.getenv('WHATSAPP_NUMBER', TELEFONO))
    if not re.fullmatch(r'[1-9]\d{8,14}', phone):
        phone = ''
    return f"""<section>
<p>Para una limpieza, indica si quieres incluir la fachada de la calle, el patio o todo el perímetro. Si hay una fuga, señala la unión o la ventana junto a la que aparece. Puedes adjuntar las fotos al abrir el chat.</p>
<p>Describe el trabajo y pulsa «Continuar en WhatsApp». Se abrirá tu consulta lista para enviarla. También puedes revisar o descargar el resumen.</p>
<form id="consulta" data-phone="{escape(phone)}" hidden>
<p><label>Municipio y provincia<br><input name="lugar" required maxlength="140" placeholder="Por ejemplo, Boñar, León"></label></p>
<p><label>Tipo de inmueble<br><select name="inmueble"><option>Vivienda unifamiliar</option><option>Comunidad de vecinos</option><option>Local o nave</option><option>Otro inmueble</option></select></label></p>
<p><label>Motivo de la consulta<br><select name="motivo"><option>Limpieza de canalones</option><option>Limpieza de tejado</option><option>Gotera o filtración</option><option>Reparación de canalón o bajante</option><option>Reparación de tejado</option><option>Pintura de fachadas</option><option>Albañilería de fachadas</option><option>Otro motivo</option></select></label></p>
<p><label>¿Qué has observado?<br><textarea name="detalle" required rows="4" maxlength="1800" placeholder="Por ejemplo, el canalón rebosa junto al portal cuando llueve."></textarea></label></p>
<p>{REBOSE}</p>
<p><label>Acceso y disponibilidad (opcional)<br><textarea name="acceso" rows="2" maxlength="500" placeholder="Patio interior, número de plantas o persona que puede abrir el portal."></textarea></label></p>
<button class="button" type="submit">{'Continuar en WhatsApp' if phone else 'Crear resumen'}</button>
{('<button type="submit" value="resumen">Ver resumen</button>' if phone else '')}</form>
<noscript><p><a href="https://wa.me/{TELEFONO}">Abrir WhatsApp para pedir presupuesto</a></p></noscript>
<section id="consulta-resultado" hidden><h2 tabindex="-1">Resumen de tu consulta</h2><p><label>Texto para compartir<br><textarea readonly rows="8"></textarea></label></p>
<button type="button" class="button" data-copy>Copiar texto</button>
<button type="button" class="button" data-save>Descargar texto</button>
<a class="button" data-share hidden target="_blank" rel="noopener noreferrer">Abrir en WhatsApp</a><p role="status"></p></section>
<script defer src="/assets/consulta.js"></script></section>"""

def presupuesto(lugar='', direcciones=None):
    campos_direccion = ''
    if lugar:
        datos = direcciones or {}
        for campo, etiqueta, clave, limite in [('barrio', 'Barrio o localidad', 'barrios', 100), ('calle', 'Calle o plaza', 'vias', 140)]:
            nombres = datos.get(clave, [])
            opciones = ''.join(f'<option value="{escape(nombre, quote=True)}"></option>' for nombre in nombres)
            lista = f' list="sugerencias-{campo}"' if opciones else ''
            campos_direccion += f'<label>{etiqueta} (opcional)<input name="{campo}"{lista} maxlength="{limite}"></label>'
            if opciones:
                campos_direccion += f'<datalist id="sugerencias-{campo}">{opciones}</datalist>'
    return f'''<section id="presupuesto" class="presupuesto"><div class="wrap presupuesto-grid"><div><h2>Pide presupuesto</h2><p>Indica qué tramos quieres incluir: el canalón de la calle, el del patio o todo el perímetro. Si además gotea una junta, señala dónde para valorar esa reparación por separado.</p></div>
<form id="solicitud-presupuesto" data-phone="{TELEFONO}" hidden>
<label>{"Municipio" if lugar else "Municipio o barrio"}<input name="lugar" value="{escape(lugar, quote=True)}" maxlength="140" required></label>
{campos_direccion}
<label>¿Qué necesitas?<textarea name="detalle" rows="3" maxlength="1500" required placeholder="Por ejemplo, limpiar el canalón de una comunidad de tres plantas."></textarea></label>
{REBOSE}
<p>Al continuar se abre WhatsApp con tu consulta preparada. Tú decides cuándo enviarla. <a href="/privacidad/">Privacidad</a></p>
<button class="button" type="submit">Continuar en WhatsApp</button></form>
<noscript><a href="https://wa.me/{TELEFONO}">Pedir presupuesto por WhatsApp</a></noscript></div></section>'''
