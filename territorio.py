import json
import unicodedata
from html import escape
from pathlib import Path

# Población y superficie del repertorio municipal IGN revisado el 20/10/2025.
PERFILES = json.loads((Path(__file__).parent / 'data/perfil-municipal.json').read_text())

def inicial(nombre):
    return unicodedata.normalize('NFD', nombre)[0].upper()

def indice(letras, prefijo, etiqueta):
    enlaces = ''.join(f'<a href="#{prefijo}-{letra}">{letra}</a>' for letra in sorted(set(letras)))
    return f'<nav class="indice-local" aria-label="{etiqueta}"><strong>{etiqueta}</strong><div>{enlaces}</div></nav>'

def perfil(codigo, nombre, cabecera):
    poblacion, superficie = PERFILES[codigo]
    habitantes = format(poblacion, ',').replace(',', '.')
    extension = f'{superficie:.2f}'.replace('.', ',')
    return (f'<section class="perfil-local"><h2>El municipio de {escape(nombre)}</h2>'
            f'<dl><div><dt>Cabecera municipal</dt><dd>{escape(cabecera)}</dd></div>'
            f'<div><dt>Superficie municipal</dt><dd>{extension} km²</dd></div>'
            f'<div><dt>Población de referencia¹</dt><dd>{habitantes} habitantes</dd></div></dl>'
            '<small>¹ Datos municipales de la edición de octubre de 2025.</small></section>')
