import datetime
from .db import db
from .todo import Todo
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    locked = db.Column(db.Boolean(), default=True, nullable=False)
    update_at = db.Column(db.DateTime(timezone=True),
                          default=db.func.now())
    created_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    todos = db.relationship(
        "Todo", backref=db.backref("User")
    )
    profile = db.relationship(
        "Profile", backref=db.backref("User")
    )

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('UTF8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {"id": self.id,
                "email": self.email,
                "password": self.password,
                "active": self.active,
                "locked": self.active,
                "created_at": self.created_at,
                "todos": self.todos}
