from flask import Flask
import sys
import os

port = int(os.environ.get("PORT", 8080))
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Web Data O'Mine<h1><h2>Web Project<h2>"


if __name__ == "__main__":
    print("Listening port " + str(port))
    app.run(host='0.0.0.0',port=port)
