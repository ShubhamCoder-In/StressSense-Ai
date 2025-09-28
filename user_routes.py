from flask import Blueprint, render_template, request, redirect, url_for, session, g
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()  
# Create a Blueprint for user routes
user_bp = Blueprint("user", __name__)

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.stresssense          # Database name
users_collection = db.users 

germini_key = os.getenv("GERMINI_API_KEY")

# ------------------- Helper to get current user -------------------
@user_bp.before_request
def load_user():
    g.user = None
    if 'user_id' in session:
        try:
            g.user = users_collection.find_one({"_id": ObjectId(session['user_id'])})
        except Exception as e:
            g.user = None

# ------------------- User Panel -------------------

@user_bp.route("/dashboard")
def dashboard():
    if not g.user:
        return redirect(url_for("user.login"))
    return render_template("userDashboard.html", user=g.user)

@user_bp.route("/UserProfile")
def profile():
    if not g.user:
        return redirect(url_for("user.login"))
    return render_template("userprofile.html", user=g.user)

@user_bp.route("/update_profile", methods=["POST"])
def update_profile():
    if not g.user:
        return redirect(url_for("user.login"))

    # Update user data from form
    update_data = {
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "role": request.form.get('role'),
        "bio": request.form.get('bio'),
        # "password": request.form.get('password')  # optional
    }
    # Remove None values
    update_data = {k: v for k, v in update_data.items() if v is not None}

    users_collection.update_one({"_id": ObjectId(session['user_id'])}, {"$set": update_data})
    return redirect(url_for("user.profile"))

@user_bp.route("/assessments")
def assessments():
    if not g.user:
        return redirect(url_for("user.login"))
    return render_template("Assessments.html", user=g.user)

@user_bp.route("/suggestions")
def suggestions():
    if not g.user:
        return redirect(url_for("user.login"))
    return render_template("AiSuggestion.html", user=g.user, germini_key = germini_key)

@user_bp.route("/output")
def output():
    if not g.user:
        return redirect(url_for("user.login"))
    return render_template("output.html", user=g.user)

@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))  

@user_bp.route("/login")
def login():
    return render_template("login.html")
