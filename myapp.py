from flask import Flask, request

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run():
    print("تم تشغيل السكريبت")
    return "تم التنفيذ"

app.run()
