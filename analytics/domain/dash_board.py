

class DashBoard(object):

    @classmethod
    def get_components(cls):
        raise NotImplemented("All sub classes should implement this method to build dashboard components")

    @classmethod
    def filter_dashboard(cls, filers=None):
        """
        """
        pass