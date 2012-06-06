import requests

class HttpRequester:
    
    def __init__(self, username, password):
        self._auth = (username, password)
    
    def get(self, uri, params):
        return HttpResponse(requests.get(uri, params=params, auth=self._auth))
    
    def post(self, uri, body):
        return HttpResponse(requests.post(uri, data=body, auth=self._auth))
    
    def put(self, uri, body):
        return HttpResponse(requests.put(uri, data=body, auth=self._auth))
    
    def delete(self, uri):
        return HttpResponse(requests.delete(uri, auth=self._auth))
        

class HttpResponse:
    
    def __init__(self, response_obj):
        self._response = response_obj
        
    @property
    def body(self):
        return self._response.text
    
    @property
    def status_code(self):
        return self._response.status_code