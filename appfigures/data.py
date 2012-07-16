from base import BaseClient

DATA_BASE_URI = "data"

CATEGORIES_DATA = "categories"
COUNTRIES_DATA = "countries"
LANGUAGES_DATA = "languages"
CURRENCIES_DATA = "currencies"

APPLE_STORE_ID = "apple"

class DataClient(BaseClient):

    def __init__(self, result_client, uri=DATA_BASE_URI):
        super(DataClient, self).__init__(uri, result_client)
        
    def get_data(self, data_type, *other_args):
        args = (data_type,) + other_args
        return self.get_response(args)
        