from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def birthday():
    cut = False
    if request.method == "POST":
        cut = True
    return render_template("birthday.html", cut=cut)

if __name__ == "__main__":
    app.run(debug=True)

