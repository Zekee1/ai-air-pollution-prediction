from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Backend is running with Python!"})

@app.route("/api/data")
def data():
    sample = {
        "city": "Los Angeles",
        "pm25": 12.5,
        "pm10": 20.3,
        "aqi": "Good"
    }
    return jsonify(sample)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
