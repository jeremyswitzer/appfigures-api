import unittest

from mock import MagicMock
from appfigures.data import DataClient, DATA_BASE_URI


class DataClientTest(unittest.TestCase):


    def setUp(self):
        self.result_service = MagicMock()
        self.data_type = "TEST_DATA_TYPE"
        self.result_dict = { "Success": True }
        self.result_service.get_deserialized_result.return_value = self.result_dict
        self.client = DataClient(self.result_service)
        
    
    def test_get_data(self):
        expected_args = (DATA_BASE_URI, self.data_type)
        
        result = self.client.get_data(self.data_type)
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, None)
        
    
    def test_get_data_with_other_args(self):
        store_name = "android"
        expected_args = (DATA_BASE_URI, self.data_type, store_name)
        
        result = self.client.get_data(self.data_type, store_name)
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, None)


if __name__ == "__main__":
    unittest.main()