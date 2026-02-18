from flask import Blueprint, request, jsonify
from services.preprocessing import preprocess_data
from services.quantum_model import run_quantum_model

quantum_bp = Blueprint("quantum", __name__)

@quantum_bp.route("/run", methods=["POST"])
def run_quantum():
    encoding = request.json.get("encoding", "ZZ")

    df = preprocess_data("uploads/temp.xlsx")

    q_labels, q_scores = run_quantum_model(
        df,
        encoding=encoding
    )

    return jsonify({
        "encoding": encoding,
        "anomalies": int((q_labels == -1).sum()),
        "scores": q_scores.tolist()
    })
