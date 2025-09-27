from flask import Flask, render_template,request,session
from user_routes import user_bp
from expert_routes import expert_bp
from admin_routes import admin_bp
from auth_routes import auth_bp
# from assignment_routes import assignment_bp
import secrets
from flask_cors import CORS
from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime
from prediction import predict_stress
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
CORS(app)  # Optional, for cross-origin requests
from bson.json_util import dumps

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

# ---------------- Run Flask ----------------

client = MongoClient("mongodb+srv://StressSenseUser:StressSenseUser123@stresssenseai.8jkey3a.mongodb.net/?retryWrites=true&w=majority")  # Update if needed
db = client["StressSenceAI"]
assignments_collection = db["assignments"]

@app.route("/submit-assignment", methods=["POST"])
def submit_assignment():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received"}), 400

        if 'user_id' not in session:
            return jsonify({"error": "User not logged in"}), 401

        data["userId"] = session['user_id']  # save user id
        data["submittedAt"] = datetime.utcnow()
        assignments_collection.insert_one(data)
        
        return jsonify({"message": "Assignment saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/get-assignments/<user_id>", methods=["GET"])
def get_assignments(user_id):
    try:
        assignments = list(assignments_collection.find({"userId": user_id}))
        return dumps(assignments), 200  # Return JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    text = data.get('text', '').strip()
    if not text:
        return jsonify({"prediction": None}), 200  # Return null if no text

    # Call your prediction function
    result = predict_stress(text)  # Can be async or sync depending on implementation

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
