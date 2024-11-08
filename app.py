from flask import Flask

app = Flask(__name__)
#made some change made to this code. Welcome to page. Some changes again jiji made some changes at home. Made an update to the code here !
@app.route("/")
def home():
    return "<body style='color:red';width:100%;height:100%><h1>Hello, this is a test page for the Flask application mahn, welcome! Thursday.  </h1></body>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
