import pymongo

class MongoPipeline(object):

    def __init__(self):
        self._db = None

    @classmethod
    def from_crawler(cls, crawler):
        pass