from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    """Modelo de usuario"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        #Encripta y guarda la contraseña
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        #Verifica si la contraseña es correcta
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        #Convierte el usuario a diccionario
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
