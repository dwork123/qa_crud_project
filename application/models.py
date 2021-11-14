from application import db


class customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key= True)
    first_name= db.Column(db.String(50))
    last_name= db.Column(db.String(50))
    address= db.Column(db.String(255))
    phone_no= db.Column(db.Integer)
    customer_orders= db.relationship('order', backref= 'customer')

# order_product = db.Table('order_product',
#     db.Column('order_id', db.Integer, db.ForeignKey('order.order_id'), primary_key=True),
#     db.Column('product_id', db.Integer, db.ForeignKey('product.product_id'), primary_key=True)
# )

class order(db.Model):
    order_id = db.Column(db.Integer, primary_key= True)
    item= db.Column(db.String(50))
    quantity= db.Column(db.Integer)
    price= db.Column(db.Integer)
    customer_id= db.Column(db.Integer, db.ForeignKey('customer.customer_id'))

    # products = db.relationship ('product', secondary=order_product)
    
# class product(db.model):
#     product_id = db.Column(db.Integer, primary_key)
#     customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customer.customer_id'))
#     order_id =db.Column('order_id', db.Integer, db.ForeignKey('order.order_id'))
