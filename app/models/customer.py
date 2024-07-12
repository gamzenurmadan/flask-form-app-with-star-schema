from ..extensions import db

class Customer(db.Model):
    __tablename__ = "dim_customer"

    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50))
    customer_surname = db.Column(db.String(50))
    customer_city = db.Column(db.String(50))