import json
import unittest

from appfigures import api, constants as c
from appfigures.services import ResultService
from appfigures.transport import HttpResponse
from datetime import date
from mock import MagicMock


class LocalIntegrationTest(unittest.TestCase):


    def setUp(self):
        self.requester = MagicMock()
        result_service = create_closed_result_service(self.requester, c.PODIO_API_URL_1_1)
        self.client = api.Client("test", "test", result_service=result_service)
        
        self.startdate = date(2012, 1, 1)
        self.enddate = date(2012, 2, 2)
        self.products = [10000, 20000, 30000]
        self.event_id = 111111
        self.caption = "Test Caption"
        self.details = "Test Details"
        self.usa = "US"
        self.response = MagicMock()
        self.response.text = '{ "Success": true }'
        self.response.status_code = 200
        self.return_response = HttpResponse(self.response)
        self.return_dict = { "Success": True }

    #GET
    def test_get_sales_report_by_product(self):
        
        self.requester.get.return_value = self.return_response
        
        report = self.client.get_sales_report_by_product(self.startdate, self.enddate, 
                                                         data_source=c.REPORT_TYPE_DAILY, 
                                                         products=self.products, country=self.usa)
        
        expected_url = "{0}/{1}/{2}/{3}/{4}".format(c.PODIO_API_URL_1_1, 
                                                    c.SALES_BASE_URI, 
                                                    c.REPORT_BY_PRODUCT, 
                                                    self.startdate.isoformat(), 
                                                    self.enddate.isoformat())
        
        expected_params = { 
            "dataSource": c.REPORT_TYPE_DAILY, 
            "products": ';'.join(str(i) for i in self.products),
            "country": self.usa
        }
        
        self.assertDictEqual(report, self.return_dict)
        self.requester.get.assert_called_once_with(expected_url, expected_params)
    
    #POST   
    def test_create_new_event(self):
        self.requester.post.return_value = self.return_response
        
        event = self.client.create_new_event(self.caption, self.startdate, 
                                             self.details, self.products)
        
        expected_url = "{0}/{1}".format(c.PODIO_API_URL_1_1, c.EVENTS_BASE_URI)
        expected_params = json.dumps({
            "caption": self.caption,
            "date": self.startdate.isoformat(),
            "details": self.details,
            "products": self.products
        })
        
        self.assertDictEqual(event, self.return_dict)
        self.requester.post.assert_called_once_with(expected_url, expected_params)
    
    #PUT
    def test_update_event(self):
        self.requester.put.return_value = self.return_response
        
        event = self.client.update_event(self.event_id, self.caption, 
                                         self.startdate, self.details,
                                         self.products)
        
        expected_url = "{0}/{1}/{2}".format(c.PODIO_API_URL_1_1, 
                                            c.EVENTS_BASE_URI, 
                                            self.event_id)
        expected_body = json.dumps({
            "caption": self.caption,
            "date": self.startdate.isoformat(),
            "details": self.details,
            "products": self.products
        })
        
        self.assertDictEqual(event, self.return_dict)
        self.requester.put.assert_called_once_with(expected_url, expected_body)
    
    #DELETE
    def test_delete_event(self):
        self.requester.delete.return_value = self.return_response
        
        result = self.client.delete_event(self.event_id)
        
        expected_url = "{0}/{1}/{2}".format(c.PODIO_API_URL_1_1, 
                                            c.EVENTS_BASE_URI, 
                                            self.event_id)
        
        self.assertDictEqual(result, self.return_dict)
        self.requester.delete.assert_called_once_with(expected_url)
        
    def test_get_json_array_and_return_list(self):
        
        self.response.text = '''[ { "Success": true, "Failure": false },
                                { "Success": 1, "Failure": 0 } ]'''
        
        self.requester.get.return_value = self.return_response
        
        return_list = [
            { "Success": True, "Failure": False },
            { "Success": 1, "Failure": 0 }
        ]
        
        result = self.client.get_currencies()
        
        expected_url = "{0}/{1}/{2}".format(c.PODIO_API_URL_1_1, 
                                            c.DATA_BASE_URI, 
                                            c.CURRENCIES_COLLECTION)
        
        self.assertListEqual(result, return_list)
        self.requester.get.assert_called_once_with(expected_url, None)

def create_closed_result_service(requester, base_url):
    from appfigures.serialization import JsonSerializer
    from appfigures.urls import AppFiguresUrlBuilder
    
    serializer = JsonSerializer()
    url_builder = AppFiguresUrlBuilder(base_url)
    
    return ResultService(requester, serializer, url_builder)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()