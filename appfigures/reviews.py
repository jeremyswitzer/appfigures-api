from base import BaseClient

REVIEWS_BASE_URI = "reviews"

class ReviewsClient(BaseClient):
    def __init__(self, result_service, uri=REVIEWS_BASE_URI):
        super(ReviewsClient, self).__init__(uri, result_service)

    def get_reviews(self, product_id, page, countries, **kwargs):
        args = (product_id, countries, page)
        return self.get_response(args, kwargs)
        