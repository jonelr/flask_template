# myapp/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    __tablename__ = "users"

    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.email} authenticated: {self.authenticated} active: {self.active}"

    def is_active(self):
        return self.active

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
