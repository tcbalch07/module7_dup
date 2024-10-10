from flask import Flask
from app.db_connect import get_db, close_db
from app.blueprints.books import books

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)
    app.secret_key = '6595'  # Replace with a secure key or environment variable

    # Register Blueprints (ensure this is done only once)
    app.register_blueprint(books, name='books_blueprint')

    # Setup database connection teardown
    @app.teardown_appcontext
    def teardown_db(exception=None):
        close_db(exception)

    return app
