from application import db
from datetime import datetime

# class item(db.Model1):
#     item_no = db.Column(db.Integer, primary_key = True)
#     item_name = db.Column(db.String(50))
#     item_cat = db.Column(db.Integer)
#     item_size = db.Column(db.Integer)
#     storage_date = db.Column(db.String(50))
#     storage_expiry = db.Column(db.String(50))
    
# class category(db.model2):
#     item_id = db.column(db.integer, primary_key = True)
    
# -------------------------------------------------------------------------
# class player(db.Model):
#     player_id = db.Column(db.Integer, primary_key = True)
#     squad_number = db.Column(db.integer)
#     Player_name = db.Column(db.Integer(50))
#     player_age = db.Column(db.Integer)
#     player_club = db.Column(db.String(50))
#     player_nation = db.column(db.string(50))

# class team(db.Model):
#     player_id = db.Column(db.Integer, primary_key = True)
    
# class league(db.Model):
#     player_id = db.Column(db.Integer, primary_key = True)
# ---------------------------------------------------------------------------

class customer(db.model):
    customer_ID = db.column(db.integer)
    first_name= db.column(db.char(50))
    first_name= db.column(db.char(50))
    phone_no= db.column(db.integer)
    email_address= db.column(db.char(50))

class order(db.model):
    order_ID = db.column(db.integer)
    customer_ID = db.column(db.integer)
    product_ID = db.column(db.integer)
    order_clock= db.column(db.datetime)
    customer_name= db.column(db.char(50))
    customer_address= db.column(db.char(50))
    
class product (db.model):
    product_ID= db.column(db.integer)
    product_quantity= db.column(db.integer)
    product_type = db.column(db.char(50))
    