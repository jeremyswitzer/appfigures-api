import datetime
import unittest
from appfigures.sales import SalesClient
from appfigures.api import PODIO_API_URL_1_1

class TestSalesApi(unittest.TestCase):
    
    def setUp(self):
        self._client = SalesClient("<test_user>", "<test_password>", PODIO_API_URL_1_1)
    
    def test_report_by_product(self):
        report = self._client.get_sales_report("products", datetime.date(2011, 10, 1), datetime.date(2012, 4, 22))
        self.assertIsInstance(report, dict)
        
if __name__ == '__main__':
    unittest.main()