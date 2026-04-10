"""
Crear un modelo de tabla de prueba.
"""

# app es un modulo creado en el programa principal del gestor de tareas
# db es un método del módulo app, también creado en el programa principal
from app import db

# Definir Tabla
class Usuario(db.Model):

    # columna primaria con tipo de dato = integer
    id = db.Column(db.Integer, primary_key=True)
    # columna con tipo de dato string, no se puede omitir
    nombre = db.Column(db.String(100), nullable=False)
