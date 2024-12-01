from flask import Flask

app = Flask(__name__)


# decorator
@app.route('/')
def root():
    return '<h1>Hello, world!</h1>'


@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'





if __name__ == '__main__':
    app.run(debug=True)
    