import logging
from personal_site.app import db
from personal_site.models.wish import Wish
from personal_site.managers.base_manager import BaseManager

logger = logging.getLogger(__name__)


class WishManager(BaseManager):
    def __init__(self):
        super(WishManager, self).__init__(Wish)

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

wish_manager = WishManager()