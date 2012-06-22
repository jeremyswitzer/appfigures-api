import unittest
from datetime import date
from mock import MagicMock
from appfigures.ranks import RanksClient, RANKS_BASE_URI


class RanksClietTest(unittest.TestCase):


    def setUp(self):
        self.base_url = "http://example.com"
        self.result_service = MagicMock()
        self.ranks_client = RanksClient(self.base_url, self.result_service)

    def test_get_ranks(self):
        result_dict = { 'test': 'test' }
        input_params = { 'param_one': ['test1', 1234], 'param_two_two': 'test2' }
        expected_params = { 'paramOne': 'test1;1234', 'paramTwoTwo': 'test2' }
        products = [1235, 44444, 1111]
        granularity = "Bi-quarterly"
        startdate = date(2012, 04, 1)
        enddate = date(2012, 05, 30)
        expected_uri = "{0}/{1}/{2}/{3}/{4}/{5}".format(self.base_url, RANKS_BASE_URI, 
                                                        "1235;44444;1111", granularity,
                                                        "2012-04-01", "2012-05-30")
        
        self.result_service.get_deserialized_result.return_value = result_dict
        
        result = self.ranks_client.get_ranks(products, granularity, startdate, enddate, **input_params)
        
        self.assertDictEqual(result, result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_uri, expected_params)


if __name__ == "__main__":
    unittest.main()