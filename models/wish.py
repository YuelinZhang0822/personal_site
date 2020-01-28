from personal_site.app import db


class Wish(db.Model):
    __tablename__ = 'wish'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String, nullable=True)

