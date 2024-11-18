# Entrega Proyecto Web Personal.
Este proyecto consiste en el desarrollo de una página web personal utilizando el framework **Django**. Incluye dos aplicaciones principales: `core` (para las funcionalidades generales) y `portfolio` (para la gestión de proyectos). Además, el proyecto está configurado con un workflow de GitHub Actions para la ejecución automática de los test.
## Repositorio.
- Link: https://github.com/mgonzalz/doo_web-personal
- Usuario: María González - [@mgonzalz](https://github.com/mgonzalz)

## Estructura del proyecto.
```python
.
├── manage.py
├── requirements.txt
├── webpersonal/
│   ├── webpersonal/    # Carpeta principal de la configuración del proyecto.
│       ├── settings.py
│       ├── urls.py
│       ├── ...
│       ├── core/                # Aplicación principal.
│           ├── templates/
│           ├── views.py
│           ├── ...
│       ├── portfolio/           # Aplicación para gestionar proyectos del portafolio.
│           ├── models.py        # Definición de modelos.
│           ├── admin.py         # Configuración para el panel de administración.
│           ├── ...
│       ├── media /      # Imágenes de los proyectos creados.
├── resources/           # Carpeta con plantillas HTML.
│   ├── index.html
│   ├── ...
```
- Core: Aplicación para funcionalidades generales como `home` o las páginas estáticas.
- Portfolio: Aplicación que permite gestionar proyectos, almacenándolos en la base de datos.
- Automatización con Github Actions: Workflow configurado para ejecutar pruebas de los modelos definidos en la aplicación `portfolio`.
- Gestión de dependencias: Incluye un archivo `requirements.txt` con las dependencias necesarias para ejecutar el proyecto.

## Instalación.
### Creación de un entorno virtual.
Primero se deberá de crear un entorno virtual, en este caso lo llamaremos: `env-django`.
```powershell
python -m venv env-django
env\Scripts\activate
```
- Nota: Si se realiza en VSCode se deberá de añadir este comando antes de activar para otorgar los permisos adecuados: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

Una vez que el entorno virtual esté activado, deberás instalar las dependencias del proyecto.
```powershell
pip install -r requirements.txt
```
### Migración de datos y acceso a la aplicación.
Para configurar la base de datos y poner en marcha el servidor de desarrollo, es necesario realizar las migraciones. Esto permitirá actualizar la base de datos según las migraciones definidas en el proyecto, garantizando que todos los cambios realizados en los modelos se apliquen correctamente.

```powershell
cd webpersonal
python manage.py migrate
python manage.py runserver
```
Si todo está correctamente configurado, se debería de ver la página de inicio de tu aplicación Django en local. Si se desea acceder al panel de administración, ingresar a http://127.0.0.1:8000/admin y usar las credenciales del superusuario definidas.



