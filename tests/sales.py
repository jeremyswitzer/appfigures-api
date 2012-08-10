import datetime
import unittest
from mock import MagicMock

from appfigures.constants import SALES_BASE_URI, REPORT_BY_COUNTRY_AND_PRODUCT
from appfigures.sales import SalesClient

class TestSalesApi(unittest.TestCase):
    
    def setUp(self):
        self.base_url = "http://example.com"
        self.result_service = MagicMock()
        self.sales_client = SalesClient(self.result_service)
    
    def test_report_by_country_and_product(self):
        result_dict = { 'test': 'test' }
        expected_params = { 'paramOne': 'test2', 'paramTwoTwo': 'test2' }
        
        startdate = datetime.date(2011, 10, 1)
        enddate = datetime.date(2012, 4, 22)
        
        expected_args = (SALES_BASE_URI, REPORT_BY_COUNTRY_AND_PRODUCT, startdate, enddate)
        
        self.result_service.get_deserialized_result.return_value = result_dict
        
        result = self.sales_client.get_sales_report(REPORT_BY_COUNTRY_AND_PRODUCT, 
                                                    startdate, enddate, **expected_params)
        
        self.assertDictEqual(result, result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, expected_params)
        
if __name__ == '__main__':
    unittest.main()