from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ROYAL KING USSD WORKING"

@app.route("/ussd", methods=["GET", "POST"])
def ussd():
    return "CON Welcome to ROYAL KING AFFORDABLE DATA HUB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
