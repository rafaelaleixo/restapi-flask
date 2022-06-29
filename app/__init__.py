from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


from .models import users, posts, commentaries
from .views import users, helper
from .routes import routes

