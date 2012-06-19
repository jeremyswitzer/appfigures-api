from base import BaseClient

EVENTS_BASE_URI = "events"
ALL_PRODUCTS = ["All"]

class EventsClient(BaseClient):
    def __init__(self, base_url, result_service, uri=EVENTS_BASE_URI):
        super(EventsClient, self).__init__(base_url, uri, result_service) 
        
    def get_events(self):
        uri = self.construct_uri()
        response = self.get_response(uri)
        return response
    
    def create_event(self, caption, event_date, products):
        uri = self.construct_uri()
        params = self._create_params(caption, event_date, products)
        response = self.create_item(uri, params)
        return response
    
    def update_event(self, event_id, caption, event_date, products):
        uri = self.construct_uri(event_id)
        params = self._create_params(caption, event_date, products)
        response = self.update_item(uri, params)
        return response
    
    def delete_event(self, event_id):
        uri = self.construct_uri(event_id)
        response = self.delete_item(uri)
        return response["Success"] == "True"
    
    def _create_params(self, caption, event_date, products):
        params = {
            "caption": caption,
            "date": self.format_to_string(event_date),
            "products": products
        }
        
        return params
