# Apuntes para repasar lo aprendido #

* Proyecto: Gestor de Tareas

  - Objetivo General: Aprender a crear una aplicación web en la que se pueda ingresar manualmente el nombre de un usuario y una tarea que pueda realizar o que sea asignada a este, que el usuario pueda ingresar con su perfil y ver sus tareas clasificadas como en curso, pendientes o terminadas, que pueda borrar tareas, agregar notas, consultar o tener a la vista datos básicos como fecha de inicio y fecha de termino así como el tiempo que le queda para terminar una tarea.

  - Meta: Este proyecto es el segundo proyecto que voy a crear en forma, por lo tanto no es un trabajo ni hay tiempo de entrega, pero si hay un compromiso de entrega personal o para terminar en un mínimo de un (1) mes, el objetivo del plazo es trabajar constantemente, saber cuanto tiempo real se le tiene que dedicar a un proyecto de este tamaño y lo más importante es aprender a usar nuevas herramientas, desarrollar la lógica en la estructura del programa, desarrollar el programa de cero, escalar paulatinamente e interiorizar el conocimiento de verdad, con la ayuda de  Inteligencia Artificial, la busqueda de información en la red por mi cuenta, y el uso de estos apuntes que servirán para repasar cuando se necesite, para usar cada vez necesitar menos la ayuda de la asistencia y mejorar las habilidades necesarias.

  - Herramientas: El proyecto estará diseñado en Python, con el microframework Flask, y otros frameworks para usar bases de datos como flask_sqlalchemy, para la estructura visual web HTML y estilizar con CSS.

* Fecha de Inicio de proyecto > 08-4-2026 
* Fecha de Fin de proyecto > 08-05-2026 (aproximado)
* Tiempo de trabajo por semana > 5 horas (aproximado) 

_____________________________________________________________________

### Nota: no he registrado las primeras fechas de trabajo, hoy es 15-04-2026 y comenzaré por registrar brevemente lo que he aprendido, buscaré la ayuda de GEMINI para que verifique si mis conocimientos son acertados y modificar o afinar estos para que estos apuntes sean claros y certeros.

## Archivos y Carpetas ##

- Principal: app.py

  * app.py > es el archivo principal, en este se maneja la lógica para ejecutar la aplicación, se importan las herramientas antes instaladas (Flask) y los módulos creados en la construcción del programa (extensions.py, models.py).

  * Detalles:
    - from flask import Flask, render_template, request, flash, redirect, url_for *Framework para web*
    - from sqlalchemy.exc import IntegrityError *framework para DB*
    - from extensions import db *módulo*
    - from models import Usuario *módulo*

    - def crear_app(): *función para crear app*
    - app = Flask(__name__) *crear app*
    - Configuración de app: 
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db' *ruta para acceder a la DB*
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.secret_key = 'clave_secreta_para_alertas' *la usa Flask para acceder a las alertas* 
    - db.init_app(app) *inicia la app*
    - with app.app_context(): *ya hay un contexto de app, ya existe*
        db.create_all() *entonces crea una DB*
    - @app.route('/', methods=['GET','POST']) *ruta raíz (timbre para llamar a la función decorada) + métodos recibir y enviar*
        def index(): *función decorada (@)*
    - if request.method == 'POST': *si se está enviando algo (guardando en la web)*
        nombre = request.form.get('nombre').strip() *crea nombre con el valor nombre (definido en html)*
        tarea = request.form.get('tarea').strip() *igual que nombre*
    - if not nombre or not tarea: *si no se recibe nada cuando opriman guardar*
        flash("El nombre o tarea no pueden estar vacíos!", "error") *lanza mensaje (uso de Flask>flash)*
    - else: *si se mandó correctamente*
        try:
            nuevo = Usuario(nombre=nombre, tarea=tarea) *crea instancia/tabla con columnas nombre y tarea*
            db.session.add(nuevo) *agrega a DB los datos anteriores*
            db.session.commit() *asegura la agregación (basicamente)*
            flash(f"Usuario '{nombre}' guardado con éxito", "success") *Regresa un mensaje en la web*
            flash(f"Tarea '{tarea}' guardada con éxito", "success")
        except IntegrityError: *Error lanzado al violar una regla*
            db.session.rollback() *deshace la sesión bloqueada por el error anterior para que siga trabajando*
            flash("Ese nombre ya existe. Elige otro.", "error") *alerta por el error encontrado*
    - return redirect(url_for('index')) *vuelve a cargar la página principal, limpia el envío de datos evitando duplicados*
    - lista_usuarios = Usuario.query.all() *crea instancia haciendo una consulta completa de la tabla*
        return render_template('index.html', usuarios=lista_usuarios) *renderiza el HTML y envía los datos de la consulta*
    - return app *resultado final, devuelve la app con el resultado completo de todo lo que hizo previamente*
    - if __name__ == "__main__": *Ejecuta solo el archivo directo (python app.py)*
        app = crear_app() *llama a la función*
        app.run(debug=True) *reinicia el servidor por si mismo, muestra detalles de errores en la web*

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

- Secundarios: 

  * extensions.py
    - from flask_sqlalchemy import SQLAlchemy *herramienta para DB's con flask*
    - db = SQLAlchemy() *crea la instancia/DB*

  * models.py
    - from extensions import db *importa la DB creada en extensions.py*
    - class Usuario(db.Model): *Crea la tabla/clase que hereda de db*
        id = db.Column(db.Integer, primary_key=True) *crea col pk id*
        nombre = db.Column(db.String(100), nullable=False, unique=True) *Crea col nombre no duplicado no vacío*
        tarea = db.Column(db.String(200), nullable=False) *crea col no vacío*
    - def __repr__(self): *para trabajar desde la consola de python, busca datos sin recibir código extraño*
        return f'<Usuario {self.nombre}>'


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
- Carpetas: 

  * __pycache__ *maneja los módulos creados (no se sube a github > .gitignore)*
  * instance *contiene la DB tareas.db (no se sube a github > .gitignore)*
  * static *contiene archivos CSS y JS*
  * templates *contiene archivos HTML*
  * venv *contiene la información del entorno virtual (no se sube a github > .gitignore)*

- DB: tareas.db *contiene la DB*

- Frontend: index.html *lo que se muestra en la web*

- Otros archivos: 

  * .gitignore *contiene los comandos para retener archivos que no se suben a github*
  * apuntes.md (este archivo) *apuntes de lo aprendido*


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* 20-04-2026

## Variables de entorno -creación y práctica- ##

- Archivo: 
    * .env *en la raíz del programa*
    * NOMBRE_DE_VARIABLE=valor_de_la_variable *Nombre = mayusculas, valor = minusculas*

- app.py:
    * from dotenv import load_dotenv *para carga el archivo .env*
    * from os import getenv *obtiene la variable*

- crear_app():
    * load_dotenv() *carga el archivo, recibe True si es cargado correctamente*
    * app.secret_key = getenv('LLAVE_SECRETA') *obtiene el valor accediendo al nombre*


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Análisis: Siguiente paso (MVP)##

- Qué camino seguir?:
    1. login y acceso por usuario *la vía correcta en este punto*
    2. funciones básicas (borrar, agregar, estado...) *la vía incorrecta en este punto*

- 1. Login > Información mínima para acceder:
    * Autenticación - Correo y Contraseña

- models.py:
    * email = db.Column(db.String(50), nullable=False, unique=True) *correo único del usuario*
    * clave_encriptada = db.Column(db.String(128), nullable=False) *clave encriptada no única de longitud (128 por convención)*

### Para la siguiente sesión ###

- Borrar tareas.db y probar el nuevo modelo
- Instalar: Flask-Bcrypt
- Aprender a registrar un usuario con contraseña encriptada

### Nota: borrar tareas.db mientras se crea el programa es válido, pero no es una opción en un proyecto real con datos y usuarios reales. La herramienta Flask-Migrate modifica sin borrardatos y en su momento aprenderé a usar esta nueva herramienta.