from ..extensions import db

class Timestamp(db.Model):
    __tablename__ = "dim_timestamp"
    
    timestamp_id = db.Column(db.Integer, primary_key=True)
    timestamp_name = db.Column(db.String(50))
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)