import datetime
import unittest
from mock import MagicMock
from appfigures.sales import SalesClient, SALES_BASE_URI, SALES_BY_COUNTRY_AND_PRODUCT

class TestSalesApi(unittest.TestCase):
    
    def setUp(self):
        self.base_url = "http://example.com"
        self.result_service = MagicMock()
        self.sales_client = SalesClient(self.base_url, self.result_service)
    
    def test_report_by_country_and_product(self):
        result_dict = { 'test': 'test' }
        input_params = { 'param_one': 'test2', 'param_two_two': 'test2' }
        expected_params = { 'paramOne': 'test2', 'paramTwoTwo': 'test2' }
        
        startdate = datetime.date(2011, 10, 1)
        enddate = datetime.date(2012, 4, 22)
        
        expected_uri = "{0}/{1}/{2}/{3}/{4}".format(
                            self.base_url, SALES_BASE_URI, 
                            SALES_BY_COUNTRY_AND_PRODUCT, 
                            startdate.isoformat(), enddate.isoformat())
        
        self.result_service.get_deserialized_result.return_value = result_dict
        
        result = self.sales_client.get_sales_report(SALES_BY_COUNTRY_AND_PRODUCT, startdate, enddate, **input_params)
        
        self.assertDictEqual(result, result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_uri, expected_params)
        
if __name__ == '__main__':
    unittest.main()