from flask import render_template
from app import app
from datetime import datetime

@app.route('/')
def index():
    current_date = datetime.now().strftime("%B %d, %Y")
    return render_template('index.html', current_date=current_date)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')

