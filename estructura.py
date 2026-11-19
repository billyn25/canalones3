from html import escape
from contacto import TELEFONO, TELEFONO_VISIBLE

def pie(whatsapp, servicios, provincias):
    def columna(titulo, enlaces):
        items=''.join(f'<li><a href="{url}">{escape(nombre)}</a></li>' for url,nombre in enlaces)
        return f'<nav aria-label="{titulo} del pie"><h2>{titulo}</h2><ul>{items}</ul></nav>'
    nav=columna('Servicios', [('/servicios/'+k+'/',v['title']) for k,v in servicios.items()])
    zonas=columna('Zonas de trabajo',[('/zonas/'+k+'/',v) for k,v in provincias.items()])
    obras=columna('Trabajos y guías',[('/zonas/bizkaia/ugao-miraballes/#trabajo','Limpieza integral en Ugao-Miraballes'),('/zonas/bizkaia/lekeitio/#trabajo','Tejado y canalones en Lekeitio'),('/guias/','Guías para viviendas y comunidades')])
    return f'''<footer class="site-footer pie-profesional"><div class="wrap"><div class="pie-contacto"><div><h2>Consulta sobre tu cubierta</h2><p>Indícanos el pueblo y dónde aparece el agua. Por WhatsApp puedes adjuntar una foto del punto afectado.</p></div><div><a class="numero" href="tel:+{TELEFONO}">{TELEFONO_VISIBLE}</a><a class="pie-wa" href="{escape(whatsapp)}">Escribir por WhatsApp</a></div></div><div class="pie-directorio"><div><a class="pie-marca" href="/">Alero Norte</a><p>Limpieza y reparación de canalones y tejados. Desplazamientos desde Bilbao.</p></div>{nav}{zonas}{obras}</div></div></footer>'''

def proceso():
    return '''<section class="wrap proceso"><h2>Qué se valora antes de presupuestar</h2><dl><div><dt>La zona afectada</dt><dd>Un rebose junto a una bajante orienta la revisión hacia su embocadura. Si la humedad aparece bajo una chimenea, interesa ver el encuentro con las tejas.</dd></div><div><dt>El acceso</dt><dd>Dos canalones de igual longitud pueden requerir medios distintos. Indica las plantas del edificio y si la fachada da a la calle, a un jardín o a un patio interior.</dd></div><div><dt>El alcance</dt><dd>Conviene concretar qué tramos se limpian, dónde se retiran los residuos y si hay piezas que reparar. En comunidades ayuda identificar los portales que comparten bajante.</dd></div></dl><a href="/preparar-consulta/">Preparar los datos para mi presupuesto</a></section>'''
