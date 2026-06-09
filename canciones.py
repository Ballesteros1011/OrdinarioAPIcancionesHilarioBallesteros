from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Cancion

canciones = Blueprint("canciones", __name__)

@canciones.route("/canciones", methods=["GET"])
@jwt_required()
def obtener_canciones():
    return jsonify([c.to_dict() for c in Cancion.query.all()])

@canciones.route("/canciones/<int:id>", methods=["GET"])
@jwt_required()
def obtener_cancion(id):
    return jsonify(Cancion.query.get_or_404(id).to_dict())

@canciones.route("/canciones", methods=["POST"])
@jwt_required()
def crear_cancion():
    data = request.get_json()
    nueva = Cancion(
        titulo=data["titulo"],
        duracion=data["duracion"],
        artista=data["artista"],
        genero=data["genero"],
        popularidad=data["popularidad"]
    )
    db.session.add(nueva)
    db.session.commit()
    return jsonify({"mensaje": "Canción creada"}), 201

@canciones.route("/canciones/<int:id>", methods=["PUT"])
@jwt_required()
def actualizar_cancion(id):
    cancion = Cancion.query.get_or_404(id)
    data = request.get_json()

    cancion.titulo = data["titulo"]
    cancion.duracion = data["duracion"]
    cancion.artista = data["artista"]
    cancion.genero = data["genero"]
    cancion.popularidad = data["popularidad"]

    db.session.commit()
    return jsonify({"mensaje": "Canción actualizada"})

@canciones.route("/canciones/<int:id>", methods=["DELETE"])
@jwt_required()
def eliminar_cancion(id):
    cancion = Cancion.query.get_or_404(id)
    db.session.delete(cancion)
    db.session.commit()
    return jsonify({"mensaje": "Canción eliminada"})
