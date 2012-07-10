import unittest
from mock import MagicMock
from appfigures.reviews import ReviewsClient, REVIEWS_BASE_URI


class ReviewsClientTest(unittest.TestCase):
    
    def setUp(self):
        self.base_url = "http://example.com"
        self.result_service = MagicMock()
        self.reviews_client = ReviewsClient(self.result_service)

    def test_get_latest_reviews_for_usa(self):
        result_dict = { 'test': 'test' }
        expected_params = { 'paramOne': 'test2', 'paramTwoTwo': 'test2' }
        page = 0
        productid = 100000
        country = "US"
        expected_args = (REVIEWS_BASE_URI, productid, country, page)
        
        self.result_service.get_deserialized_result.return_value = result_dict
        
        result = self.reviews_client.get_reviews(productid, page, country, **expected_params)
        
        self.assertDictEqual(result, result_dict)
        self.result_service.get_deserialized_result.assert_called_once_with(expected_args, expected_params)
        

if __name__ == "__main__":
    unittest.main()