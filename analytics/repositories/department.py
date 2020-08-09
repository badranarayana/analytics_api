from analytics.db.department import Department
from .base_repository import RepositoryBase


class DepartmentRepo(RepositoryBase):
    model = Department

    @classmethod
    def get_department_details_by_id(cls, id):
        return cls.get_by_id(id)

    @classmethod
    def get_teams_by_department(cls, dept_id):
        return cls.model  # Write a ORM Query to get teams by department id