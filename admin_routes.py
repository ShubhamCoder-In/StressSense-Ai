from flask import Blueprint, render_template, redirect, url_for, session, request

# Create a Blueprint for admin routes
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# ------------------- Admin Panel -------------------

# Dashboard
@admin_bp.route("/")
def dashboard():
    return render_template("AdminDashboard.html")

# Users Management
@admin_bp.route("/users")
def users():
    # Admin can view/manage users
    return render_template("users.html")

# Reports
@admin_bp.route("/reports")
def reports():
    return render_template("reports-admin.html")

# Settings / Admin Profile
@admin_bp.route("/settings")
def settings():
    return render_template("settings-admin.html")

@admin_bp.route("/update_profile", methods=["POST"])
def update_profile():
    # Example: update admin profile from form
    # admin['name'] = request.form.get('name')
    # admin['email'] = request.form.get('email')
    return redirect(url_for("admin.settings"))

# Logout
@admin_bp.route("/logout")
def logout():
    session.clear()  # clear session if using login system
    return redirect(url_for("index"))  
# Login page
@admin_bp.route("/login")
def login():
    return render_template("login.html")
