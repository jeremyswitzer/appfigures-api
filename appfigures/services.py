class ResultService:
    
    def __init__(self, requester, serializer):
        self._requester = requester
        self._serializer = serializer
        
    def get_deserialized_result(self, url, params=None):
        result = self._requester.get(url, params)
        return self._serializer.deserialize(result.body)


def create_default_result_service(username, password):
    from transport import HttpRequester
    from serialization import JsonSerializer
    
    requester = HttpRequester(username, password)
    serializer = JsonSerializer()
    
    return ResultService(requester, serializer)