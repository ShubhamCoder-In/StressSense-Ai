from flask import Blueprint, request, jsonify
import bcrypt
import bson
from pymongo import MongoClient
from flask import session

auth_bp = Blueprint("auth", __name__)
# ---------------- MongoDB Connection ----------------
MONGO_URI = "mongodb+srv://StressSenseUser:StressSenseUser123@stresssenseai.8jkey3a.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.stresssense          # Database name
users_collection = db.users      # Collection for users

# ------------------- Signup API -------------------
@auth_bp.route("/api/signup", methods=["POST"])
def signup_api():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        if not name or not email or not password or not role:
            return jsonify({"message": "All fields are required!"}), 400

        # Check if user already exists
        if users_collection.find_one({"email": email}):
            return jsonify({"message": "Email already exists!"}), 409

        # Hash password
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Insert new user
        users_collection.insert_one({
            "name": name,
            "email": email,
            "password": hashed_password,
            "role": role
        })

        return jsonify({"message": "Signup successful!"}), 201

    except Exception as e:
        return jsonify({"message": f"Server error: {str(e)}"}), 500

# ------------------- Login API -------------------
@auth_bp.route("/api/login", methods=["POST"])
@auth_bp.route("/api/login", methods=["POST"])
def login_api():
    try:
        data = request.get_json()
        email, password = data.get("email"), data.get("password")
        if not email or not password:
            return jsonify({"message": "Email and password required!"}), 400

        user = users_collection.find_one({"email": email})
        if not user:
            return jsonify({"message": "Invalid email or password!"}), 401

        hashed_pw = user["password"]
        if isinstance(hashed_pw, bson.binary.Binary):
            hashed_pw = bytes(hashed_pw)

        if bcrypt.checkpw(password.encode("utf-8"), hashed_pw):
            # ✅ Save user info in session
            session['user_id'] = str(user["_id"])
            session['user_name'] = user.get("name")
            session['user_role'] = user.get("role")

            # ✅ Redirect based on role
            role = user.get("role")
            if role == "user":
                return jsonify({"redirect": "/dashboard"}), 200
            elif role == "expert":
                return jsonify({"redirect": "/expert"}), 200
            elif role == "admin":
                return jsonify({"redirect": "/admin"}), 200
            else:
                return jsonify({"message": "Role not recognized"}), 400
        else:
            return jsonify({"message": "Invalid email or password!"}), 401

    except Exception as e:
        return jsonify({"message": f"Server error: {str(e)}"}), 500