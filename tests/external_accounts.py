
import unittest

from mock import MagicMock

from appfigures.external_accounts import ExternalAccountsClient, EXTERNAL_ACCOUNTS_BASE_URI


class ExternalAccountsClientTest(unittest.TestCase):


    def setUp(self):
        self.account_id = 111111
        self.nickname = "Test Name"
        self.email = u"testing@appfigures.com"
        self.password = "abc123"
        self.flag = True
        self.result_dict = { "Success": True }
        
        self.result_service = MagicMock()
        self.client = ExternalAccountsClient(self.result_service, EXTERNAL_ACCOUNTS_BASE_URI)



    def test_get_external_account_noarg(self):
        self.result_service.get_deserialized_result.return_value = self.result_dict
        
        result = self.client.get_external_account()
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result \
                           .assert_called_once_with((EXTERNAL_ACCOUNTS_BASE_URI,), None)
    
    def test_get_external_account_with_id(self):
        self.result_service.get_deserialized_result.return_value = self.result_dict
        
        result = self.client.get_external_account(self.account_id)
        self.assertDictEqual(result, self.result_dict)
        self.result_service \
            .get_deserialized_result \
            .assert_called_once_with((EXTERNAL_ACCOUNTS_BASE_URI, self.account_id), None)
    
    def test_create_external_account(self):
        from appfigures.external_accounts import ITUNES_CONNECT as account_type
        
        self.result_service.create_new_result.return_value = self.result_dict
        args = (self.nickname, self.email, self.password, self.flag, account_type)
        expected_args = (EXTERNAL_ACCOUNTS_BASE_URI,)
        expected_params = {
            "nickname": self.nickname,
            "username": self.email,
            "password": self.password,
            "auto_import": self.flag,
            "type": account_type
        }
        
        result = self.client.create_external_account(*args)
        self.assertDictEqual(result, self.result_dict)
        self.result_service.create_new_result  \
                           .assert_called_once_with(expected_args, expected_params)
        
    
    def test_update_external_account(self):
        from appfigures.external_accounts import ANDROID_MARKET as account_type
        
        self.result_service.update_result.return_value = self.result_dict
        args = (self.account_id, self.nickname, self.email, self.password, self.flag, account_type)
        expected_args = (EXTERNAL_ACCOUNTS_BASE_URI, self.account_id)
        expected_params = {
            "nickname": self.nickname,
            "username": self.email,
            "password": self.password,
            "auto_import": self.flag,
            "type": account_type
        }
        
        result = self.client.update_external_account(*args)
        self.assertDictEqual(result, self.result_dict)
        self.result_service.update_result.assert_called_once_with(expected_args, expected_params)
    
    def test_delete_external_account(self):
        self.result_service.delete_result.return_value = self.result_dict
        
        result = self.client.delete_external_account(self.account_id)
        self.assertDictEqual(result, self.result_dict)
        self.result_service.delete_result \
                           .assert_called_once_with((EXTERNAL_ACCOUNTS_BASE_URI, self.account_id))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()