# Necoclik Store

Pequeña tienda demo en Flask que muestra un catálogo de productos, permite filtrar por categoría, ver detalle de producto y agregar elementos a un carrito de compras en sesión.

**Características**
- Listado de productos desde `products.py`.
- Filtrado por categoría (`/categoria/<category>`).
- Página de detalle de producto (`/producto/<int:producto_id>`).
- Carrito basado en `session` con rutas para agregar (`/agregar/<int:producto_id>`), ver (`/carrito`) y vaciar (`/vaciar`).
- Plantillas Jinja en `templates/` y assets en `static/`.

**Requisitos**
- Python 3.8+ (probado con 3.10+).
- Flask (microframework).

Instalación rápida (PowerShell):

```powershell
# Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate

# Instalar Flask
pip install Flask
```

Ejecución

- Ejecutar directamente con Python (ya incluye `app.run(debug=True)`):

```powershell
python app.py
```

- Alternativamente, usar `flask run` (opcional):

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run
```

Por defecto la aplicación se sirve en `http://127.0.0.1:5000`.

Rutas principales

- `/` — Página principal con todos los productos.
- `/categoria/<category>` — Filtrar productos por categoría.
- `/producto/<int:producto_id>` — Detalle de producto.
- `/agregar/<int:producto_id>` — Agregar producto al carrito (usa `session`).
- `/carrito` — Ver carrito.
- `/vaciar` — Vaciar carrito.

Estructura del proyecto

- `app.py` — Aplicación Flask y definiciones de rutas.
- `products.py` — Lista de diccionarios `products` con los productos de ejemplo.
- `templates/` — Plantillas Jinja: `base.html`, `index.html`, `categoria.html`, `product_detail.html`, `cart.html`.
- `static/` — CSS e imágenes (ej.: `styles.css`, `img/`).

Notas y recomendaciones

- La `secret_key` está definida en `app.py` como una cadena fija. Para producción, moverla a una variable de entorno y no incluirla en el repositorio.
- No hay `requirements.txt` incluido. Para generar uno después de instalar dependencias:

```powershell
pip freeze > requirements.txt
```

- Los precios en `products.py` están en números enteros; si necesitas formateos o moneda distinta, ajustar la plantilla o los datos.

- Las imágenes referenciadas en `products.py` usan rutas en `/static/img/` (asegúrate de que las imágenes existan en esa carpeta).

Posibles mejoras

- Añadir manejo de cantidades en el carrito (actualmente agrega el id por cada clic).
- Añadir persistencia (base de datos) en lugar de lista en memoria para los productos.
- Añadir autenticación de usuarios y persistencia del carrito por usuario.

**Autor**

- Ingeniera Luz Eliana Martinez

Contacto y licencia

Proyecto de ejemplo. Modifica libremente para aprendizaje y pruebas.
