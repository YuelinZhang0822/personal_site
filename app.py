from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/devdb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET"])
def show_wish_list():
    # Import Wish here to avoid import looping
    from personal_site.models.wish import Wish
    wishes = Wish.query.all()
    fomated_wishes = [{"id": wish.id, "title": wish.title, "description": wish.description} for wish in wishes]
    return fomated_wishes[0]["title"]