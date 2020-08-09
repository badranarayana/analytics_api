from analytics.db.user import User
from .base_repository import RepositoryBase


class UserRepo(RepositoryBase):
    model = User

    def get_user_details_by_id(self, id):
        return self.get_by_id(id)

    def get_objectives_by_team(self, team_id):
        return self.model  # Write a ORM Query to get team members