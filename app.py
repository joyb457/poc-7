from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "POC-7 CI/CD Successful"

app.run(host="0.0.0.0", port=5000)
