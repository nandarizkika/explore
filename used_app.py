from flask import Flask, request, jsonify, render_template
from logging import debug
from flask_cors import CORS # library for handling cross origin resources sharing.
from used_predict import make_predictions

#Untuk digunakan di postman

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def default():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data_input = request.get_json()

        result = make_predictions(data_input)
        threshold = 0.5
        risk_status = 'Resiko Tinggi' if result >= threshold else 'Resiko Rendah'
        
        result = {
            "model": "credit-risk-scoring-by-rizkika",
            "version": "beta-version-1.0.0",
            "result": result[0],
            "result_status": risk_status
        }
        
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000, debug=False)