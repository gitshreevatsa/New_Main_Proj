from flask import jsonify
from db_file import db, student
  
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

