import logging
from personal_site import db
from personal_site.models.wish import Wish
from personal_site.models.wish import WishSchema
from personal_site.managers.base_manager import BaseManager

logger = logging.getLogger(__name__)


class WishManager(BaseManager):
    def __init__(self):
        super(WishManager, self).__init__(Wish, WishSchema)

    def check(self, title, status, **kwargs):
        try:
            if not title:
                return False
            if status not in ["active", "archive", "inactive", "realized"]:
                return False
        except NameError:
            logger.exception("Missing title or status")
        return True

    def add_new(self, title, description="", status="active", **kwargs):
        new_wish = Wish(title, description, status)
        db.session.add(new_wish)
        db.session.commit()
        return new_wish

    def update_existing(self, id, title, description, status, **kwargs):
        existing_wish = self.get_one(id)
        existing_wish.title = title
        existing_wish.description = description
        existing_wish.status = status
        db.session.commit()
        return existing_wish


wish_manager = WishManager()
