import unittest
from mock import MagicMock
from appfigures.errors import AppFiguresException, ServerException
from appfigures.services import ResultService


class ResultServiceTest(unittest.TestCase):

    def setUp(self):
        self.requester = MagicMock()
        self.serializer = MagicMock()
        self.builder = MagicMock()
        self.response = MagicMock()
        self.result_service = ResultService(self.requester, self.serializer, self.builder)
        self.url = "http://example.com"
        self.in_args = ("test1", "test2")
        self.out_args = ("test3", "test4")
        self.in_params = { "key1": "value1" }
        self.out_params = { "key2": "value2" }
        self.input_json = "Test Json input"
        self.response.body = "Test Json Body"
        self.result_dict = { "result": "Result"}

    def test_get_result(self):
        self.requester.get.return_value = self.response
        self.serializer.serialize_args.return_value = self.out_args
        self.serializer.serialize_params.return_value = self.out_params
        self.serializer.deserialize.return_value = self.result_dict
        self.builder.construct_url.return_value = self.url
        
        result = self.result_service.get_deserialized_result(self.in_args, self.in_params)
        
        self.assertDictEqual(result, self.result_dict)
        self.builder.construct_url.assert_called_once_with(*self.out_args)
        self.requester.get.assert_called_once_with(self.url, self.out_params)
        self.serializer.serialize_params.assert_called_once_with(self.in_params)
        self.serializer.serialize_args.assert_called_once_with(self.in_args)
        self.serializer.deserialize.assert_called_once_with(self.response.body)
    
    def test_create_new_result(self):
        self.requester.post.return_value = self.response
        self.serializer.serialize.return_value = self.input_json
        self.serializer.serialize_args.return_value = self.out_args
        self.serializer.deserialize.return_value = self.result_dict
        self.builder.construct_url.return_value = self.url
        
        result = self.result_service.create_new_result(self.in_args, self.in_params)
        
        self.assertDictEqual(result, self.result_dict)
        self.builder.construct_url.assert_called_once_with(*self.out_args)
        self.serializer.serialize.assert_called_once_with(self.in_params)
        self.serializer.serialize_args.assert_called_once_with(self.in_args)
        self.requester.post.assert_called_once_with(self.url, self.input_json)
        self.serializer.deserialize.assert_called_once_with(self.response.body)
    
    def test_update_result(self):
        self.requester.put.return_value = self.response
        self.serializer.serialize.return_value = self.input_json
        self.serializer.serialize_args.return_value = self.out_args
        self.serializer.deserialize.return_value = self.result_dict
        self.builder.construct_url.return_value = self.url
        
        result = self.result_service.update_result(self.in_args, self.in_params)
        
        self.assertDictEqual(result, self.result_dict)
        self.builder.construct_url.assert_called_once_with(*self.out_args)
        self.serializer.serialize.assert_called_once_with(self.in_params)
        self.serializer.serialize_args.assert_called_once_with(self.in_args)
        self.requester.put.assert_called_once_with(self.url, self.input_json)
        self.serializer.deserialize.assert_called_once_with(self.response.body)
    
    def test_delete_result(self):
        self.requester.delete.return_value = self.response
        self.serializer.serialize_args.return_value = self.out_args
        self.serializer.deserialize.return_value = self.result_dict
        self.builder.construct_url.return_value = self.url
        
        result = self.result_service.delete_result(self.in_args)
        
        self.assertDictEqual(result, self.result_dict)
        self.builder.construct_url.assert_called_once_with(*self.out_args)
        self.requester.delete.assert_called_once_with(self.url)
        self.serializer.serialize_args.assert_called_once_with(self.in_args)
        self.serializer.deserialize.assert_called_once_with(self.response.body)
    
    def test_raise_error(self):
        result_dict = { "status": 500, "message": "test", "additional": "", "reference": 111 }
        self.requester.get.return_value = self.response
        self.serializer.deserialize.return_value = result_dict
        self.serializer.serialize_args.return_value = self.out_args
        self.serializer.serialize_params.return_value = self.out_params
        self.builder.construct_url.return_value = self.url
        
        try:
            result = self.result_service.get_deserialized_result(self.in_args, self.in_params)
            del result
            self.fail("Should have failed.")
        except AppFiguresException as ex:
            self.assertTrue(isinstance(ex, ServerException))


if __name__ == "__main__":
    unittest.main()