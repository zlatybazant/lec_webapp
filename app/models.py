from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class Employee(UserMixin, db.Model):
	"""tworzy tablice pracownikow"""

__tablename__ = 'employees'

id = db.Column(db.Integer, primary_key=True)
#email = db.Colum(db.String(60), index=True, unique=True)
#username = db.Colum(db.String(60), index=True, unique=True)
first_name = db.Colum(db.String(60), index=True, unique=True)
last_name = db.Colum(db.String(60), index=True, unique=True)
password_hash = db.Colum(db.String(128))
is_admin = db.Colum(db.Boolean, default=False)
