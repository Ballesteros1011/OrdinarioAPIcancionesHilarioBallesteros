from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth = Blueprint("auth", __name__)

usuario = {
    "username": "admin",
    "password": "123456"
}

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if data["username"] == usuario["username"] and data["password"] == usuario["password"]:
        token = create_access_token(identity=data["username"])
        return jsonify({"token": token})

    return jsonify({"mensaje": "Credenciales incorrectas"}), 401
