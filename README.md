# Alero Norte

Web estática de canalones y cubiertas. Requiere Python 3.10 o posterior. Netlify compila con la configuración de netlify.toml. Para probar localmente:

    SITE_URL=https://dominio.example python3 build.py
    python3 verificar.py
    python3 -m http.server -d dist

SITE_URL es el origen público definitivo. En Netlify se utiliza URL en su defecto. WHATSAPP_NUMBER habilita el contacto al compilar con el teléfono internacional del negocio. Sin teléfono el visitante puede preparar, copiar y descargar su consulta.

Los artículos se editan en editorial.py. Las fichas se generan con build.py a partir de data/. La consulta meteorológica carga AEMET cuando la persona abre el pronóstico. Los enlaces de ruta calculan el recorrido desde Bilbao.
