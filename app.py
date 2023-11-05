from flask import Flask, render_template
from data import get_logpings as glp
app = Flask(__name__)

@app.route('/')
def index():
    server_dict = glp()
    return render_template('index.html', servers=server_dict)
