from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# -----------------------
# الصفحة 1
# -----------------------
@app.route("/")
def index():
    return render_template("index.html")


# -----------------------
# الصفحة 2
# -----------------------
@app.route("/page2")
def page2():
    return render_template("page2.html")


# -----------------------
# الصفحة 3
# -----------------------
@app.route("/page3")
def page3():
    return render_template("page3.html")


# -----------------------
# API تجريبي (اختياري)
# -----------------------
@app.route("/api", methods=["POST"])
def api():
    try:
        url = "https://jsonplaceholder.typicode.com/todos/1"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                "error": "API failed",
                "status": response.status_code
            })

    except Exception as e:
        return jsonify({
            "error": "Exception occurred",
            "details": str(e)
        })


# -----------------------
# تشغيل السيرفر
# -----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
