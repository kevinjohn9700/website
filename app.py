"""
Tiny Flask server for the site.

Run it with:
    pip install flask
    python app.py

Then open the link it prints (usually http://127.0.0.1:5000).

You do NOT need this to just view the site — double-clicking index.html
in your file explorer works fine too. This is only here because you
asked for Python: it's handy if you want to add features later (a
password gate, a guestbook, counting how many times she's visited...).
"""

from flask import Flask, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


# Photos referenced in index.html as "photos/filename.jpg" are served
# automatically since the whole folder is treated as static content.

if __name__ == "__main__":
    print("\nOpen this in your browser:  http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
