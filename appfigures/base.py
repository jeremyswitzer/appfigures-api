import datetime
import types

class BaseClient(object):
    
    def __init__(self, base_url, endpoint_uri, result_service):
        self._base_url = base_url
        self._enpoint_uri = endpoint_uri
        self._result_service = result_service
        
    def get_response(self, uri, params=None):
        return self._result_service.get_deserialized_result(uri, params)
    
    def create_item(self, uri, params):
        return self._result_service.create_new_result(uri, params)
    
    def update_item(self, uri, params):
        return self._result_service.update_result(uri, params)
    
    def delete_item(self, uri):
        return self._result_service.delete_result(uri)
    
    def construct_uri(self, *args):
        parts = [self._base_url, self._enpoint_uri]
        parts.extend(args)
        parts = [str(p).strip('/ ') for p in parts]
        uri = '/'.join(parts)
        return uri
    
    def format_date(self, date_obj):
        return date_obj.isoformat()
    
    def format_list(self, list_obj):
        return ';'.join(map(str, list_obj))
    
    def format_to_string(self, obj):
        if isinstance(obj, datetime.date):
            return self.format_date(obj)
        elif isinstance(obj, types.ListType):
            return self.format_list(obj)
        else:
            return obj
            
    def convert_params(self, **kwargs):
        fmt = self.format_to_string
        u2c = self.underscore_to_camelcase
        return dict([(u2c(k), fmt(v)) for k,v in kwargs.items()])
        
    def underscore_to_camelcase(self, value):
        def camelcase(): 
            yield str.lower
            while True:
                yield str.capitalize
    
        c = camelcase()
        return "".join(c.next()(x) if x else '_' for x in value.split("_"))
