from app import db
from datetime import datetime as dt


class Todos(db.Model):
	pk = db.Column(db.Integer, primary_key=True)
	todo = db.Column(db.String(500), nullable=False)
	created = db.Column(db.DateTime, default=dt.utcnow)
	
	def __repr__(self):
		return f'{self.todo}'