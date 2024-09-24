from flask import Flask

# Creating the Flask app instance
app = Flask(__name__, template_folder='templates', static_folder='static')

# Importing the routes after the app is initialized
from app import routes

