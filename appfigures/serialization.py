try:
    import simplejson as json
except ImportError:
    import json

class JsonSerializer:
    
    def deserialize(self, json_string):
        return json.loads(json_string)