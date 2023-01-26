from flask.cli import FlaskGroup
from src import app, db

cli = FlaskGroup(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    cli()
