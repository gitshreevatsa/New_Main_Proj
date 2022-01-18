from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mark.db'
db = SQLAlchemy(app)

class student(db.Model):
    USN = db.Column(db.String, primary_key = True)
    Name = db.Column(db.String(100), nullable = False)
    Email = db.Column(db.String(100), nullable = False)
    Phone = db.Column(db.Integer, nullable = False)
    Course = db.Column(db.String(100), nullable = False)
    Semester = db.Column(db.Integer, nullable = False)
    
    def __init__(self,USN = None, Name=None, Email=None, Phone = None,Course = None, Semester = None):
        self.USN = USN
        self.Name = Name
        self.Email = Email
        self.Phone = Phone
        self.Course = Course
        self.Semester = Semester
