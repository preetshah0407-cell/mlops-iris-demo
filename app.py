
from flask import Flask, request, jsonify
import joblib
import numpy as np
from datetime import datetime, timezone

app = Flask(__name__)
model = joblib.load("/home/preetshah0407/app/iris_model.pkl")
LOG_FILE = "/home/preetshah0407/app/ml_api.log"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"], dtype=float)

        if features.shape != (4,) or not np.isfinite(features).all():
            return jsonify({"error": "Provide four numeric features"}), 400

        prediction = model.predict(features.reshape(1, -1))[0]

        log = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "input": features.tolist(),
            "prediction": str(prediction)
        }

        with open(LOG_FILE, "a") as f:
            f.write(str(log) + "\n")

        return jsonify({"prediction": str(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
