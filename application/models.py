from application import db

class customer(db.Model):
    customer_id = db.column(db.Integer, primary_key= True)
    first_name= db.column(db.String(50))
    last_name= db.column(db.String(50))
    address= db.columndb.Column(db.char(255))
    phone_no= db.column(db.Integer)
    email_address= db.column(db.String(50))
    customer_orders= db.relationship('order', backref= 'customer')

class order(db.Model):
    order_id = db.column(db.Integer, primary_key= True)
    item= db.column(db.String(50))
    quantity= db.column(db.Integer)
    price= db.column(db.Integer)
    customer_id= db.column(db.Integer, db.foreign_key('customer.customer_id'))
    
    # def __repr__(self):
    #     return f"{self.quantity} {self.item} {self.price} {self.customer_id}"
