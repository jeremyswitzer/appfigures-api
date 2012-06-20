import unittest
from datetime import date
from mock import MagicMock
from appfigures.events import EventsClient, EVENTS_BASE_URI

class EventsClientTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://example.com"
        self.result_service = MagicMock()
        self.events_client = EventsClient(self.base_url, self.result_service)

    def test_get_reviews(self):
        result_dict = { 'test': 'test' }
        expected_uri = "{0}/{1}".format(self.base_url, EVENTS_BASE_URI)
        
        self.result_service.get_deserialized_result.return_value = result_dict
        
        result = self.events_client.get_events()
        
        self.assertDictEqual(result, result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_uri, None)
        
    def test_create_review(self):
        result_dict = { 'test': 'test' }
        expected_uri = "{0}/{1}".format(self.base_url, EVENTS_BASE_URI)
        
        self.result_service.create_new_result.return_value = result_dict
        
        caption = "Test Event"
        event_date = date.today()
        products = [10000,20000]
        
        expected_params = { "caption": caption, "date": event_date.isoformat(), "products": products }
        
        result = self.events_client.create_event(caption, event_date, products)
        
        self.assertDictEqual(result, result_dict)
        self.result_service.create_new_result.assert_called_once_with(expected_uri, expected_params)
        
    def test_update_review(self):
        result_dict = { 'test': 'test' }
        event_id = 10000
        expected_uri = "{0}/{1}/{2}".format(self.base_url, EVENTS_BASE_URI, event_id)
        
        self.result_service.update_result.return_value = result_dict
        
        caption = "Test Event"
        event_date = date.today()
        products = [10000,20000]
        
        expected_params = { "caption": caption, "date": event_date.isoformat(), "products": products }
        
        result = self.events_client.update_event(event_id, caption, event_date, products)
        
        self.assertDictEqual(result, result_dict)
        self.result_service.update_result.assert_called_once_with(expected_uri, expected_params)
        
    def test_delete_result(self):
        result_dict = { 'Success': 'True' }
        event_id = 10000
        expected_uri = "{0}/{1}/{2}".format(self.base_url, EVENTS_BASE_URI, event_id)
        
        self.result_service.delete_result.return_value = result_dict
        
        result = self.events_client.delete_event(event_id)
        
        self.assertTrue(result)
        self.result_service.delete_result.assert_called_once_with(expected_uri)
        
if __name__ == "__main__":
    unittest.main()