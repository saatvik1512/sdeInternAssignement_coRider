from flask import Blueprint, request, jsonify
from app.models import UserModel
from app.services import hash_password
from app.schemas import UserSchema
from marshmallow.exceptions import ValidationError

user_routes = Blueprint("user_routes", __name__)
user_model = UserModel()

@user_routes.route("/")
def health_check():
    return {"status": "ok"}, 200

@user_routes.route("/users", methods=["GET"])
def get_all_users():
    users = user_model.get_all_users()
    return jsonify([
        {"id": user["id"], "name": user["name"], "email": user["email"]}
        for user in users
    ])

@user_routes.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = user_model.get_user(user_id)
    print(user)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    })

@user_routes.route("/users", methods=["POST"])
def create_user():
    data = request.json
    try:
        UserSchema().load(data)
    except ValidationError as err:
        return jsonify({"error": "Invalid input", "details": err.messages}), 422

    data["password"] = hash_password(data["password"])
    user_id = user_model.create_user(data)
    return jsonify({
        "id": data["id"],
        "name": data["name"],
        "email": data["email"]
    }), 201

@user_routes.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    try:
        UserSchema().load(data)
    except ValidationError as err:
        return jsonify({"error": "Invalid input", "details": err.messages}), 422

    user = user_model.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if "password" in data:
        data["password"] = hash_password(data["password"])
    result = user_model.update_user(user_id, data)
    if result.modified_count == 0:
        return jsonify({"error": "No changes made"}), 400

    updated_user = user_model.get_user(user_id)
    return jsonify({
        "id": updated_user["id"],
        "name": updated_user["name"],
        "email": updated_user["email"]
    }), 200

@user_routes.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = user_model.delete_user(user_id)
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 204