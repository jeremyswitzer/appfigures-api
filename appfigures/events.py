from base import BaseClient

EVENTS_BASE_URI = "events"
ALL_PRODUCTS = ["All"]

class EventsClient(BaseClient):
    def __init__(self, result_service, uri=EVENTS_BASE_URI):
        super(EventsClient, self).__init__(uri, result_service) 
        
    def get_events(self):
        args = ()
        return self.get_response(args)
    
    def create_event(self, caption, event_date, details, products):
        args = ()
        params = self._create_params(caption, event_date, details, products)
        return self.create_item(args, params)
    
    def update_event(self, event_id, caption, event_date, details, products):
        args = (event_id,)
        params = self._create_params(caption, event_date, details, products)
        return self.update_item(args, params)
    
    def delete_event(self, event_id):
        args = (event_id,)
        return self.delete_item(args)
    
    def _create_params(self, caption, event_date, details, products):
        params = {
            "caption": caption,
            "date": event_date,
            "details": details,
            "products": products
        }
        return params
