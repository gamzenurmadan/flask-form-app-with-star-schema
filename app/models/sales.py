from ..extensions import db

class Sales(db.Model):
    __tablename__ = "fact_sales"

    sales_id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey("dim_customer.customer_id"))
    product_id = db.Column(db.Integer, db.ForeignKey("dim_product.product_id"))
    timestamp_id = db.Column(db.Integer, db.ForeignKey("dim_timestamp.timestamp_id"))
    cost = db.Column(db.Numeric)