from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'The server is running...'

@app.route('/home')
def home():
	return render_template('home.html')