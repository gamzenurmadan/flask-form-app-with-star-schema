from ..models import Sales
from ..extensions import db
from flask import Blueprint, jsonify, request

sales_bp = Blueprint("sales_bp", __name__)

@sales_bp.route("/sales", methods=["POST"])
def add_sale():
    data = request.get_json()
    for item in data:
        new_sale = Sales(customer_id=item["customer_id"], product_id=item["product_id"], timestamp_id=item["timestamp_id"], cost=item["cost"])
        db.session.add(new_sale)
    db.session.commit()
    return jsonify({"message":"sale is added successfully"}), 201

@sales_bp.route("/sales", methods=["GET"])
def get_sale():
    sales = Sales.query.all()
    data = [
        {
            'sales_id': entry.sales_id,
            'customer_id': entry.customer_id,
            'product_id': entry.product_id,
            'timestamp_id': entry.timestamp_id,
            'cost': entry.cost
        }
        for entry in sales
    ]
    return jsonify(data), 200

#It would be risky to update the fact table since it would effect the dimension tables as well.

@sales_bp.route("/sales/<int:sales_id>", methods=["DELETE"])
def delete_sale(sales_id):
    sale = Sales.query.get_or_404(sales_id)
    db.session.delete(sale)
    db.session.commit()
    return jsonify({"message":"sale is deleted successfully"})
