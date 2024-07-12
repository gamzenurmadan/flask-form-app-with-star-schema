from .customer_routes import customer_bp
from .product_routes import product_bp
from .timestamp_routes import timestamp_bp
from .sales_routes import sales_bp


__all__ = [customer_bp, product_bp, timestamp_bp, sales_bp]