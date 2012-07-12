import unittest

from mock import MagicMock

from appfigures.users import UsersClient, USERS_BASE_URI, USERS_PRODUCTS


class Test(unittest.TestCase):


    def setUp(self):
        self.result_service = MagicMock()
        self.email = u"testing@appfigures.com"
        self.result_dict = { "Success": True }
        self.result_service.get_deserialized_result.return_value = self.result_dict
        self.client = UsersClient(self.result_service)


    def test_get_without_info_type(self):
        result = self.client.get_user_info(self.email)
        expected_args = (USERS_BASE_URI, self.email)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, None)
        
    def test_get_with_info_type(self):
        result = self.client.get_user_info(self.email, USERS_PRODUCTS)
        expected_args = (USERS_BASE_URI, self.email, USERS_PRODUCTS)
        
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()