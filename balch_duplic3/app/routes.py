from flask import render_template
from app_factory import app

@app.route('/')
def home():
    return render_template('index.html')  # Ensure this is the correct 'index.html'







