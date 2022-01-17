from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mark.db'
db = SQLAlchemy(app)

class student(db.Model):
    USN = db.Column(db.Integer, primary_key = True)
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
    
    
def create(body):
    sUSN = str(body['USN'])
    sName = str(body['Name'])
    sEmail = str(body['Email'])
    sPhone = str(body['Phone'])
    sCourse = str(body['Course'])
    sSemester = str(body['Semester'])
    create_array = student(sUSN, sName, sEmail, sPhone, sCourse, sSemester)
    db.session.add(create_array)
    db.session.commit()


def read():
    select = student.query.filter_by().all()  #change it to query_all
    print(select)
    print(type(select))
    data = []
    for select in select:
        data.append(
        {
        'USN' : select.USN,
        'Name' : select.Name, 
        'Email' : select.Email,
        'Phone' : select.Phone,
        'Course' : select.Course,
        'Semester' : select.Semester
        })
    return jsonify({'data' : data})



def update(body):
    grab = body['USN']
    student.query.filter_by(USN = grab).update(body)
    db.session.commit()
    
    
def delete(body):
    sUSN = body['USN']
    select = student.query.filter_by(USN = sUSN).first()
    db.session.delete(select)
    db.session.commit()


@app.route('/new_Entries', methods = ['POST'])
def new():
    body = request.get_json()
    output = create(body)
    return "Added"

@app.route('/read_Entries', methods = ['GET'])
def show(): 
    output = read()
    return output

@app.route('/update_Entries', methods = ['PUT'])
def updating():
    body = request.get_json()
    Output = update(body)
    return "Updated Successfully"

@app.route('/delete_Entries', methods = ['DELETE'])
def remove(): 
    body = request.get_json()
    output = delete(body)
    return "Delete Successful" 

if __name__ == '__main__':
    app.run(debug = True, port= 5000)
    
    
"""{
    "USN" : "3",
    "Name" : "Deepu",
    "Email" : "deepu@gmail.com",
    "Phone" : "887788778877",
    "Course" : "UG",
    "Semester" : "5"
}


{
    "data": [
        {
            "Course": "UG",
            "Email": "deepu@gmail.com",
            "Name": "Deepu",
            "Phone": 887788778877,
            "Semester": 5,
            "USN": 2
        },
        {
            "Course": "UG",
            "Email": "deepu@gmail.com",
            "Name": "Deepu",
            "Phone": 887788778877,
            "Semester": 5,
            "USN": 3
        }
    ]
}


 select = student.query.filter_by(USN = 3).first()
    print(select)
    data = {
        'USN' : select.USN,
        'Name' : select.Name, 
        'Email' : select.Email,
        'Phone' : select.Phone,
        'Course' : select.Course,
        'Semester' : select.Semester
        }
"""

