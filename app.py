# Gestor de Tareas #

from flask import Flask

app = Flask(__name__)

# configuración de base de datos
# entiendo que es la configuración, pero en realidad que esta haciendo? solo para saber, y ya pueda decidir si es algo que necesito tener en la cabeza u olvidar por el momento
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos
from flask_sqlalchemy import SQLAlchemy
# Conectar Base de Datos
db = SQLAlchemy(app) # Instancia de SQLAlchemy con (app) como parámetro

@app.route('/')
def hola_mundo():
    return "hola kai, te amobbb"




if __name__ == "__main__":
    app.run(debug=True)
