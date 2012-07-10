import unittest
from datetime import date
from mock import MagicMock
from appfigures.ranks import RanksClient, RANKS_BASE_URI


class RanksClietTest(unittest.TestCase):


    def setUp(self):
        self.result_service = MagicMock()
        self.ranks_client = RanksClient(self.result_service)

    def test_get_ranks(self):
        result_dict = { 'test': 'test' }
        expected_params = { 'param_one': ['test1', 1234], 'param_two_two': 'test2' }
        products = [1235, 44444, 1111]
        granularity = "Bi-quarterly"
        startdate = date(2012, 04, 1)
        enddate = date(2012, 05, 30)
        expected_args = (RANKS_BASE_URI, products, granularity, startdate, enddate)
        
        self.result_service.get_deserialized_result.return_value = result_dict
        
        result = self.ranks_client.get_ranks(products, granularity, startdate, enddate, **expected_params)
        
        self.assertDictEqual(result, result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, expected_params)


if __name__ == "__main__":
    unittest.main()