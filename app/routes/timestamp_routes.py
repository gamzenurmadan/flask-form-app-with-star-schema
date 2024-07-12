from ..models import Timestamp
from ..extensions import db
from flask import Blueprint, jsonify, request

timestamp_bp = Blueprint("timestamp_bp", __name__)

@timestamp_bp.route("/timestamps", methods=["POST"])
def add_timestamp():
    data=request.get_json()
    new_timestamp = Timestamp(timestamp_name=data["timestamp_name"], month=data["month"], year=data["year"])
    db.session.add(new_timestamp)
    db.session.commit()
    return jsonify({"message":"timestamp added successfully"})

@timestamp_bp.route("/timestamps", methods=["GET"])
def get_timestamp():
    timestamps = Timestamp.query.all()
    return jsonify([{"timestamp_id":t.timestamp_id, "timestamp_name":t.timestamp_name, "month":t.month, "year":t.year} for t in timestamps])

@timestamp_bp.route("timestamps/<int:timestamp_id>", methods=["DELETE"])
def delete_timestamp(timestamp_id):
    timestamp = Timestamp.query.get_or_404(timestamp_id)
    db.session.delete(timestamp)
    db.session.commit()
    return jsonify({"message":"timestamp is deleted successfully"})

@timestamp_bp.route("/timestamps/<int:timestamp_id>", methods=["PUT"])
def update_timestamp(timestamp_id):
    data = request.get_json()
    timestamp = Timestamp.query.get_or_404(timestamp_id)
    timestamp.timestamp_name = data.get("timestamp_name", timestamp.timestamp_name)
    timestamp.month = data.get("month", timestamp.month)
    timestamp.year = data.get("year", timestamp.year)