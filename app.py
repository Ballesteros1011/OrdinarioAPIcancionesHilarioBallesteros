from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from routes.auth import auth
from routes.canciones import canciones

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
JWTManager(app)

app.register_blueprint(auth)
app.register_blueprint(canciones)

with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return {"mensaje": "API de canciones funcionando"}

if __name__ == "__main__":
    app.run(debug=True)
