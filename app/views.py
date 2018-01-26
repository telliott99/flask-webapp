from flask import render_template
from app import app


@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template("index.html")
    
@app.route('/dispatch', methods = ['POST'])
def dispatch():
    return render_template(
        'error.html',
         name = "your request")
