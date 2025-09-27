from flask import Blueprint, render_template, redirect, url_for, session

# Create Blueprint
expert_bp = Blueprint("expert", __name__, url_prefix="/expert")

# ------------------- Expert Panel -------------------

@expert_bp.route("/")
def dashboard():
    # Render expert dashboard
    return render_template("expertDashboard.html")

@expert_bp.route("/students")
def students():
    # Render a page showing expert's students
    return render_template("students.html")

@expert_bp.route("/reports")
def reports():
    # Render a page for reports
    return render_template("reports.html")

@expert_bp.route("/logout")
def logout():
    # Clear session and redirect to login
    session.clear()
    return redirect(url_for("index"))    # Assuming login_page route is '/'

