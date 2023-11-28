from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__, url_prefix="")


@main_bp.route("/", methods=["GET"])
def all_users():
    return jsonify({"Hello": "World"}), 200
