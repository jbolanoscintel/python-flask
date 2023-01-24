class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    locked = db.Column(db.Boolean(), default=True, nullable=False)
    update_at = Column(DateTime(timezone=True), server_default=db.func.now())
    created_at = Column(DateTime(timezone=True), onupdate=db.func.now())\
    todo = relationship("Todo")
    profile = relationship("Profile")

    def __init__(self, email, password, active, locked):
        self.email = email
        self.password = password