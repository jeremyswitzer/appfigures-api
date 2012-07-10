try:
    import simplejson as json
except ImportError:
    import json
    
from datetime import date
from types import ListType

class JsonSerializer:
    
    def deserialize(self, json_string):
        return json.loads(json_string)
    
    def serialize(self, dict_obj):
        return json.dumps(dict_obj, default=self.serialize_date)
    
    def serialize_args(self, args):
        return (self._to_string(a) for a in args)
    
    def serialize_params(self, params):
        ts,u2c = self._to_string,self._underscore_to_camelcase
        return dict([(u2c(k), ts(v)) for k,v in params.items()])
    
    def serialize_date(self, date_obj):
        if isinstance(date_obj, date):
            return date_obj.isoformat()
        else:
            raise TypeError, "No custom serialization needed for object"
    
    def serialize_list(self, list_obj):
        return ';'.join(map(str, list_obj))
    
    def _to_string(self, obj):
        if isinstance(obj, date):
            return self.serialize_date(obj)
        elif isinstance(obj, ListType):
            return self.serialize_list(obj)
        else:
            return str(obj)
        
    def _underscore_to_camelcase(self, value):   
        def camelcase(): 
            yield str.lower
            while True:
                yield str.capitalize
    
        c = camelcase()
        return "".join(c.next()(x) if x else '_' for x in value.split("_"))

        