from flask import Flask
import os

app = Flask(__name__)


if __name__ == "__main__":
    app.run( debug=True, host='0.0.0.0', port=5007)