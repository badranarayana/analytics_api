from analytics.db.objective import Objective
from .base_repository import RepositoryBase


class ObjectiveRepo(RepositoryBase):
    model = Objective

    def get_objective_details_by_id(self, id):
        return self.get_by_id(id)