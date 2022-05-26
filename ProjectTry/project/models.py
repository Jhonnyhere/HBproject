from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    father_name = db.Column(db.Text)
    address = db.Column(db.Text)
    standard = db.Column(db.Text)
    roll_no = db.Column(db.Integer)
    phone = db.Column(db.Integer)