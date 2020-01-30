from builtins import object
from personal_site.app import db


class BaseManager(object):
    def __init__(self, model, schema=None):
        self.model = model
        self.schema = schema

    def add_one(self, **kwargs):
        if not self.check(**kwargs):
            raise Exception("Invalid data")
        self.add_new(**kwargs)

    def update(self, id, **kwargs):
        obj = self.get_one(id)
        if not obj:
            self.add_one(**kwargs)
        else:
            # TODO: It's risky here. Can't make sure every model class has `to_dict()`
            obj_value = obj.to_dict()
            obj_value.update(kwargs)
            self.update_existing(id, **obj_value)

    def delete(self, id):
        """
        Dangerous! Need to add access control
        """
        obj = self.get_one(id)
        if not obj:
            raise Exception("{} object {} doesn't exist!".format(self.model.__name__, id))
        db.session.delete(obj)
        db.session.commit()

    def check(self, **kwargs):
        return True

    def add_new(self, **kwargs):
        raise NotImplementedError("Method add_one must be overrode in sub class")

    def update_existing(self, id, **kwargs):
        raise NotImplementedError("Method update_existing must be overrode in sub class")

    def get_one(self, id):
        return self.model.query.get(id)

    def get_many(self, ids):
        if not ids:
            return []
        return self.model.query.filter(self.model.id.in_(ids)).all()

    def get_all(self):
        return self.model.query.all()
