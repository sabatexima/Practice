from flask import Blueprint,render_template,Flask, request, jsonify

sample = Blueprint("sample", __name__)

@sample.route("/")
def index():
    print("sample.index")
    return render_template('index.html')

@sample.route("/send", methods=["POST"])
def send():
    data = request.json
    name = data.get("name")
    message = data.get("message")
    print(f"[受信] {name}：{message}")
    return render_template('in.html')