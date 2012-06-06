class ResultService:
    
    def __init__(self, requester, serializer):
        self._requester = requester
        self._serializer = serializer
        
    def get_deserialized_result(self, url, params=None):
        result = self._requester.get(url, params)
        return self._serializer.deserialize(result.body)
    
    def create_new_result(self, url, params):
        body = self._serializer.serialize(params)
        result = self._requester.post(url, body)
        return self._serializer.deserialize(result.body)
    
    def update_result(self, url, params):
        body = self._serializer.serialize(params)
        result = self._requester.put(url, body)
        return self._serializer.deserialize(result.body)
    
    def delete_result(self, url):
        result = self._requester.delete(url)
        return self._serializer.deserialize(result.body)


def create_default_result_service(username, password):
    from transport import HttpRequester
    from serialization import JsonSerializer
    
    requester = HttpRequester(username, password)
    serializer = JsonSerializer()
    
    return ResultService(requester, serializer)