# Gestor de Tareas #

from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError
from extensions import db
from models import Usuario, Tarea
from dotenv import load_dotenv
from os import getenv


def crear_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    load_dotenv()
    app.secret_key = getenv('LLAVE_SECRETA')

    db.init_app(app)

    with app.app_context():
        db.create_all()



    @app.route('/', methods=['GET','POST'])
    def index():

        if request.method == 'POST':
            nombre = request.form.get('nombre').strip()
            tarea = request.form.get('tarea').strip()

            if not nombre or not tarea:
                flash("El nombre o tarea no pueden estar vacíos!", "error")

            else:
                try:
                    nuevo = Usuario(nombre=nombre)
                    db.session.add(nuevo)
                    db.session.commit()
                    tareas = Tarea(tarea_nombre=tarea, usuario_id=nuevo.id)
                    db.session.add(tareas)
                    db.session.commit()
                    flash(f"Usuario '{nombre}' y su tarea guardados con éxito.")
                except IntegrityError:
                    db.session.rollback()
                    flash("Ese nombre ya existe. Elige otro.", "error")
            
            return redirect(url_for('index'))

        lista_usuarios = Usuario.query.all()
        lista_tareas = Tarea.query.all()
        return render_template('index.html', usuarios=lista_usuarios, tareas=lista_tareas)
    
    return app

if __name__ == "__main__":
    app = crear_app()
    app.run(debug=True)

