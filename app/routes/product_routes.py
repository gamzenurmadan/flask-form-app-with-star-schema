from ..models import Product
from ..extensions import db
from flask import Blueprint, request, jsonify

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/products", methods=["POST"])
def add_product():
    data=request.get_json()
    new_product = Product(product_name=data["product_name"], product_category=data["product_category"], product_stock=data["product_stock"])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "product "+ new_product.product_name +" added successfully."})

@product_bp.route("/products", methods=["GET"])
def get_product():
    products = Product.query.all()
    return jsonify([{"product_id":p.product_id, "product_name":p.product_name, "product_category":p.product_category, "product_stock":p.product_stock} for p in products])

@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "product is deleted successfully."})

@product_bp.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data=request.get_json()
    product = Product.query.get_or_404(product_id)
    product.product_name = data.get("product_name", product.product_name)
    product.product_category = data.get("product_category", product.product_category)
    product.product_stock = data.get("product_stock", product.product_stock)
    db.session.commit()
    return jsonify({"message": "product is updated successfully."})