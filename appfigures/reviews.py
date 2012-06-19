from base import BaseClient

REVIEWS_BASE_URI = "reviews"

class ReviewsClient(BaseClient):
    def __init__(self, base_url, result_service, uri=REVIEWS_BASE_URI):
        super(ReviewsClient, self).__init__(base_url, uri, result_service)
        
    def get_reviews(self, product_id, page, countries, **kwargs):
        countries = self.format_to_string(countries)
        uri = self.construct_uri(product_id, countries, page)
        params = self.convert_params(**kwargs)
        result = self.get_response(uri, params)
        return result
    
    