from extensions import db
from sqlalchemy import ForeignKey


class Usuario(db.Model):

    __tablename__ = "usuario"
    tareas = db.relationship('Tarea')
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    clave_encriptada = db.Column(db.String(128), nullable=False)
    
    def __repr__(self):
        return f'<Usuario {self.nombre}>'

class Tarea(db.Model):

    __tablename__ = "tarea"
    id = db.Column(db.Integer, primary_key=True)
    tarea_nombre = db.Column(db.String(100), nullable=False, unique=True)
    usuario_id = db.Column(db.Integer, ForeignKey('usuario.id'))
    

    def __repr__(self):
        return f'<Tarea {self.tarea_nombre}>'