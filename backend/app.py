from flask import Flask
from flask_cors import CORS

from routes.upload import upload_bp
from routes.classical import classical_bp
from routes.quantum import quantum_bp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(upload_bp, url_prefix="/api/upload")
app.register_blueprint(classical_bp, url_prefix="/api/classical")
app.register_blueprint(quantum_bp, url_prefix="/api/quantum")

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

