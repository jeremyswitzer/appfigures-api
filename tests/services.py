import unittest
from mock import MagicMock
from appfigures.errors import AppFiguresException, ServerException
from appfigures.services import ResultService


class ResultServiceTest(unittest.TestCase):

    def setUp(self):
        self.requester_mock = MagicMock()
        self.serializer_mock = MagicMock()
        self.response_mock = MagicMock()
        self.result_service = ResultService(self.requester_mock, self.serializer_mock)
        self.input_uri = "http://example.com"
        self.input_params = { "test": "test" }
        self.response_mock.body = "Test Json Body"

    def test_get_result(self):
        result_dict = { "result": "Result"}
        self.requester_mock.get.return_value = self.response_mock
        self.serializer_mock.deserialize.return_value = result_dict
        
        result = self.result_service.get_deserialized_result(self.input_uri, self.input_params)
        
        self.assertDictEqual(result, result_dict)
        self.requester_mock.get.assert_called_once_with(self.input_uri, self.input_params)
        self.serializer_mock.deserialize.assert_called_once_with(self.response_mock.body)
    
    def test_create_new_result(self):
        result_dict = { "result": "Result"}
        input_json = "Test Json input"
        self.requester_mock.post.return_value = self.response_mock
        self.serializer_mock.serialize.return_value = input_json
        self.serializer_mock.deserialize.return_value = result_dict
        
        result = self.result_service.create_new_result(self.input_uri, self.input_params)
        
        self.assertDictEqual(result, result_dict)
        self.serializer_mock.serialize.assert_called_once_with(self.input_params)
        self.requester_mock.post.assert_called_once_with(self.input_uri, input_json)
        self.serializer_mock.deserialize.assert_called_once_with(self.response_mock.body)
    
    def test_update_result(self):
        result_dict = { "result": "Result"}
        input_json = "Test Json input"
        self.requester_mock.put.return_value = self.response_mock
        self.serializer_mock.serialize.return_value = input_json
        self.serializer_mock.deserialize.return_value = result_dict
        
        result = self.result_service.update_result(self.input_uri, self.input_params)
        
        self.assertDictEqual(result, result_dict)
        self.serializer_mock.serialize.assert_called_once_with(self.input_params)
        self.requester_mock.put.assert_called_once_with(self.input_uri, input_json)
        self.serializer_mock.deserialize.assert_called_once_with(self.response_mock.body)
    
    def test_delete_result(self):
        result_dict = { "result": "Result"}
        self.requester_mock.delete.return_value = self.response_mock
        self.serializer_mock.deserialize.return_value = result_dict
        
        result = self.result_service.delete_result(self.input_uri)
        
        self.assertDictEqual(result, result_dict)
        self.requester_mock.delete.assert_called_once_with(self.input_uri)
        self.serializer_mock.deserialize.assert_called_once_with(self.response_mock.body)
    
    def test_raise_error(self):
        result_dict = { "status": 500, "message": "test", "additional": "", "reference": 111 }
        self.requester_mock.get.return_value = self.response_mock
        self.serializer_mock.deserialize.return_value = result_dict
        
        try:
            result = self.result_service.get_deserialized_result(self.input_uri, self.input_params)
            del result
            self.fail("Should have failed.")
        except AppFiguresException as ex:
            self.assertTrue(isinstance(ex, ServerException))


if __name__ == "__main__":
    unittest.main()