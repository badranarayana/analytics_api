from analytics.domain.department import DepartmentDashboard
from .base_api import ResourceBase  # could be Django/ Flask Resource base class


class DepartmentDashboardApi(ResourceBase):

    def get(self):
        try:
            # get the department id from request payload
            dept_id = 1
            return DepartmentDashboard.get_components(dept_id=dept_id)
        except Exception as err:
            # logging error traceback with logger utility
            print(err.args)