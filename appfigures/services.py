from decorators import exception_check

class ResultService:
    
    def __init__(self, requester, serializer, url_builder):
        self._requester = requester
        self._serializer = serializer
        self._url_builder = url_builder
    
    @exception_check
    def get_deserialized_result(self, args, params):
        params = self._serializer.serialize_params(params)
        url = self._create_url(args)
        result = self._requester.get(url, params)
        return self._serializer.deserialize(result.body)
    
    @exception_check
    def create_new_result(self, args, params):
        url = self._create_url(args)
        body = self._serializer.serialize(params)
        result = self._requester.post(url, body)
        return self._serializer.deserialize(result.body)
    
    @exception_check
    def update_result(self, args, params):
        url = self._create_url(args)
        body = self._serializer.serialize(params)
        result = self._requester.put(url, body)
        return self._serializer.deserialize(result.body)
    
    @exception_check
    def delete_result(self, args):
        url = self._create_url(args)
        result = self._requester.delete(url)
        return self._serializer.deserialize(result.body)
    
    def _create_url(self, args):
        parts = self._serializer.serialize_args(args)
        return self._url_builder.construct_url(*parts)

def create_default_result_service(username, password, base_url):
    from transport import HttpRequester
    from serialization import JsonSerializer
    from urls import AppFiguresUrlBuilder
    
    requester = HttpRequester(username, password)
    serializer = JsonSerializer()
    url_builder = AppFiguresUrlBuilder(base_url)
    
    return ResultService(requester, serializer, url_builder)