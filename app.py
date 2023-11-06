from flask import Flask, render_template
from data import get_log
app = Flask(__name__)

@app.route('/')
def index():
    server_dict = get_log("ping")
    return render_template('index.html', servers=server_dict)
   
