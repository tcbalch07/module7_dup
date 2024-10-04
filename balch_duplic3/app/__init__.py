from flask import Flask
from app_factory import db

app = Flask(__name__)

# Import routes after initializing the app
from app import routes




