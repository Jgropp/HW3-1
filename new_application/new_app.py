
from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 


@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/sentence')
def word():
	return render_template('template1.html')

@app.route('/result', methods = ['GET', 'POST'])
def string_result():
	if request.method == 'GET':
		result = request.args
		words = str(result['sentence'])
		number = len(words.split())
		return "your sentence is " + str(number) + " words long"

@app.route('/a')
def name():
	return render_template('template2.html')

@app.route('/result-2', methods = ['GET', 'POST'])
def result_two():
	if request.method == 'GET':
		result = request.args
		lettera = str(result['letter_a'])
		number = (lettera.count('a'))
		if 'a' in lettera:
			return 'The letter "a" occurs ' + ' ' + str(number)+ ' ' + ' times in the sentence'
		else:
			return 'The letter "a" is not in this sentence'

if __name__ == '__main__':
	app.run()