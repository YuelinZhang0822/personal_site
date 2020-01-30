from builtins import object
from collections import Iterable


class BaseManager(object):
    def __init__(self, model, schema=None):
        self.model = model
        self.schema = schema

    def add_one(self, **kwargs):
        if not self.check(**kwargs):
            raise Exception("Invalid data")
        self.add_new(**kwargs)

    def check(self, **kwargs):
        return True

    def add_new(self, **kwargs):
        raise NotImplementedError("Method add_one must be override in sub class")

    def get_one(self, id):
        return self.model.query.get(id)