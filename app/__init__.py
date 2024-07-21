from flask import Flask, render_template, request, redirect, url_for
from .config import Config
from .extensions import db
from .models import Customer, Product, Timestamp, Sales
from .routes import customer_bp, product_bp, timestamp_bp, sales_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    app.secret_key = 'supersecretkey'

    CORS(app)

    db.init_app(app)

    app.register_blueprint(customer_bp, url_prefix="/api")
    app.register_blueprint(product_bp, url_prefix="/api")
    app.register_blueprint(timestamp_bp, url_prefix="/api")
    app.register_blueprint(sales_bp, url_prefix="/api")

    @app.route("/", methods=["GET", "POST"])
    def form_design():
        if request.method == 'POST':
            row_models = request.form.getlist('row_models')
            column_models = request.form.getlist('column_models')
            return redirect(url_for('form_usage', row_models=row_models, column_models=column_models))
        return render_template('form_design.html')
        
    
    @app.route("/form-usage", methods=["GET", "POST"])
    def form_usage():
        return render_template('form_usage.html')
    
    return app