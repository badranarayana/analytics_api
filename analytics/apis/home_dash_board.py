from analytics.domain.home_dashboard import HomeDashboard
from .base_api import ResourceBase  # could be Django/ Flask Resource base class


# We use serializers/swagger to parse request and response payload
class DepartmentDashboardApi(ResourceBase):

    def get(self):
        try:
            return HomeDashboard.get_components()
        except Exception as err:
            # logging error traceback with logger utility
            print(err.args)