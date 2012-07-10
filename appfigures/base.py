class BaseClient(object):
    
    def __init__(self, endpoint_uri, result_service):
        self._endpoint_uri = endpoint_uri
        self._result_service = result_service
        
    def get_response(self, args, params=None):
        args = (self._endpoint_uri,) + args
        return self._result_service.get_deserialized_result(args, params)
    
    def create_item(self, args, params):
        args = (self._endpoint_uri,) + args
        return self._result_service.create_new_result(args, params)
    
    def update_item(self, args, params):
        args = (self._endpoint_uri,) + args
        return self._result_service.update_result(args, params)
    
    def delete_item(self, args):
        args = (self._endpoint_uri,) + args
        return self._result_service.delete_result(args)
    

