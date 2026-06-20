# This file will be validated by the linter tool i.e. ruff.
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world();
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
