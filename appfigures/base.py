class BaseClient(object):
    
    def __init__(self, base_url, endpoint_uri, result_service):
        self._base_url = base_url
        self._enpoint_uri = endpoint_uri
        self._result_service = result_service
        
    def get_response(self, uri, params=None):
        result = self._result_service.get_deserialized_result(uri, params)
        return result
    
    def construct_uri(self, *args):
        parts = [self._base_url, self._enpoint_uri]
        parts.extend(args)
        parts = [str(p).strip('/ ') for p in parts]
        uri = '/'.join(parts)
        return uri
    
    def convert_params(self, **kwargs):
        return dict([(self.underscore_to_camelcase(k), v) for k,v in kwargs.items()])
        
    def underscore_to_camelcase(self, value):
        def camelcase(): 
            yield str.lower
            while True:
                yield str.capitalize
    
        c = camelcase()
        return "".join(c.next()(x) if x else '_' for x in value.split("_"))
