# Guide from: https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/1

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello friends!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
