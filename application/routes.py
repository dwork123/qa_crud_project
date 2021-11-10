from flask import request, redirect, render_template
from application import app, db
from application.forms import add_cust, update_cust #update imports
from application.models import customer, order #update imports


#update home route eith database info
@app.route('/')
def home():
    cust = customer.query.all()
    return render_template('Home.html', records=cust)


#update editrecord with database info
@app.route("/editrecord/<int:cust_id>", methods=['GET', 'POST'])
def editrecordform(cust_id):
    form = update_cust()
    cust = customer.query.filter_by(cust_id=cust_id).first()

    if request.method == 'POST':
        cust.name = form.cust_first_name.data
        cust.salary = form.cust_last_name.data
        cust.dept = form.address.data
        cust.subject = form.phone_no.data
        cust.marks = form.e_mail.data

        cust.first_name= form.customer_id.data

        db.session.commit()
        return redirect("/")
    return render_template('editform.html', form=form)






#update filterrecords with database info
@app.route("/filterrecords",methods=["POST"])
def filterrecords():
    if request.form["dept"]=="all":
        return redirect("/")
    else:
        data = Employee.query.filter_by(dept=request.form["dept"]).all()
        return render_template("home.html",records=data)





#update saved records with database info
@app.route("/saverecord",methods=["GET","POST"])
def saverecord():
    form = add_cust()
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