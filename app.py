from students import students
from teachers import teachers
from flask import Flask, jsonify

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


@app.route('/teachers', methods=['GET'])
def getTeachers():
    return jsonify({"teachers": teachers})

#My total routes for the Rest API. 
if __name__ == '__main__':
    app.run(debug=True, port=4000)