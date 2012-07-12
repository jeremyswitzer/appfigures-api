from appfigures.base import BaseClient

EXTERNAL_ACCOUNTS_BASE_URI = "external_accounts"
ITUNES_CONNECT = "itunes_connect"
ANDROID_MARKET = "android_market"
GOOGLE_CHECKOUT = "google_checkout"

class ExternalAccountsClient(BaseClient):


    def __init__(self, result_service, uri=EXTERNAL_ACCOUNTS_BASE_URI):
        super(ExternalAccountsClient, self).__init__(uri, result_service)
        
    def get_external_account(self, account_id=None):
        args = (account_id,) if account_id else ()
        return self.get_response(args)
    
    def create_external_account(self, nickname, username, password, auto_import, account_type):
        args = ()
        params = self._create_params(nickname, username, password, auto_import, account_type)
        return self.create_item(args, params)
    
    def update_external_account(self, account_id, nickname, username, password, auto_import, account_type):
        args = (account_id,)
        params = self._create_params(nickname, username, password, auto_import, account_type)
        return self.update_item(args, params)
    
    def delete_external_account(self, account_id):
        args = (account_id,)
        return self.delete_item(args)
    
    def _create_params(self, nickname, username, password, auto_import, account_type):
        params = {
            "nickname": nickname,
            "username": username,
            "password": password,
            "auto_import": auto_import,
            "type": account_type
        }
        
        return params
        