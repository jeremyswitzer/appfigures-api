from base import BaseClient

USERS_BASE_URI = "users"
PRODUCTS_COLLECTION = "products"
EXTERNAL_ACCOUNTS_COLLECTION = "external_accounts"

class UsersClient(BaseClient):
    
    def __init__(self, result_service, uri=USERS_BASE_URI):
        super(UsersClient, self).__init__(uri, result_service)
        
    def get_user_info(self, email, info_type=None):
        args = filter(None, (email, info_type))
        return self.get_response(args)