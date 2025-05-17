from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 
                                       'mysql+pymysql://root:mysqlVSLV4454@localhost/city_dashboard')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("EMAIL_USER")
    MAIL_PASSWORD = os.getenv("EMAIL_PASS")
