from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cancion(db.Model):
    __tablename__ = "canciones"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.Integer)
    artista = db.Column(db.String(100))
    genero = db.Column(db.String(50))
    popularidad = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "duracion": self.duracion,
            "artista": self.artista,
            "genero": self.genero,
            "popularidad": self.popularidad
        }
