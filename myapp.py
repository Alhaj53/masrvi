from flask import Flask, render_template, jsonify
from api_script import get_api_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run():
    result = get_api_data()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
