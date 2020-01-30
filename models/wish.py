from personal_site import db
from marshmallow import Schema, fields

class WishSchema(Schema):
    """
    Fields to deserialize/show/update manually
    """
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    status = fields.Str()


class Wish(db.Model):
    __tablename__ = 'wish'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String, nullable=True)
    status = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, title, description='', status='active'):
        self.title=title
        self.description=description
        self.status=status

    def to_dict(self):
        return WishSchema().dump(self)

    def to_json(self):
        return WishSchema().dumps(self)

