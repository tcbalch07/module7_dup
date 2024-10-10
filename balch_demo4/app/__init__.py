from flask import Flask

app = Flask(__name__)

from app import routes  # Ensure that routes are imported after initializing the app

