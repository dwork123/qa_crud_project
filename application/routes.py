from flask import request, redirect, render_template
from application import app, db
from application.forms import AddEmp, UpdateEmp #update imports
from application.models import Employee #update imports

#update home route eith database info
@app.route('/')
def home():
    emps = Employee.query.all()
    return render_template('Home.html', records=emps)

#update editrecord with database info
@app.route("/editRecord/<int:empno>", methods=['GET', 'POST'])
def editRecordForm(empno):
    form = UpdateEmp()
    emp = Employee.query.filter_by(empno=empno).first()
    if request.method == 'POST':
        pass

#update filterrecords with database info
@app.route("/filterrecords",methods=["POST"])
def filterrecords():
    if request.form["dept"]=="all":
        return redirect("/")
    else:
        data = Employee.query.filter_by(dept=request.form["dept"]).all()
        return render_template("home.html",records=data)

#update saved records with database info
@app.route("/saveRecord",methods=["GET","POST"])
def saveRecord():
    form = AddEmp()
    if request.method == 'POST':
        pass 
        #add -'name' =form.name.data
        #add database info
        newperson = person
        db.session.add(newperson)
        db.session.commit()
        return redirect("/")
        return render_template("inputform.html", form=form)


#update with database info
@app.route("/personaldetails/<int:empno>")
def personalInformation(empno):
	data = Employee.query.filter_by(empno=empno).first()
	return render_template("personalinfo.html",record=data)


#update delete function with database info
@app.route("/deleteEmployee/<int:empno>")
def deleteEmployee(empno):
    emp = Employee.query.filter_by(empno=empno).first()
    db.session.delete(emp)
    db.session.commit()
    return redirect("/")