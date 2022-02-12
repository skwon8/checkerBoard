from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rows=8, columns=8)

@app.route('/<int:y>')
def oneDimension(y):
    return render_template('index.html', rows=8, columns=y)

@app.route('/<int:x>/<int:y>')
def twoDimension(x, y):
    return render_template('index.html', rows=x, columns=y)

if __name__ == '__main__':
    app.run(debug=True)