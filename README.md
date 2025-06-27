# Gestor de Estudiantes

Aplicación web en Django para gestionar estudiantes, materias, profesores y calificaciones.

## Características

- Listado, búsqueda y filtrado de estudiantes.
- Registro y edición de estudiantes, materias, profesores y calificaciones.
- Exportación de datos a Excel.
- Panel de administración personalizado.
- Interfaz moderna con Tailwind CSS.

## Requisitos

- Python 3.10 o superior
- pip
- Git

## Instalación

1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/Eric-Montero/gestor_estudiantes.git
   cd gestor_estudiantes
   ```

2. **Crea y activa un entorno virtual:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones:**
   ```sh
   py manage.py makemigrations
   py manage.py migrate
   ```

5. **Crea un superusuario:**
   ```sh
   py manage.py createsuperuser
   ```

6. **Inicia el servidor:**
   ```sh
   py manage.py runserver
   ```

7. **Accede a la aplicación:**
   - [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Licencia

MIT

---

Desarrollado por [[Eric Montero](https://github.com/Eric-Montero)].