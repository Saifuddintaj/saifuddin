from flask import Flask
from flask.templating import render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index',methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/resume',methods=['GET'])
def resume():
    return render_template("resume.html")