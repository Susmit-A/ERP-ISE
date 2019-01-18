from flask import Flask, render_template, request
from classes.FirebaseObject import FirebaseObject
from classes.Student import Student
from classes.Department import Department
from classes.Scheme import Scheme
from classes.Subject import Subject
from classes.Teacher import Teacher

app = Flask(__name__)


@app.route("/")
@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/department")
def department():
    return render_template("department.html", departments=Department.fetch_all())


@app.route("/departmentinfo", methods=['GET', 'POST'])
def departmentinfo():
    dept = request.args['department']
    dept_name = Department.get_name(dept)
    staff = list(dict(Teacher.fetch_all(dept)).values())
    students = dict(Student.fetch_all(dept=dept, sem=5))
    return render_template("department_info.html", dept=dept_name, staff=staff, students=students)


FirebaseObject()
if __name__ == "__main__":
    app.run(debug=True)
