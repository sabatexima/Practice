from flask import Blueprint
from flask import render_template

sample = Blueprint("sample", __name__)

@sample.route("/")
def index():
    print("sample.index")
    return render_template('home/index.html')
