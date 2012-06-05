import unittest
from mock import MagicMock
from appfigures.base import BaseClient

class BaseClientUnitTest(unittest.TestCase):

    def setUp(self):
        self.result_service = MagicMock()
        self.url_test = "http://example.com"
        self.uri_test = "test"
        self.testclient = BaseClient(self.url_test, self.uri_test, self.result_service)

    def test_get_response_with_params(self):
        result_dict = { 'test': 'test' }
        url = "{0}/{1}".format(self.url_test,self.uri_test)
        params = { 'param1': 'test1', 'param2': 'test2' }
        
        self.result_service.get_deserialized_result.return_value = result_dict
        
        result = self.testclient.get_response(url, params)
        
        self.assertDictEqual(result, result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(url, params)
        
    def test_construct_uri(self):
        arg1,arg2,arg3 = " first/","/second "," /third /"
        expected_uri = "{0}/{1}/first/second/third".format(self.url_test,self.uri_test)
        
        result = self.testclient.construct_uri(arg1, arg2, arg3)
        
        self.assertEqual(result, expected_uri)
        
        
    def test_convert_params(self):
        input_params = { 'param_one': 'test2', 'param_two_two': 'test2' }
        expected_params = { 'paramOne': 'test2', 'paramTwoTwo': 'test2' }
        
        result = self.testclient.convert_params(**input_params)
        
        self.assertDictEqual(result, expected_params)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()