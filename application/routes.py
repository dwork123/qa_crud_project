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
        cust.name = form.first_name.data
        cust.last_name = form.last_name.data
        cust.address = form.address.data
        cust.phone_no = form.phone_no.data
        cust.e_mail = form.e_mail.data

        db.session.commit()
        return redirect("/")
    return render_template('editform.html', form=form)


@app.route("/editrecord/<int:order_id>", methods=['GET', 'POST'])

def editrecordform(customer_id):
    form = update_order
    order = order.query.filter_by(order_id=order_id).first()

        if request.method == 'POST':
        cust.name = form.item.data
        cust.last_name = form.quantity.data
        cust.address = form.price.data

    db.session.commit()
        return redirect("/")
    return render_template('editorderform.html', form=form)


# update filter
@app.route("/filterrecords",methods=["POST"])
def filterrecords():
    if request.form["cust_id"]=="all":
        return redirect("/")
    else:
        data = customer.query.filter_by(dept=request.form["cust"]).all()
        return render_template("Home.html",records=data)
# -----------------------------------------------------------------

#update saved records with database info
@app.route("/saverecord",methods=["GET","POST"])
def saverecord():
    form = add_cust()
    if request.method == 'POST':

        cust.name = form.first_name.data
        cust.last_name = form.last_name.data
        cust.address = form.address.data
        cust.phone_no = form.phone_no.data
        cust.e_mail = form.e_mail.data

        new_cust = customer(first_name=first_name, last_name=last_name, address=address, phone_no=phone_no, e_mail=e_mail)
        db.session.add(new_cust)
        db.session.commit()
        return redirect("/")
        return render_template("costumerinputform.html", form=form)


@app.route("/saverecord",methods=["GET","POST"])
def saverecord():
    form = add_order()
    if request.method == 'POST':



@app.route("/personaldetails/<int:customer_id>")
def personalinformation(customer_id):
	data = customer.query.filter_by(customer_id=customer_id).first()
	return render_template("customerinfo.html", record=data)

@app.route("/personaldetails/<int:order_id>")
def personalinformation(order_id):
	data = order.query.filter_by(order_id=orderr_id).first()
	return render_template("orderinfo.html", record=data)


#delete functions
@app.route("/deletecustomer/<int:customer_id>")
def deletecustomer(customer_id):
    cust = cust.query.filter_by(customer_id=custumer_id).first()
    db.session.delete(cust)
    db.session.commit()
    return redirect("/")

@app.route("/deleteorder/<int:order_id>")
def deleteorder(order_id):
    ord = order.query.filter_by(order_id=order_id).first()
    db.session.delete(ord)
    db.session.commit()
    return redirect("/")