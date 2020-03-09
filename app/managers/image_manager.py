import logging
from app import db
from app.models.image import Image
from app.models.image import ImageSchema
from app.managers.base_manager import BaseManager

logger =logging.getLogger(__name__)


class ImageManager(BaseManager):
    def __init__(self):
        super(ImageManager, self).__init__(Image, ImageSchema)

    def add_new(self, bidata, text=""):
        new_image = Image(bidata, text)
        db.session.add(new_image)
        db.session.commit()
        return new_image

    def update_existing(self, id, text, **kwargs):
        existing_image = self.get_one(id)
        existing_image.text = text
        db.session.commit()
        return existing_image


image_manager = ImageManager()