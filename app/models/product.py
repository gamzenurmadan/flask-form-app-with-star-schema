from ..extensions import db

class Product(db.Model):
    __tablename__ = "dim_product"

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50))
    product_category = db.Column(db.String(50))
    product_stock = db.Column(db.Integer)