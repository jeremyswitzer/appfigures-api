def exception_check(fn):
    def wrapper(self, *args, **kwargs):
        result = fn(self, *args, **kwargs)
        if "status" in result:
            import sys, errors
            ex = errors.EXCEPTIONS[result["status"]]
            raise ex, ex(result["message"], result["additional"], result["reference"]), sys.exc_info()[2]
        return result
    return wrapper

class ResultService:
    
    def __init__(self, requester, serializer):
        self._requester = requester
        self._serializer = serializer
    
    @exception_check
    def get_deserialized_result(self, url, params=None):
        result = self._requester.get(url, params)
        return self._serializer.deserialize(result.body)
    
    @exception_check
    def create_new_result(self, url, params):
        body = self._serializer.serialize(params)
        result = self._requester.post(url, body)
        return self._serializer.deserialize(result.body)
    
    @exception_check
    def update_result(self, url, params):
        body = self._serializer.serialize(params)
        result = self._requester.put(url, body)
        return self._serializer.deserialize(result.body)
    
    @exception_check
    def delete_result(self, url):
        result = self._requester.delete(url)
        return self._serializer.deserialize(result.body)

def create_default_result_service(username, password):
    from transport import HttpRequester
    from serialization import JsonSerializer
    
    requester = HttpRequester(username, password)
    serializer = JsonSerializer()
    
    return ResultService(requester, serializer)