from application import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    prize = db.Column(db.String(30), nullable=False)
    reference = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return ''.join(['user id: ', str(self.id), '\r\n', 'name: ', self.first_name, ' ', self.last_name, '\r\n', 'time: ', str(self.time), '\r\n', 'prize: ', self.prize, '\r\n', 'id number: ', self.id_string])