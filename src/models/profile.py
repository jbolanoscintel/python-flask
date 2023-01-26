from .db import db


class Profile(db.Model):
    __tablename__ = "Profile"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128), unique=True, nullable=False)
    Owner = db.Column(db.Integer, db.ForeignKey("User.id"))
    active = db.Column(db.Boolean(), nullable=False)
    background_img = db.Column(db.String(128), nullable=True)
    profile_img = db.Column(db.String(128), nullable=True)
    update_at = db.Column(db.DateTime(timezone=True),
                          server_default=db.func.now())
    created_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    def __init__(self, description, author):
        self.description = description
        self.author = author
