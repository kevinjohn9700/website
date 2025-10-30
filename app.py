from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('myfile.html')

@app.route('/submit', methods=['POST'])
def submit():
    response = request.form.get('response')
    print(f"User clicked: {response}")
    return f"You clicked: {response}"

if __name__ == '__main__':
    app.run(debug=True)
