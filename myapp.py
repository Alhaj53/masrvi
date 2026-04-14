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

        if not pin or not num:
            return jsonify({"status": "error", "msg": "missing_data"})

        # تشغيل script.py مع إرسال المدخلات له
        result = subprocess.run(
            ["python", "script.py", num, pin],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        try:
            data = json.loads(output)
        except:
            return jsonify({
                "status": "error",
                "msg": "bad_script_output",
                "raw": output
            })

        if "access_token" in data:
            return jsonify({
                "status": "success",
                "token": data["access_token"]
            })

        return jsonify({"status": "fail", "data": data})

    except Exception as e:
        return jsonify({
            "status": "error",
            "details": str(e)
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
