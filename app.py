from flask import Flask, render_template, request, session, jsonify
from user_routes import user_bp
from expert_routes import expert_bp
from admin_routes import admin_bp
from auth_routes import auth_bp
import secrets
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
from prediction import predict_stress
from bson.json_util import dumps

# ---------------- Initialize Flask App ----------------
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
CORS(app)  # Optional, for cross-origin requests

# ---------------- Routes for HTML ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

# ---------------- Register Blueprints ----------------
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(expert_bp)
app.register_blueprint(admin_bp)

# ---------------- MongoDB Setup ----------------
client = MongoClient("mongodb+srv://StressSenseUser:StressSenseUser123@stresssenseai.8jkey3a.mongodb.net/?retryWrites=true&w=majority")
db = client["StressSenceAI"]
assignments_collection = db["assignments"]

# ---------------- Assignment Routes ----------------
@app.route("/submit-assignment", methods=["POST"])
def submit_assignment():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received"}), 400

        if 'user_id' not in session:
            return jsonify({"error": "User not logged in"}), 401

        data["userId"] = session['user_id']  
        data["submittedAt"] = datetime.utcnow()
        assignments_collection.insert_one(data)
        
        return jsonify({"message": "Assignment saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/get-assignments/<user_id>", methods=["GET"])
def get_assignments(user_id):
    try:
        assignments = list(assignments_collection.find({"userId": user_id}))
        return dumps(assignments), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- Prediction Route ----------------
@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    text = data.get('text', '').strip()
    if not text:
        return jsonify({"prediction": None}), 200

    result = predict_stress(text)
    return jsonify(result)

# ---------------- Run Flask ----------------
if __name__ == "__main__":
    app.run(debug=True)

