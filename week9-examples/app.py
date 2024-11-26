from flask import Flask

app = Flask(__name__)

@app.route('/hdip')
def hello():
    return "Hello, World!"