import os,json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("toolswap.html")

@app.route('/toolswap', methods=['GET','POST'])
def toolswap():
	sn = request.form.get("serialnumber")
	pa = request.form.get("productionarea")
	pr = request.form.get("producer")
	st = request.form.get("station")
	if not sn or not pa or not pr or not st:
		return "brakuje danych"	
	file = open("lec.json", "r")

'''
:::::::::::::::::::::: TO DO ::::::::::::::
	- funkcja przeszukania pliku json po n/s, usuniecia i podmiany obszaru
	
'''
