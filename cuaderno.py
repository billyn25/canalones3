"""Lecturas prácticas para propietarios y comunidades."""
from html import escape


def lectura(slug, titulo, intro, imagen, pie, secciones):
    partes = []
    for encabezado, *parrafos in secciones:
        partes.append(f'<h2>{escape(encabezado)}</h2>')
        partes.extend(f'<p>{escape(p)}</p>' for p in parrafos)
    return dict(slug=slug, title=titulo, intro=intro, img=imagen, alt=pie,
                body=''.join(partes))


LECTURAS = [
    lectura('comparar-presupuestos-de-retejado', 'Dos precios para retejar la misma casa: ¿qué incluye cada uno?',
        'Una oferta cuenta las tejas que va a cambiar. Otra mide un paño entero. Antes de comparar importes conviene poner ambas sobre el mismo dibujo.',
        'burgos/faldon', 'Vista del faldón de una cubierta de teja en Burgos', [
        ('Marca dónde termina la obra', 'Imagina una casa con una ampliación sobre la cocina. En la oferta A se lee «tejado principal» y en la B «cubierta de la vivienda». Rodea en una foto el tejado alto y la ampliación por separado. Pide que cada empresa marque dónde interviene y si incluye la unión entre ambos. Es una pregunta pequeña que puede explicar buena parte de la diferencia.'),
        ('Separa los gastos que aparecen una sola vez', 'Haz tres filas en una hoja: preparación del acceso, intervención en la cubierta y retirada de material. Apunta en cada casilla qué está incluido. Si la retirada figura como partida independiente, comprueba si abarca tanto bajar los escombros como llevárselos. Deja en blanco lo que falte aclarar. Asignarle un cero haría parecer más barata una oferta todavía incompleta.'),
        ('Acuerda cómo se aprobaría un imprevisto', 'Pregunta qué ocurriría si, al levantar la primera hilera, apareciera un apoyo deteriorado. Una respuesta útil concreta quién te enseñaría el hallazgo, cómo se valoraría el cambio y en qué momento decidirías. Guarda la foto marcada junto al presupuesto aceptado. Después te servirá para comprobar qué parte de la casa corresponde a la factura.')]),
    lectura('canalon-rebosa-en-una-esquina', 'El canalón rebosa siempre por la misma esquina',
        'La escena dura unos minutos y cuando llega el técnico ya ha escampado. La secuencia del rebose puede contar más que una foto del charco.',
        'comillas/alero', 'Borde de teja y alero en una vivienda de Comillas', [
        ('Qué ocurre primero', 'Desde una ventana cerrada o desde la calle, fíjate en qué punto aparece la primera caída de agua. ¿Salta por encima del borde a mitad del tramo o cae de una unión incluso antes de que el canalón parezca lleno? Si grabas unos segundos, incluye la esquina y la boca de la bajante en el mismo plano siempre que sean visibles.'),
        ('Dos avisos que suenan iguales por teléfono', 'En una casa, el agua cae sobre la puerta únicamente durante el chaparrón. En otra, sigue goteando de la misma unión después de que el resto del alero haya dejado de verter. El charco puede quedar en un sitio parecido. En la primera visita interesa seguir el recorrido hasta la salida; en la segunda también merece atención la propia unión. Ninguna de las dos observaciones basta por sí sola para decidir qué pieza cambiar.'),
        ('Qué preguntar si proponen una limpieza', 'Pide que el parte indique dónde se encontró material y hasta qué punto se pudo revisar la salida. Si el problema reaparece, compara el arranque del rebose con el vídeo anterior. Eso ayuda a decidir si toca volver al mismo punto o examinar otro tramo.')]),
    lectura('mancha-techo-despues-de-llover', 'Ha dejado de llover y la mancha del techo sigue creciendo',
        'La hora a la que aparece una marca y el sitio donde cae la primera gota son dos pistas distintas. Así puedes conservarlas para la visita.',
        'comillas/encuentros', 'Encuentro de varios paños de teja en Comillas', [
        ('Sitúa el borde de la mancha', 'Haz una fotografía de la estancia desde la puerta y otra del contorno visible. Incluye en la primera una referencia fija, como el encuentro entre dos paredes. Dos primeros planos sin orientación pueden parecer idénticos aunque correspondan a esquinas distintas. Anota cuándo empezó a llover, cuándo viste el cambio y si todavía caía agua en ese momento.'),
        ('Por qué importa la habitación de al lado', 'El punto donde el agua se hace visible puede estar separado de su entrada. Si encima hay una terraza, una chimenea o un cambio de altura, sitúalos en un croquis sencillo. Una foto de la cubierta tomada desde la calle permite al profesional relacionar el interior y el exterior. Ahórrate las flechas que señalan una teja concreta si desde tu posición solo puedes identificar el lado del edificio.'),
        ('Después de la visita', 'Guarda por separado la observación inicial y la explicación que se haya podido comprobar. Si se interviene en la cubierta, repite el encuadre tras otro episodio de lluvia. Una marca antigua puede seguir visible: lo que interesa registrar es si vuelve a humedecerse o cambia de extensión.')]),
    lectura('limpiar-tejado-antes-de-poner-placas', 'Qué revisar en el tejado antes de instalar placas solares',
        'Una vez colocados los paneles, algunas hileras quedan fuera de la vista. La coordinación empieza antes de que lleguen los dos equipos.',
        'burgos/hileras', 'Hileras de tejas cerámicas vistas en una cubierta de Burgos', [
        ('El plano que interesa al tejador', 'Pide al instalador un dibujo de la superficie prevista y de los recorridos de cable. Sobre una copia, señala dónde hubo reparaciones, por dónde se accede a la cubierta y qué canalón se limpia periódicamente. Un rectángulo dibujado sobre una fotografía es suficiente para iniciar la conversación si todos reconocen la misma vertiente.'),
        ('Una pregunta para cada empresa', 'Al profesional de cubierta pregúntale qué zonas ha podido revisar dentro de la futura huella de los paneles. Al instalador, cómo quedará el acceso a las salidas de agua y quién atenderá una incidencia situada bajo un módulo. Si hay una pieza pendiente de sustituir, conviene acordar el orden de las dos intervenciones antes de fijar fechas.'),
        ('El pequeño archivo que conviene conservar', 'Reúne las fotos anteriores al montaje, la distribución finalmente instalada y los contactos de ambas empresas. Si el diseño cambia durante la obra, guarda la versión final. Cuando alguien vuelva a revisar el tejado podrá saber qué había debajo y a quién consultar para organizar el acceso.')]),
    lectura('pedir-limpieza-canalones-patio-interior', 'Cómo preparar una limpieza de canalones en un patio interior',
        'El tramo puede verse perfectamente desde el segundo piso y tener su único acceso por otro portal. Ese detalle cambia la organización de la visita.',
        'comillas/faldon', 'Faldón de tejas junto al borde de la cubierta en Comillas', [
        ('Sigue el recorrido de las personas', 'Empieza en la puerta de calle. Anota qué portal abre al patio, si hay una segunda puerta con llave y quién puede facilitar el acceso. En una finca con locales, comprueba si el paso que parece comunitario atraviesa en realidad un almacén con horario propio. Comunica estas condiciones antes de cerrar la cita.'),
        ('Dónde acaba lo que se retira', 'Explica si debajo hay un tendedero, una terraza de uso privado o una cubierta ligera. Pregunta cómo se recogerán los restos y por dónde saldrán las bolsas. La misma longitud de canalón requiere una preparación diferente cuando la zona inferior está ocupada. Una fotografía desde un espacio común suele aclarar mejor la distribución que una lista de pisos.'),
        ('Cómo entregar el trabajo al administrador', 'Pide que se identifiquen el tramo atendido y las salidas revisadas. Si un patio quedó cerrado, que figure por su nombre. Así podrás organizar el acceso pendiente con el vecino adecuado y evitar que la siguiente convocatoria vuelva a citar a toda la comunidad.')]),
    lectura('limpieza-musgo-que-pedir', 'Musgo en las tejas: qué preguntar antes de encargar la limpieza',
        'Dos ofertas pueden usar la palabra «antimusgo» y describir actuaciones distintas. Estas preguntas ayudan a saber qué resultado estás contratando.',
        'burgos/remate', 'Detalle del remate de una cubierta con líquenes en Burgos', [
        ('Distingue la zona visible de la zona incluida', 'En una foto frontal destaca el faldón que da a la calle. El presupuesto puede incluir también el patio, o limitarse a la primera vertiente. Pide que se identifiquen los paños y los remates. Si tu preocupación es que caigan restos sobre la entrada, señala el alero concreto y pide que se tenga en cuenta al organizar la recogida.'),
        ('Qué significa «tratamiento» en esa oferta', 'Pregunta qué material se retirará durante la visita, si se prevé aplicar un producto y qué aspecto cabe esperar al terminar. Si se propone una aplicación, solicita su nombre y las indicaciones de uso que afecten a la vivienda. Menciona si recoges agua de lluvia en un depósito para que la empresa explique cómo tratará esa instalación.'),
        ('Cómo valorar el resultado', 'Acuerda dos puntos de vista accesibles desde el suelo para las fotos anteriores y posteriores. Además del aspecto, solicita que el parte indique qué pasó con los restos acumulados en el borde y en las salidas. Una foto amplia y un detalle de la desembocadura responden a preguntas diferentes.')]),
    lectura('ruido-gotas-en-alfeizar', 'Un goteo golpea el alféizar incluso después del chaparrón',
        'Desde el dormitorio se oye cada golpe, pero el sonido por sí solo dice poco sobre su origen. Las observaciones más útiles se hacen en dos momentos.',
        'comillas/solape', 'Detalle de piezas solapadas en una cubierta de Comillas', [
        ('Mientras está lloviendo', 'Anota en qué habitación se oye y en qué ventana. En una fachada con varios miradores, «la segunda por la derecha» cambia según mires desde dentro o desde la calle. Usa el portal, la planta y una referencia visible. Si desde el interior se distingue un punto de impacto, fotografía el conjunto de la ventana con esa referencia.'),
        ('Cuando la fachada deja de recibir lluvia', 'Mira si los golpes continúan a intervalos parecidos o si van espaciándose. Observa si también cae agua de un balcón superior o del borde de una persiana. Un saliente puede recibir agua de más arriba y soltarla sobre otra superficie. Por eso interesa contar lo que se ve en cada nivel antes de atribuir el ruido al canalón.'),
        ('Un aviso que permite preparar la visita', 'Por ejemplo: «Dormitorio al patio del portal A. La gota golpea la chapa exterior. Se seguía oyendo quince minutos después de escampar. Desde casa no veo el borde superior». Con esa descripción el administrador puede pedir acceso al punto desde el que sí se vea la trayectoria.')]),
    lectura('comprar-casa-documentacion-tejado', 'Vas a comprar una casa con tejado antiguo: qué documentación pedir',
        '«El tejado se hizo hace unos años» puede referirse a una cumbrera, a un faldón o a toda la cubierta. Hay una forma sencilla de concretarlo durante la visita.',
        'comillas/cumbrera', 'Hilera de cumbrera en una cubierta de teja de Comillas', [
        ('Relaciona cada documento con una parte de la casa', 'Lleva una foto general o un croquis. Si el propietario conserva una factura, pídele que señale qué zona corresponde a las partidas. Una mención a la cumbrera puede describir la línea superior de dos vertientes sin aclarar si se trabajó en las hileras inferiores. Anota también los anexos: un porche posterior puede tener una historia completamente distinta.'),
        ('Tres fechas que conviene separar', 'Pregunta cuándo se hizo la última obra, cuándo se limpiaron las salidas y cuándo se observó por última vez la vivienda durante lluvia. Pueden ser tres años distintos. Si la casa estuvo cerrada, registra ese intervalo; así sabrás hasta dónde llega el conocimiento de quien te enseña el inmueble.'),
        ('Qué llevar a una revisión profesional', 'Entrega las fotografías fechadas, las partidas disponibles y una lista breve de dudas concretas. Por ejemplo: «La factura menciona la vertiente de calle; queremos conocer el estado de la que da al jardín». Un informe que identifique qué pudo verse y qué quedó oculto será más útil para planificar gastos futuros.')]),
]
