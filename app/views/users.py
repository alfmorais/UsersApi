import json

from flask import Blueprint, jsonify, request

from app.controllers.users import UserController

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/", methods=["GET"])
def all_users():
    users = UserController.find_all()
    return jsonify({"users": [user for user in users]}), 200


@users_bp.route("/", methods=["POST"])
def create_user():
    body = json.loads(request.data)
    return jsonify({"user": [body]})
