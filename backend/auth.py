from flask import Blueprint, request, jsonify
from models import User, db
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/api/users/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200
