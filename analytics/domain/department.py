from .dash_board import DashBoard
from analytics.repositories.department import DepartmentRepo


class DepartmentDashboard(DashBoard):
    repo = DepartmentRepo

    @classmethod
    def get_components(cls, dept_id):
        # component = {
        #     'teamId': '',
        #     'teamName': '',
        #     'teamLeadName': '',
        #     'teamLeadPhoto': '',  # just assume file name available in db table in one of the column
        # }
        teams = []
        for team in cls.get_teams(dept_id):
            teams.append(
                {
                    'teamId': team.id,
                    'teamName': team.name,
                    'teamLeadName': team.teamLead.name,  # get from users table
                    'teamLeadPhoto': team.teamLead.photo,  # get from users table
                }
            )
        return teams

    @classmethod
    def get_teams(cls, dept_id):
        return cls.repo.get_teams_by_department(dept_id=dept_id)
