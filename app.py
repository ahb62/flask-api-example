from students import students
from teachers import teachers
from flask import Flask, jsonify, request

# Our modules, that we use for developing a backend server.

app = Flask(__name__)

# Why Flask have a property called __name__? Could I write some different?

@app.route('/ping')
def ping():
    return jsonify({"message":   "Pong!"})

@app.route('/students', methods=['GET'])
def getStudents():
    return jsonify({"students": students})


@app.route('/students/<string:students_studentsFullName>', methods=['GET'])
def getStudent(students_studentsFullName):
    studentsFound = [student for student in students if student['studentsFullName'] == students_studentsFullName]
    if ( len(studentsFound) > 0 ):
        return jsonify({"student": studentsFound[0]}), print(students_studentsFullName)
    return "not found"

#Testing the POST method with Flask
@app.route('/students', methods=['POST'])
def addStudent():
    # Get the data from the request
    newStudent = {
        "Subjects Enrolled": request.json['Subjects Enrolled'],
        "V": request.json['V'],
        "studentsFullName": request.json['studentsFullName']
    }
    #In this line of code, we are adding the new Student to the list of /students
    students.append(newStudent)
    #With this line, we can see the data that we sent to the server and a message that the data was sent.
    return jsonify({"students": students, "message": "Student added successfully!"})

#An example for the PUT method

@app.route('/students/<string:student_name>', methods=['PUT'])
def updateStudent(student_name):
    studentsFound = [student for student in students if student['studentsFullName'] == student_name]
    if ( len(studentsFound) > 0 ):
        studentsFound[0]['studentsFullName'] = request.json['studentsFullName']
        studentsFound[0]['V'] = request.json['V']
        studentsFound[0]['Subjects Enrolled'] = request.json['Subjects Enrolled']
        return jsonify({"student": studentsFound[0], "message": "Student updated successfully!"})
    return jsonify({"message:" "product not found"})




#An example for the DELETE method

@app.route('/students/<string:studentsFullName>', methods=['DELETE'])
def deleteStudent(studentsFullName):
    studentsFound = [student for student in students if student['studentsFullName'] == studentsFullName]
    if ( len(studentsFound) > 0 ):
        students.remove(studentsFound[0])
        return jsonify({"message": "Student deleted successfully!"})
    return jsonify({"message": "Student not found!"})



@app.route('/teachers', methods=['GET'])
def getTeachers():
    return jsonify({"teachers": teachers})

#My total routes for the Rest API. 
if __name__ == '__main__':
    app.run(debug=True, port=4000)