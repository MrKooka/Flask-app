from app import app
from flask import render_template


@app.route('/')
def index():
	name = 'lol'
	return render_template('index.html',name = name)

@app.errorhandler(404)
def pageNotFount(error):
	return render_template('page404.html')