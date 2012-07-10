import unittest

from appfigures import api, sales
from appfigures.services import ResultService
from appfigures.transport import HttpResponse
from datetime import date
from mock import MagicMock


class LocalIntegrationTest(unittest.TestCase):


    def setUp(self):
        self.requester = MagicMock()
        result_service = create_closed_result_service(self.requester, api.PODIO_API_URL_1_1)
        self.client = api.Client("test", "test", result_service=result_service)
        
        self.startdate = date(2012, 1, 1)
        self.enddate = date(2012, 2, 2)
        self.products = [10000, 20000, 30000]
        self.usa = "US"
        self.response = MagicMock()
        self.response.text = '{ "Success": true }'
        self.response.status_code = 200
        self.return_response = HttpResponse(self.response)
        self.return_dict = { "Success": True }


    def test_get_sales_report_by_product(self):
        
        self.requester.get.return_value = self.return_response
        
        report = self.client.get_sales_report_by_product(self.startdate, self.enddate, 
                                                         data_source=api.DATASOURCE_DAILY, 
                                                         product_ids=self.products, country=self.usa)
        
        expected_url = "{0}/{1}/{2}/{3}/{4}".format(api.PODIO_API_URL_1_1, 
                                                    sales.SALES_BASE_URI, 
                                                    sales.SALES_BY_PRODUCT, 
                                                    self.startdate.isoformat(), 
                                                    self.enddate.isoformat())
        
        expected_params = { 
            "dataSource": api.DATASOURCE_DAILY, 
            "productIds": ';'.join(str(i) for i in self.products),
            "country": self.usa
        }
        
        self.assertDictEqual(report, self.return_dict)
        self.requester.get.assert_called_once_with(expected_url, expected_params)

def create_closed_result_service(requester, base_url):
    from appfigures.serialization import JsonSerializer
    from appfigures.urls import AppFiguresUrlBuilder
    
    serializer = JsonSerializer()
    url_builder = AppFiguresUrlBuilder(base_url)
    
    return ResultService(requester, serializer, url_builder)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()