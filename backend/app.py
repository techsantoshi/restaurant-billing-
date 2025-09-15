from flask import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app,supports_credentials=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from models import User, Product, Order

from routtes.auth import auth_bp
from routes.admin import admin_bp
from routes.orders import orders_bp
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(orders_bp, url_prefix="/api/orders")

if __name__ == "__main__":
    app.run(debug=True)