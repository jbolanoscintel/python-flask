from .db import db


class Todo(db.Model):
    __tablename__ = "Todo"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128), unique=True, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey(
        "User.id", ondelete='CASCADE'))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    complete_date = db.Column(db.Boolean(), default=True, nullable=False)
    estimated_complete_date = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=db.func.now())
    created_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    def __init__(self, description, author, estimated_complete_date):
        self.description = description
        self.author = author
        self.estimated_complete_date = estimated_complete_date
