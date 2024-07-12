import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:9876@localhost:5432/star_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
