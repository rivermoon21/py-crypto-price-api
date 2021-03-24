
from datetime import datetime
from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

# init app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# declare database schema
class SensorData(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	sensorName = db.Column(db.String(20), unique=False, nullable=False)
	sensorData = db.Column(db.Float, unique=False, nullable=False)

	def __repr__(self) -> str:
		return 'Input: ' + self.sensorName + str(self.sensorData)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	user_name = name.capitalize()
	return render_template('index.html', name=user_name)

@app.route('/data')
def get_data():
	data = SensorData.query.all()
	outputData = []

	if data:
		for d in data:
			entry = {'time': d.timestamp, 'name': d.sensorName, 'data': d.sensorData}
			outputData.append(entry)
	else:
		outputData.append(None)

	return {"data": outputData}

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404