import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    SECRET_KEY = os.getenv("SeCRET_KEY","santoshi")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY","santoshi_jwt")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL","sqlite:///billing.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv("FLASK_ENV","development")
