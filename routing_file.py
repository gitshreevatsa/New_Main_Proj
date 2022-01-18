from flask import request
from classModels import create, delete, read, update
from db_file import app

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
    
