import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World"


if name == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
