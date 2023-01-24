class User(db.Model):
    __tablename__ = "Todo"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128), unique=True, nullable=False)
    author = Column(Integer, ForeignKey("User.id"))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    complete_date = db.Column(db.Boolean(), default=True, nullable=False)
    estimated_complete_date = db.Column(db.Boolean(), default=True, nullable=False)
    update_at = Column(DateTime(timezone=True), server_default=db.func.now())
    created_at = Column(DateTime(timezone=True), onupdate=db.func.now())

    def __init__(self, description, author):
        self.description = description
        self.author = author