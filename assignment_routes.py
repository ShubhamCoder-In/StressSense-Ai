# from flask import Blueprint, request, jsonify
# from pymongo import MongoClient
# from datetime import datetime

# # Initialize Blueprint correctly
# assignment_bp = Blueprint('assignment',url_prefix='/assignments')

# # MongoDB setup
# MONGO_URI = "mongodb+srv://StressSenseUser:StressSenseUser123@stresssenseai.8jkey3a.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(MONGO_URI)
# db = client["StressSenceAI"]
# assignments_collection = db["assignments"]

# # Route to submit assignment
# @assignment_bp.route("/submit", methods=["POST"])
# def submit_assignment():
#     try:
#         data = request.get_json()
#         if not data:
#             return jsonify({"error": "No data received"}), 400

#         data["submittedAt"] = datetime.utcnow()
#         assignments_collection.insert_one(data)
#         return jsonify({"message": "Assignment saved successfully!"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
