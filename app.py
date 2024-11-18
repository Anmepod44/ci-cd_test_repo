from flask import Flask

app = Flask(__name__)
#made some change made to this code. Welcome to page. Some changes again jiji made some changes at home. Made an update to the code here ! welcome home
@app.route("/")
def home():
    return "<body style='color:green';width:100%;height:100%><h1>Hello, welcome back to the backend dummy page </h1></body>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
