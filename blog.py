"""Artículos originales de Alero Norte, ordenados para la portada del blog."""
from html import escape

ARTICULOS = [
{
    "slug": "malla-canalon-hojas",
    "title": "¿Merece la pena una malla si caen hojas en el canalón?",
    "intro": "Antes de pedir una malla, mira qué deja el árbol en el patio: hojas anchas, agujas o semillas. La respuesta cambia las preguntas que conviene hacer al instalador.",
    "img": "lekeitio-borde-tejado",
    "miniatura": "lekeitio-alero-small.webp",
    "alt": "Borde del tejado en el trabajo de Lekeitio",
    "body": "<h2>Piensa en lo que cae y en dónde va a parar</h2><p>Una hoja ancha puede quedarse encima de la rejilla; los restos finos pueden atravesar sus huecos. Si el agua ya rebosa, interesa localizar primero el tramo donde ocurre. Colocar una protección sobre una salida que ya está obstruida dejaría el problema debajo.</p><h2>La pregunta que suele olvidarse</h2><p>¿Cómo podrá el técnico revisar la embocadura una vez instalada la malla? Pide que te enseñen en el presupuesto qué tramo se desmonta, cómo se accede a la salida y si la siguiente limpieza incluye levantar y recolocar la protección. Una solución razonable para una fachada con un solo árbol puede ser poco práctica en un patio con varios aleros a distintas alturas.</p><h2>Cómo decidir después del primer otoño</h2><p>Guarda la fecha de instalación y pide en la siguiente revisión una foto de lo acumulado encima y debajo de la malla. Anota también si volvió a rebosar y en qué punto. Con esa pequeña comparación podrás decidir si mantener la protección, modificar un tramo o ajustar el calendario de limpieza.</p>"
},
{
    "slug": "parte-revision-tejado-comunidad",
    "title": "Qué guardar en el parte de revisión del tejado de una comunidad",
    "intro": "Una factura acredita un gasto. Para que el siguiente administrador sepa qué se revisó y qué quedó pendiente, hace falta una nota que pueda entender meses después.",
    "img": "burgos/hileras",
    "alt": "Hileras de tejas en una cubierta de la provincia de Burgos",
    "body": "<h2>Empieza por el alcance de la visita</h2><p>«Revisión de cubierta» dice poco cuando hay dos portales, un patio y un garaje independiente. Pide que el parte identifique la fecha, el edificio, los paños que se pudieron revisar y las zonas que quedaron pendientes de acceso. Si hubo fotografías, ponles el mismo nombre que al tramo correspondiente.</p><h2>Una anotación que sirva en la próxima junta</h2><p>Ejemplo de registro: «Portal B, canalón del patio. Se retiraron hojas de la salida. Quedó pendiente observar la junta situada sobre la ventana del primero durante el próximo episodio de lluvia». Es un ejemplo de redacción. Contiene tres datos que se pueden recuperar más tarde: lugar, actuación y comprobación pendiente.</p><h2>Cierra el aviso cuando haya una comprobación</h2><p>Una columna para la fecha y otra para el resultado bastan. Si el vecino informa de que volvió a gotear, añade cuándo y dónde; si nadie ha podido comprobarlo, deja la casilla pendiente. Al cambiar de administrador, entrega el último parte junto al croquis de los portales. Así la siguiente visita empieza con la historia de ese punto concreto.</p>"
},
    {
        "slug": "tejas-de-distinto-color",
        "title": "¿Por qué hay tejas de distinto color en un mismo tejado?",
        "intro": "En la cubierta de Comillas se alternan tonos naranjas y oscuros. Al mirar de cerca, el detalle que merece atención es una grieta que atraviesa una pieza.",
        "img": "comillas/fisura",
        "alt": "Teja fisurada junto a otra de tono anaranjado en Comillas",
        "body": "<h2>Dos cosas distintas en una misma foto</h2><p>En una vista general, el cambio de color llama enseguida la atención. Puede haber piezas de distintas partidas o con distinta exposición. El color por sí solo dice poco sobre la edad de una teja y tampoco permite fechar una reparación. En la imagen de Comillas sí hay algo que se puede señalar con precisión: la línea de fractura y el borde del fragmento que sigue apoyado sobre la hilera.</p><h2>Qué guardar si se sustituyen algunas piezas</h2><p>Si te quedan tejas de repuesto después de una obra, conserva la referencia del modelo o una foto de la caja junto a la factura. Dos tejas de un naranja casi idéntico pueden tener una curvatura y una longitud diferentes. Esa información le sirve al profesional que años después tenga que buscar una pieza compatible.</p><p>Para el archivo de la vivienda, una foto general que sitúe el paño y otra de la zona intervenida cuentan más que una imagen aislada de una teja nueva. Así, cuando cambie el color con el tiempo, seguirá quedando constancia de dónde se trabajó.</p>"
    },
    {
        "slug": "plano-de-bajantes-comunidad",
        "title": "Cómo dibujar un plano de bajantes para tu comunidad",
        "intro": "Un croquis de una página ayuda a que vecinos, administrador y técnico se entiendan cuando uno habla del portal y otro del patio.",
        "img": "comillas/alero",
        "alt": "Vista del alero y el borde de la cubierta en Comillas",
        "body": "<h2>Empieza por la puerta del portal</h2><p>Basta un rectángulo que represente el edificio visto desde arriba. Marca la entrada, escribe el nombre de la calle en ese lado y sitúa los patios. Después añade las bajantes visibles desde zonas comunes. Si una desaparece tras un cerramiento, termina ahí el dibujo y deja pendiente su recorrido.</p><h2>Un ejemplo que evita dos visitas a portales distintos</h2><p>Imagina una finca con dos entradas y un patio compartido. El aviso «gotea el tubo de la izquierda» cambia de sentido según quién mire. En el croquis puedes escribir «B1: fachada de calle, junto al portal 2» y «B2: patio, esquina del cuarto de contadores». Cuando llame otro vecino, el administrador podrá preguntarle si se refiere a B1, a B2 o a otro punto.</p><h2>Qué conservar con el dibujo</h2><p>Añade la fecha y una foto tomada desde una zona común por cada referencia. Anota qué zonas quedaron sin identificar. Guarda el plano con la documentación de la finca y actualízalo si se desvía una bajante o se cierra un patio. El próximo aviso podrá empezar con dos datos sencillos: el punto del plano y lo que se ha observado allí.</p>"
    },
    {
        "slug": "segunda-residencia-despues-de-llover",
        "title": "Qué mirar en una segunda residencia después de varias semanas de lluvia",
        "intro": "En una casa que pasa días cerrada es difícil saber cuándo apareció una marca. Una visita ordenada deja una referencia para la siguiente.",
        "img": "llanes/ventanas",
        "alt": "Ventanas de cubierta entre las tejas en Llanes",
        "body": "<h2>Repite el mismo recorrido al llegar</h2><p>Antes de mover muebles o abrir todas las ventanas, observa el techo de la última planta, los rincones de fachada y el contorno interior de las ventanas de cubierta. Apunta la fecha de la última visita en que recuerdas haber visto seca cada zona. Si desconoces cuánto tiempo lleva ahí una marca, esa observación acota el intervalo sin atribuirla a una tormenta concreta.</p><h2>Dos fotos que puedas repetir</h2><p>Escoge un punto fijo, como el marco de una puerta, y fotografía la habitación desde allí. Haz después un detalle que incluya una referencia reconocible. En la próxima visita mantén aproximadamente el ángulo y la luz. Es mucho más fácil comparar el borde de una marca con la esquina de una ventana que comparar dos primeros planos sin contexto.</p><h2>Si otra persona abre la casa por ti</h2><p>Déjale una nota concreta: «Desde la puerta del dormitorio, mira la esquina que da al jardín». Pídele fecha y foto si observa un cambio. Desde el suelo también puede señalar si el agua cae junto al porche o al otro lado de la casa. Con esa descripción podrás organizar el acceso y explicar qué se vio, incluso si el día de la visita técnica ya no llueve.</p>"
    },
    {
        "slug": "leer-una-foto-de-limahoya",
        "title": "Cómo seguir el camino del agua en una foto de tejado",
        "intro": "En Idiazabal, una franja metálica pasa junto a la chimenea. Seguirla con la vista ayuda a entender por qué los restos se reúnen en ese punto.",
        "img": "idiazabal/chimenea",
        "alt": "Fragmentos de teja sobre la limahoya junto a la chimenea en Idiazabal",
        "body": "<h2>Busca primero la línea baja</h2><p>Dos pendientes pueden bajar una hacia otra. La línea donde se encuentran recoge el agua de ambos lados y se llama limahoya. En la fotografía de Idiazabal se distingue por la chapa clara entre dos grupos de tejas. La chimenea sirve de referencia para situar ese tramo en el conjunto.</p><h2>Lee la foto de arriba abajo</h2><p>Empieza por una hilera alta y sigue la pendiente hasta la chapa. Repite el recorrido desde el paño opuesto. Ahora fíjate en los trozos de teja apoyados sobre el metal: la imagen permite ver dónde han quedado y cómo ocupan parte del paso. Para saber si el agua llega bien al alero haría falta ver también la continuación de ese canal, que queda fuera del encuadre.</p><h2>Qué pregunta deja abierta la imagen</h2><p>La foto muestra restos y su posición. Por sí sola no permite identificar por dónde entra agua en una vivienda. Si guardas fotografías de una intervención, conserva tanto este detalle como una vista amplia del encuentro. Juntas permiten volver al mismo punto y entender qué parte de la cubierta se estaba examinando.</p>"
    }
]


def publicar_blog(page):
    base = '/blog/'
    estilo = '<link rel="stylesheet" href="/assets/blog.css">'
    tarjetas = []
    for articulo in ARTICULOS:
        ruta = base + articulo['slug'] + '/'
        titulo = escape(articulo['title'])
        foto = '/assets/obras/' + articulo['img']
        miniatura = '/assets/obras/' + articulo.get('miniatura', articulo['img'] + '-small.webp')
        tarjetas.append(f'<article><a href="{ruta}"><img src="{miniatura}" alt="" loading="lazy"><h2>{titulo}</h2></a><p>{escape(articulo["intro"])}</p></article>')
        texto = (f'<article class="lectura-blog"><p class="firma-blog">Alero Norte · <time datetime="2026-11-26">26 de noviembre de 2026</time></p>'
                 f'<figure><img src="{foto}.webp" alt="{escape(articulo["alt"])}"><figcaption>{escape(articulo["alt"])}</figcaption></figure>'
                 + articulo['body'] + '<p><a href="/blog/">Volver al blog</a></p></article>')
        page(ruta, articulo['title'], articulo['intro'], texto, [(base, 'Blog')], extra=estilo)
    page(base, 'Blog de tejados y canalones', 'Fotografías comentadas y consejos para quienes cuidan una vivienda o administran una comunidad.', '<div class="indice-blog">'+''.join(tarjetas)+'</div>', extra=estilo)
