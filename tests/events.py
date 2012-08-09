import unittest
from datetime import date
from mock import MagicMock
from appfigures.events import EventsClient, EVENTS_BASE_URI

class EventsClientTest(unittest.TestCase):

    def setUp(self):
        self.result_service = MagicMock()
        self.result_dict = { 'test': 'test' }
        self.events_client = EventsClient(self.result_service)

    def test_get_events(self):
        expected_args = (EVENTS_BASE_URI, )
        self.result_service.get_deserialized_result.return_value = self.result_dict
        
        result = self.events_client.get_events()
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, None)
        
    def test_create_event(self):
        caption = "Test Event"
        event_date = date.today()
        details = "Test Details"
        products = [10000,20000]
        expected_args = (EVENTS_BASE_URI, )
        expected_params = { "caption": caption, "date": event_date, 
                            "details": details, "products": products }
        
        self.result_service.create_new_result.return_value = self.result_dict
        
        result = self.events_client.create_event(caption, event_date, details, products)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.create_new_result.assert_called_once_with(expected_args, expected_params)
        
    def test_update_event(self):
        caption = "Test Event"
        event_date = date.today()
        details = "Test Details"
        products = [10000,20000]
        event_id = 10000
        expected_args = (EVENTS_BASE_URI, event_id)
        expected_params = { "caption": caption, "date": event_date, 
                            "details": details, "products": products }
        
        self.result_service.update_result.return_value = self.result_dict
        
        result = self.events_client.update_event(event_id, caption, event_date, details, products)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.update_result.assert_called_once_with(expected_args, expected_params)
        
    def test_delete_event(self):
        event_id = 10000
        expected_args = (EVENTS_BASE_URI, event_id)
        
        self.result_service.delete_result.return_value = self.result_dict
        
        result = self.events_client.delete_event(event_id)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.delete_result.assert_called_once_with(expected_args)
        
if __name__ == "__main__":
    unittest.main()