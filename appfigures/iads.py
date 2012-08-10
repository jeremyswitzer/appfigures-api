from appfigures.base import BaseClient

IADS_BASE_URI = "iads"

class iAdsClient(BaseClient):

    def __init__(self, result_service, uri=IADS_BASE_URI):
        super(iAdsClient, self).__init__(uri, result_service)
    
    def get_iads(self, report_type, startdate, enddate, **kwargs):
        args = (report_type, startdate, enddate)
        return self.get_response(args, kwargs)
