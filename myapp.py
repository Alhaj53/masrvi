from flask import Flask, render_template, jsonify, request
import requests
import subprocess
import json

app = Flask(__name__)

# -----------------------
# الصفحات
# -----------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/page3")
def page3():
    return render_template("page3.html")


# -----------------------
# تشغيل السكربت مع مدخلات
# -----------------------
@app.route("/check-token", methods=["POST"])
def check_token():

    try:
        data = request.get_json()

        pin = data.get("pin")
        num = data.get("num")

        print("PIN RECEIVED:", pin)
        print("NUM RECEIVED:", num)

        result = subprocess.run(
            ["python", "script.py", pin, num],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        print("SCRIPT OUTPUT:", output)

        try:
            data = json.loads(output)
        except:
            data = {}

        if "access_token" in data:
            return jsonify({
                "token": data["access_token"]
            })

        return jsonify({"token": None})

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

@app.route("/check-otp", methods=["POST"])
def check_otp():

    data = request.get_json()

    otp = data.get("otp")
    token = data.get("token")
    num = data.get("num")
    current_pin = data.get("current_pin")

    result = subprocess.run(
        [
            "python",
            "script_otp.py",
            otp,
            token,
            num,
            current_pin
        ],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()

    try:
        return jsonify(json.loads(output))
    except:
        return jsonify({
            "status": "error",
            "output": output
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
