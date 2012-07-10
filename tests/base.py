import unittest
from mock import MagicMock
from appfigures.base import BaseClient

class BaseClientUnitTest(unittest.TestCase):

    def setUp(self):
        self.result_service = MagicMock()
        self.url_test = "http://example.com"
        self.uri_test = "uri"
        self.arg1_test = "test1"
        self.arg2_test = "test2"
        self.result_dict = { 'test': 'test' }
        self.args = (self.arg1_test, self.arg2_test)
        self.params = { 'param1': 'test1', 'param2': 'test2' }
        self.testclient = BaseClient(self.uri_test, self.result_service)
        

    def test_get_response_with_params(self):
        
        self.result_service.get_deserialized_result.return_value = self.result_dict
        
        result = self.testclient.get_response(self.args, self.params)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result \
                           .assert_called_once_with((self.uri_test,) + self.args, self.params)
        
    def test_create_item(self):
        self.result_service.create_new_result.return_value = self.result_dict
        
        result = self.testclient.create_item(self.args, self.params)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.create_new_result \
                           .assert_called_once_with((self.uri_test,) + self.args, self.params)
                           
    
    def test_update_item(self):
        self.result_service.update_result.return_value = self.result_dict
        
        result = self.testclient.update_item(self.args, self.params)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.update_result \
                           .assert_called_once_with((self.uri_test,) + self.args, self.params)
                           
    def test_delete_item(self):
        self.result_service.delete_result.return_value = self.result_dict
        
        result = self.testclient.delete_item(self.args)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.delete_result \
                           .assert_called_once_with((self.uri_test,) + self.args)
    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()