import unittest

from mock import MagicMock
from appfigures.archive import ArchiveClient, ARCHIVE_BASE_URI

class ArchiveClientTest(unittest.TestCase):

    def setUp(self):
        self.result_service = MagicMock()
        self.report_type = "TEST_REPORT_TYPE"
        self.scope = "TEST_SCOPE"
        self.result_dict = { "Success": True }
        self.result_service.get_deserialized_result.return_value = self.result_dict
        self.client = ArchiveClient(self.result_service)


    def test_get_archive(self):
        args = (ARCHIVE_BASE_URI, self.scope)
        params = { "type": self.report_type }
        
        result = self.client.get_archive(self.scope, self.report_type)
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(args, params)
        
    def test_get_archive_with_no_scope(self):
        args = (ARCHIVE_BASE_URI,)
        params = { "type": self.report_type }
        
        result = self.client.get_archive(None, self.report_type)
        self.assertDictEqual(result, self.result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(args, params)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()