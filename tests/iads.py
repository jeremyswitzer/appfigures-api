import unittest

from datetime import date
from mock import MagicMock

from appfigures.iads import iAdsClient, IADS_BASE_URI, IADS_BY_DAY


class iAdsClientTest(unittest.TestCase):

    def setUp(self):
        self.result_service = MagicMock()
        self.startdate = date(2012, 1, 1)
        self.enddate = date(2012, 2, 2)
        self.products = [11111, 22222, 33333]
        self.result_dict = { "Success": True }
        self.client = iAdsClient(self.result_service)
        

    def test_get_iads(self):
        self.result_service.get_deserialized_result.return_value = self.result_dict
        
        args = (IADS_BY_DAY, self.startdate, self.enddate)
        params = { 'products': self.products }
        
        result = self.client.get_iads(*args, **params)
        
        expected_args = (IADS_BASE_URI,) + args
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, 
                                                                            params)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()