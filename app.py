from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    message = request.form.get("message")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("messages.txt", "a") as f:
        f.write(f"[{time}] {message}\n")

    return "Message sent!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
