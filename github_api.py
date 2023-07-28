import os
from flask import Flask

PORT = os.getenv('GITHUB_API_PORT')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
   app.run(debug=True, port=PORT)