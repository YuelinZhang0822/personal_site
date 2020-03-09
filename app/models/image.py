from app import db
from marshmallow import Schema, fields

class ImageSchema(Schema):
    """
    Fields to deserialize/show/update manually
    """
    id = fields.Int()
    title = fields.Str()


class Wish(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary, nullable=False)
    text = db.Column(db.String(1024), nullable=True)

    def __init__(self, data, text=''):
        self.data = data
        self.text = text

    def to_dict(self):
        return ImageSchema().dump(self)

    def to_json(self):
        return ImageSchema().dumps(self)