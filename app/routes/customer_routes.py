from ..models import Customer
from ..extensions import db
from flask import Blueprint, request, jsonify

customer_bp = Blueprint("customer_bp", __name__)

@customer_bp.route("/customers", methods=["POST"])
def add_customer():
    data = request.get_json()
    new_customer = Customer(customer_name=data["customer_name"], customer_surname=data["customer_surname"], customer_city=data["customer_city"])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "customer "+ new_customer.customer_name +" added successfully."})

@customer_bp.route("/customers", methods=["GET"])
def get_customer():
    customers = Customer.query.all()
    return jsonify([{"customer_id":c.customer_id,"customer_name":c.customer_name, "customer_surname":c.customer_surname, "customer_city":c.customer_city} for c in customers])

@customer_bp.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    data = request.get_json()
    customer = Customer.query.get_or_404(customer_id)
    customer.customer_name = data.get('customer_name', customer.customer_name)
    customer.customer_surname = data.get('customer_surname', customer.customer_surname)
    customer.customer_city = data.get('customer_city', customer.customer_city)
    db.session.commit()
    return jsonify({"message":"customer is updated succesfully"})

@customer_bp.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message":"customer is deleted succesfully"})