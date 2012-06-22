from base import BaseClient

RANKS_BASE_URI = "ranks"

class RanksClient(BaseClient):
    def __init__(self, base_url, result_service, uri=RANKS_BASE_URI):
        super(RanksClient, self).__init__(base_url, uri, result_service)
        
    def get_ranks(self, products, granularity, startdate, enddate, **kwargs):
        products,startdate,enddate = map(self.format_to_string, (products,startdate,enddate))
        uri = self.construct_uri(products, granularity, startdate, enddate)
        params = self.convert_params(**kwargs)
        result = self.get_response(uri, params)
        return result
