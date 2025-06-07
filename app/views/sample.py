from flask import Blueprint

sample = Blueprint("sample", __name__)


@sample.route("/")
def index():
    print("sample.index")
    return render_template('home/index.html')
