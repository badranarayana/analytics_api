

class RepositoryBase(object):
    model = None

    @classmethod
    def get_by_id(cls, id):
        return cls.model    #  "ORM query to get by id"

    @classmethod
    def get_all(cls):
        return cls.model  #  Write ORM query to get the all records from dbss

