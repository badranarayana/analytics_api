from .dash_board import DashBoard
from analytics.repositories.department import DepartmentRepo


class HomeDashboard(DashBoard):
    repo = DepartmentRepo

    @classmethod
    def get_components(cls):
        components = {}
        components['objectivesOnTrack'] = cls.get_objectives_on_track()
        components['objectivesRecentlyUpdated'] = cls.get_objectives_recently_updated()
        components['placeHolderKpi'] = cls.get_placeholder_kpi_graph_data()
        components['departments'] = cls.get_departments()
        return components

    @classmethod
    def get_objectives_on_track(cls):
        return []

    @classmethod
    def get_objectives_recently_updated(cls):
        return []

    @classmethod
    def get_placeholder_kpi_graph_data(cls):
        return []

    @classmethod
    def get_departments(cls):
        return []
