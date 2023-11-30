from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        greeting = f'Hello, {name}!'
        return render_template('greet.html', greeting=greeting)


if __name__ == '__main__':
    app.run(debug=True)
