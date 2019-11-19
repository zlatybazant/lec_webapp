# app/__init__.py

#python modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import sqlite3
#from sqlite3 import Error

#local imports cofigs
from config import app_config

#variable for sqlite3
db = SQLAlchemy()

"""
def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
		print("Baza danych otwarta pomyslnie")
	except Error as e:
		print('An error occured')
	finally:
		if conn:
			conn.close()
if __name__ == '__main__':
	create_connection(r"./ec_data.dv")
"""
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	db.init_app(app)
	@app.route('/')
	def hello_world():
		return 'Hello World!'
	
	login_manager.init_app(app)
	login_manager.login_message = "Dostęp autoryzowany przez logowanie."
	login_manager.login_view = "auth.login"

	return app	
