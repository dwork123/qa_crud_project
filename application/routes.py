from flask import request, redirect, render_template
from application import app, db
from application.forms import add_cust, update_cust
from application.models import customer, order


@app.route('/')
def home():
    cust= customer.query.all()
    order= order.query.all()
    return render_template('Home.html', records=cust)

    
@app.route("/editrecord/<int:cust_id>", methods=['GET', 'POST'])

def editrecordform(cust_id):
    form = update_cust
    cust = customer.query.filter_by(cust_id=cust_id).first()

    if request.method == 'POST':
        cust.name = form.cust_first_name.data
        cust.last_name = form.cust_last_name.data
        cust.address = form.address.data
        cust.phone_no = form.phone_no.data
        cust.e_mail = form.e_mail.data

        db.session.commit()
        return redirect("/")
    return render_template('editform.html', form=form)


@app.route("/filterrecords",methods=["POST"])
def filterrecords():
    if request.form["cust_id"]=="all":
        return redirect("/")
    else:
        data = customer.query.filter_by(dept=request.form["cust"]).all()
        return render_template("Home.html",records=data)


#update saved records with database info
@app.route("/saverecord",methods=["GET","POST"])
def saverecord():
    form = add_cust()
    if request.method == 'POST':

        cust.name = form.cust_first_name.data
        cust.last_name = form.cust_last_name.data
        cust.address = form.address.data
        cust.phone_no = form.phone_no.data
        cust.e_mail = form.e_mail.data

        db.session.add(new_cust)
        db.session.commit()
        return redirect("/")
        return render_template("inputform.html", form=form)



#update with database info
@app.route("/personaldetails/<int:customer_id>")
def personalinformation(cust):
	data = customer.query.filter_by(cust=cust).first()
	return render_template("personalinfo.html",record=data)


@app.route("/deletecustomer/<int:customer_id>")
def deletecustomer(cust):
    cust = cust.query.filter_by(cust=cust).first()
    db.session.delete(cust)
    db.session.commit()
    return redirect("/")