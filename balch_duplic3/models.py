from app_factory import db


# This will map to your `basic` table in MySQL
class Basic(db.Model):
    __tablename__ = 'basic'  # Specify the table name if it's not the same as the model name

    basic_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Basic {self.title}>'

