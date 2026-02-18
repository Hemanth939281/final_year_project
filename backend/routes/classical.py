from flask import Blueprint, jsonify
from services.classical_model import run_classical_models
from services.preprocessing import preprocess_data

classical_bp = Blueprint("classical", __name__)

@classical_bp.route("/run", methods=["POST"])
def run_classical():
    df = preprocess_data("uploads/temp.xlsx")
    results = run_classical_models(df)

    output = {
        model: int((labels == -1).sum())
        for model, labels in results.items()
    }

    return jsonify(output)
