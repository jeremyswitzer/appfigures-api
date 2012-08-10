from base import BaseClient

RANKS_BASE_URI = "ranks"
TIMEZONE_USER = "user"
TIMEZONE_UTC = "utc"
TIMEZONE_EST = "est"

class RanksClient(BaseClient):
    def __init__(self, result_service, uri=RANKS_BASE_URI):
        super(RanksClient, self).__init__(uri, result_service)
        
    def get_ranks(self, products, granularity, startdate, enddate, **kwargs):
        args = (products, granularity, startdate, enddate)
        return self.get_response(args, kwargs)
