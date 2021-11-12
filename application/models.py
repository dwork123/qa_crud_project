from application import db

class customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key= True)
    first_name= db.Column(db.String(50))
    last_name= db.Column(db.String(50))
    address= db.Column(db.String(255))
    phone_no= db.Column(db.Integer)
    email_address= db.Column(db.String(50))
    customer_orders= db.relationship('order', backref= 'customer')

class order(db.Model):
    order_id = db.Column(db.Integer, primary_key= True)
    item= db.Column(db.String(50))
    quantity= db.Column(db.Integer)
    price= db.Column(db.Integer)
    customer_id= db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    
    # def __repr__(self):
    #     return f"{self.quantity} {self.item} {self.price} {self.customer_id}"
