from flask import request, redirect, render_template
from application import app, db
from application.forms import AddEmp, UpdateEmp
from application.models import Employee

@app.route('/')
def home():
    emps = Employee.query.all()
    return render_template('Homepage.html', records=emps)
