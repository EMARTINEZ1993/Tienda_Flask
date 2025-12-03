# Guía: Desplegar este proyecto Flask en Render

Esta guía explica paso a paso cómo subir y desplegar la mini tienda (Flask) en Render (https://render.com).

## Resumen rápido
- Asegúrate de tener un repositorio Git (GitHub/GitLab) con el proyecto.
- Tener `requirements.txt` (incluyendo `gunicorn`).
- Conectar el repositorio en Render y crear un **Web Service**.
- Configurar variables de entorno y comandos de build/start.

## Requisitos previos
- Cuenta en Render (crear en https://render.com).
- Repositorio remoto con tu proyecto (GitHub o GitLab).
- Archivo `requirements.txt` en la raíz con todas las dependencias (ver ejemplo más abajo).
- Tu Flask app debe exponer la aplicación como una variable llamada `app` en `app.py` (p. ej. `app = Flask(__name__)`).
- Añadir `gunicorn` a `requirements.txt` para producción.

## Archivo `requirements.txt` (ejemplo mínimo)
```
Flask>=2.0
gunicorn
# otras dependencias de tu proyecto (p. ej. sqlalchemy, psycopg2-binary, etc.)
```

## Opcional: `Procfile`
Render no requiere un `Procfile`, pero puedes usarlo si lo deseas. Ejemplo:
```
web: gunicorn app:app
```

## Comandos Git (PowerShell)
1. Inicializar y subir a GitHub si aún no tienes repo remoto:
```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/tu_usuario/tu_repo.git
git push -u origin main
```

2. Para futuros cambios:
```powershell
git add .
git commit -m "Cambios"
git push
```

## Pasos en Render
1. Inicia sesión en Render.
2. Haz clic en **New** → **Web Service**.
3. Conecta tu cuenta GitHub/GitLab (si no está conectada) y selecciona el repositorio de la mini tienda.
4. Configura las opciones del servicio:
   - **Name**: Nombre del servicio (p. ej. `mini-tienda`).
   - **Environment**: `Python`.
   - **Region**: elige la región cercana a tus usuarios.
   - **Branch**: `main` (o la rama que uses).
5. Build Command (opcional):
   - Puedes dejar vacío para usar el default o poner: `pip install -r requirements.txt`
6. Start Command:
   - Usar: `gunicorn app:app` (ajusta si tu módulo/app tiene otro nombre, p. ej. `product.app` → `gunicorn product:app`).
7. Haz clic en **Create Web Service**. Render empezará a compilar e instalar dependencias.

## Variables de entorno y secretos
En la pestaña **Environment** del servicio en Render, añade variables como:
- `SECRET_KEY` = tu_clave_secreta
- `FLASK_ENV` = `production`
- Cualquier credencial para bases de datos (p. ej. `DATABASE_URL`) o claves de servicios (Stripe, Cloudinary, etc.)

Si usas una base de datos alojada (Heroku, AWS, Railway, Render DB, etc.), añade la URL en `DATABASE_URL` y actualiza tu configuración Flask para leerla.

## Revisar logs y estado
- En la página del servicio, usa la pestaña **Logs** para ver errores de build o runtime.
- En **Events** verás deploys realizados y sus resultados.

## Posibles errores comunes
- Error `ModuleNotFoundError`: Asegúrate de que todas las dependencias estén en `requirements.txt`.
- `gunicorn` no encontrado: confirma que `gunicorn` está listado en `requirements.txt`.
- App no encontrada: verifica que el `Start Command` apunte al módulo correcto (`gunicorn app:app` si tu archivo es `app.py` y la variable se llama `app`).
- Problemas con rutas estáticas: asegúrate de que `static/` y `templates/` estén en el repo y que las rutas en Flask estén correctas.

## Despliegue automático y `render.yaml` (IaC)
Render soporta un archivo `render.yaml` para definir servicios programáticamente. Un ejemplo mínimo:
```yaml
services:
  - type: web
    name: mini-tienda
    env: python
    repo: https://github.com/tu_usuario/tu_repo
    branch: main
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

Si quieres usar `render.yaml`, añádelo a la raíz del repo y sigue la documentación de Render para deploys via `render.yaml`.

## Pruebas y comprobaciones
1. Después del deploy, abre la URL pública que Render te proporciona.
2. Revisa la página principal, páginas de producto y el carrito.
3. Usa logs si algo falla: pestaña **Logs** en el servicio.

## Buenas prácticas
- Añade `gunicorn` y fija la versión de Python (opcional: `runtime.txt` con, p. ej., `python-3.11.5`).
- No subas secretos al repo; usa las Environment Variables de Render.
- Configura un dominio personalizado desde la pestaña **Settings** si lo necesitas.

## Recursos útiles
- Documentación Render: https://render.com/docs
- Guía deploy Flask en Render (busca en la docs de Render)

---
Si quieres, puedo:
- Generar un `requirements.txt` basado en tu entorno actual.
- Añadir un `Procfile` o `render.yaml` de ejemplo al repo.
- Revisar y actualizar el `Start Command` si tu aplicación no se llama `app`.

Archivo creado: `guia_Render.md` en la raíz del proyecto.
