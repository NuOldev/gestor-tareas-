# Gestor de Tareas #

from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError
from extensions import db, bcrypt, login_manager
from flask_login import login_user
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
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/', methods=['GET', 'POST'])
    def login():
            
        if request.method == 'POST':
            correo = request.form.get('email').strip()
            password = request.form.get('password').strip()

            if not correo or not password:
                flash("El correo o contraseña no pueden estar vacíos!")
            else:
                usuario = Usuario.query.filter_by(email=correo).first()

                if usuario == None:
                    flash("Este correo aún no está registrado.", "error")
                    return redirect(url_for('login'))
            
                contrasena = bcrypt.check_password_hash(usuario.clave_encriptada, password)
                
                if contrasena:
                    login_user(usuario)
                    flash("Acceso correcto", "éxito")
                    return redirect(url_for('formulario_de_tareas'))
                else:
                    flash("Contraseña inválida", "error")
                
        return render_template('index.html')




    @app.route('/tareas', methods=['GET','POST'])
    def formulario_de_tareas():

        if request.method == 'POST':
            nombre = request.form.get('nombre').strip()
            tarea = request.form.get('tarea').strip()
            print(f"Nombre: {nombre}, Tarea: {tarea}")

            if not nombre or not tarea:
                flash("El nombre o tarea no pueden estar vacíos!")

            else:
                try:
                    nuevo_usuario = Usuario(nombre=nombre)
                    db.session.add(nuevo_usuario)
                    db.session.commit()
                    nueva_tarea = Tarea(tarea_nombre=tarea, usuario_id=nuevo_usuario.id)
                    db.session.add(nueva_tarea)
                    db.session.commit()
                    flash(f"Usuario '{nombre}' y su tarea guardados con éxito.")
                    return redirect(url_for('formulario_de_tareas'))       
                except IntegrityError as e:
                    print(f"Error: {e}")
                    db.session.rollback()
                    flash("Ese nombre ya existe. Elige otro.")        
    
            
        lista_usuarios = Usuario.query.all()
        lista_tareas = Tarea.query.all()
        return render_template('tareas.html', usuarios=lista_usuarios, tareas=lista_tareas)

    
    @app.route('/registro', methods=['GET', 'POST'])
    def formulario_de_registro():
        
        if request.method == 'POST':
            correo = request.form.get('email').strip()
            password = request.form.get('password').strip()
            pass_verification = request.form.get('password-verification').strip()

            if pass_verification != password:
                flash("Las contraseñas no coinciden, intenta nuevamente")
            else:
                try:
                    encriptado = bcrypt.generate_password_hash(password)
                    nuevo = Usuario(email=correo, clave_encriptada=encriptado)
                    db.session.add(nuevo)
                    db.session.commit()
                    print("datos guardados")
                    flash("Registro Exitoso, bienvenido.")
                    return redirect(url_for('formulario_de_tareas')) 
                except IntegrityError:
                    db.session.rollback()
                    flash("Correo en uso, usa otro correo para continuar.")

        return render_template('registro.html')
    
    return app

if __name__ == "__main__":
    app = crear_app()
    app.run(debug=True)
