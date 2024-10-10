from flask import g
from .app_factory import create_app
from .db_connect import get_db, close_db

app = create_app()

@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_appcontext
def teardown_db(exception=None):
    close_db(exception)
