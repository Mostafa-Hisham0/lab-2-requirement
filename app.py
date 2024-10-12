from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        return render_template('result.html', name=name, number=number)

if __name__ == "__main__":
    app.run(debug=True)
