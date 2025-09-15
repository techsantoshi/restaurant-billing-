from flask import Blueprint, request, jsonify
from app import db
from models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register', methods=["POST"])
def register():
    data = request.jsonify
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"msg": "Username already exists"}), 400
        user = User(username=data["username"])
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg": "User registered"})
        @auth_bp.route('/login', methods=["POST"])
        def login():
            data = request.json
            user = User.query.filter_by(username=data["username"]).first()
            if not user or not user.check_password(data["password"]):
                return jsonify({"msg": "Bad credential"}), 401
                token = create_access_token(identity={"username": user.username, "is_admin": user.is_admin})
                return jsonify(access_token=token)