import unittest
from appfigures.reviews import ReviewsClient
from appfigures.api import PODIO_API_URL_1_1


class ReviewsClientTest(unittest.TestCase):
    
    def setUp(self):
        self._reviews = ReviewsClient("<test_user>", "<test_password>", PODIO_API_URL_1_1)

    def test_get_latest_reviews(self):
        reviews = self._reviews.get_reviews("<product_id>", 0, "US")
        self.assertIsNotNone(reviews)
        print reviews
        

if __name__ == "__main__":
    unittest.main()