import requests

try:
    import simplejson as json
except ImportError:
    import json

SALES_BASE_URI = "sales/"
BY_PRODUCT = "products"

class SalesClient():
    def __init__(self, user, password, base_url, uri=SALES_BASE_URI, requester=requests):
        self._user = user
        self._password = password
        self._base_url = base_url
        self._uri = uri
        self._requester = requester

    def get_sales_report(self, report_type, startdate, enddate, **kwargs):
        
        url = "%s%s%s/%s/%s/" % (self._base_url, self._uri, report_type, startdate.isoformat(), enddate.isoformat())
        query = dict([(self.underscore_to_camelcase(k), v) for k,v in kwargs.items()])
        result = self._requester.get(url, params=query, auth=(self._user, self._password))
        return json.loads(result.text)
    
    def underscore_to_camelcase(self, value):
        def camelcase(): 
            yield str.lower
            while True:
                yield str.capitalize
    
        c = camelcase()
        return "".join(c.next()(x) if x else '_' for x in value.split("_"))