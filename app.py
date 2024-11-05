from flask import Flask

app = Flask(__name__)
#made some change
@app.route("/")
def home():
    return "<h1>Hello, this is a test page for the Flask application!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
