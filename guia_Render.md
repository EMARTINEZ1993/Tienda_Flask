# Guía rápida: desplegar en Render

Pasos mínimos para poner la `mini-tienda` en Render (sencillo y directo).

1) Preparar el repo
- Asegúrate de que el proyecto está en GitHub/GitLab y la rama principal es `main`.

2) `requirements.txt` mínimo
```
Flask>=2.0
gunicorn
```

3) Crear el Web Service en Render
- Name: `mini-tienda`
- Language: `Python 3`
- Branch: `main`
- Region: elige la que prefieras (p. ej. `Oregon` si ya tienes servicios allí)
- Root Directory: dejar vacío (si tu app está en la raíz)
- Build Command: `pip install -r requirements.txt`
- Start Command (OBLIGATORIO): `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2`

Nota: tu archivo principal es `app.py` y define `app = Flask(__name__)`, por eso el entrypoint es `app:app`.

4) Variables de entorno (en Render → Environment)
- `FLASK_SECRET_KEY` = tu_clave_secreta (la app usa `FLASK_SECRET_KEY`)
- Otras variables: `DATABASE_URL`, claves de terceros, etc.

5) Comandos Git para subir cambios (PowerShell)
```powershell
git add requirements.txt
git commit -m "Add requirements for Render"
git push
```

6) Revisar despliegue
- En la consola de Render: pestaña **Deploys** y **Logs** para ver errores.

Problemas frecuentes (rápido)
- `ModuleNotFoundError`: faltan paquetes en `requirements.txt`.
- `gunicorn` no encontrado: añadir `gunicorn` a `requirements.txt`.
- App no arranca: verificar `Start Command` y que `app.py` define `app`.

Si quieres, puedo crear `requirements.txt` y commitearlo ahora. ¿Lo hago?
