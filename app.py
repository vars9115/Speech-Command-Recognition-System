from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/command", methods=["POST"])
def command():
    return jsonify({"message": "Command received successfully!"})


@app.route("/time")
def get_time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    return jsonify({"time": current_time})


if __name__ == "__main__":
    app.run(debug=True)