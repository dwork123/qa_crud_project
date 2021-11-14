from flask import request, redirect, render_template, url_for
from application import app, db
from application.forms import add_cust, update_cust, add_order, update_order
from application.models import customer, order


@app.route('/')
def home():
    cust= customer.query.all()
    ord= order.query.all()
    print(cust)
    return render_template('home.html', records=cust)

    
@app.route("/editcustomerrecord", methods=['GET', 'POST'])
def editcustomerrecord(cust_id):
    form = update_cust
    # cust = customer.query.filter_by(cust_id=cust_id).first()
    if request.method == 'POST':
        name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone_no = form.phone_no.data

        db.session.commit()
        return redirect("/")
    else:
        return render_template('editcustomerform.html', form=form)


@app.route("/editorderrecord", methods=['GET', 'POST'])
def editorderrecord(order_id):
    form = update_order
    ord = order.query.filter_by(order_id=order_id).first()
    if request.method == 'POST':
        item = form.item.data
        quantity = form.quantity.data
        price = form.price.data

        db.session.commit()
        return redirect("/")
    else:
        return render_template('editorderform.html', form=form)


@app.route("/filterrecords",methods=["POST"])
def filterrecords():
    if request.form["cust_id"]=="all":
        return redirect("/")
    else:
        data = customer.query.filter_by(dept=request.form["cust"]).all()
        return render_template("home.html",records=data)



@app.route("/savecustomerrecord", methods=["GET","POST"])
def savecustomerrecord():
    form = add_cust()
    if request.method == 'POST':

        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone_no = form.phone_no.data

        new_customer = customer(first_name=first_name, last_name=last_name, address=address, phone_no=phone_no)
        db.session.add(new_customer)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("customerinputform.html", form=form)


@app.route("/saveorderrecord",methods=["GET","POST"])
def saveorderrecord():
    form = add_order()
    if request.method == 'POST':

        item = form.item.data
        quantity = form.quantity.data
        price = form.price.data

        new_order = order(item=item, quantity=quantity, price=price)
        db.session.add(new_order)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("orderinputform.html", form=form)



@app.route("/customerdetails/<customer_id>")
def customerinformation(customer_id):
    data = customer.query.filter_by(customer_id=customer_id).first()
    return render_template("customerinfo.html", record=data)

@app.route("/orderdetails/<order_id>")
def orderinformation(order_id):
	data = order.query.filter_by(order_id=order_id).first()
	return render_template("orderinfo.html", record=data)


@app.route("/deletecustomerrecord/<int:customer_id>")
def deletecustomer(cust_id):

    cust = customer.query.filter_by(cust_id=cust_id).first()
    db.session.delete(cust)
    db.session.commit()
    return redirect("/")
    return render_template("deleteorder.html", record=data)

@app.route("/deleteorderrecord<int:order_id>")
def deleteorder(order_id):

    ord = order.query.filter_by(order_id=order_id).first()
    db.session.delete(ord)
    db.session.commit()
    return redirect("/")