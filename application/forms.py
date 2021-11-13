from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

class add_cust(FlaskForm):
    cust_id= IntegerField('cust_id')
    first_name= StringField('first_name')
    last_name= StringField('last_name')
    address= StringField('address')
    phone_no= IntegerField('phone_no')
    submit = SubmitField('add Customer')

class update_cust(FlaskForm):
    cust_id= IntegerField('cust_id')
    first_name= StringField('first_name')
    last_name= StringField('last_name')
    address= StringField('address')
    phone_no= IntegerField('phone_no')
    submit = SubmitField('update Customer')

class add_order(FlaskForm):
    order_id= IntegerField('order_id')
    item= StringField('item')
    quantity= IntegerField('quantity')
    price= IntegerField('price')
    submit = SubmitField('add order')

class update_order(FlaskForm):
    order_id= IntegerField('order_id')
    item= StringField('item')
    quantity= IntegerField('quantity')
    price= IntegerField('price')
    submit = SubmitField('update Order')