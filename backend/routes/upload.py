from flask import Blueprint, request, jsonify
import os

from services.preprocessing import preprocess_data

upload_bp = Blueprint("upload", __name__)

UPLOAD_FOLDER = "uploads"

@upload_bp.route("/", methods=["POST"])
def upload_file():
    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, "temp.xlsx")
    file.save(filepath)


    df_scaled = preprocess_data(filepath)

    return jsonify({
        "message": "File processed successfully",
        "rows": len(df_scaled),
        "columns": list(df_scaled.columns)
    })
