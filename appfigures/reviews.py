import requests

try:
    import simplejson as json
except ImportError:
    import json

REVIEWS_BASE_URI = "reviews/"

class ReviewsClient():
    def __init__(self, user, password, base_url, uri=REVIEWS_BASE_URI, requester=requests):
        self._user = user
        self._password = password
        self._base_url = base_url
        self._uri = uri
        self._requester = requester
        
    def get_reviews(self, product_id, page, countries, **kwargs):
        
        url = '%s/%s/%s/%s/%d' % (self._base_url, self._uri, product_id, countries, page)
        result = self._requester.get(url, params=kwargs, auth=(self._user, self._password))
        return json.loads(result.text)
    
    