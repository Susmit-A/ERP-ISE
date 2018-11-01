from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/profile")
def profile():
	return render_template("profile.html")

@app.route("/department")
def department():
	return render_template("department.html")

@app.route("/departmentinfo")
def departmentinfo():
	return render_template("department_info.html")

if __name__ == "__main__":
    app.run(debug=True)