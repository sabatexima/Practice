from flask import Blueprint
from flask import render_template

sample = Blueprint("sample", __name__)

@sample.route("/")
def index():
    print("sample.index")
    return render_template('index.html')
from flask import Flask, request, jsonify

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    name = data.get("name")
    message = data.get("message")
    print(f"[受信] {name}：{message}")
    return jsonify(reply=f"{name}さん、メッセージを受け取りました！内容：{message}")

if __name__ == "__main__":
    app.run(debug=True)