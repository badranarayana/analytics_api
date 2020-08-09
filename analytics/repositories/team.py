from analytics.db.team import Team
from .base_repository import RepositoryBase


class TeamRepo(RepositoryBase):
    model = Team

    @classmethod
    def get_team_details_by_id(cls, team_id):
        return cls.get_by_id(team_id)
    @classmethod
    def get_team_members(cls, team_id):
        return cls.model  # Write a ORM Query to get team members

    @classmethod
    def get_team_lead_details(cls, team_id):
        return cls.model  # write ORM query to get the team lead details

    @classmethod
    def get_all_teams_in_department(cls, dept_id):
        return cls.model  # write a ORM query to get the all teams by using department ID