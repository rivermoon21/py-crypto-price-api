from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	user_name = name.capitalize()
	return render_template('index.html', name=user_name)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404