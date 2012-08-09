import sales
from reviews import ReviewsClient
from events import EventsClient
from ranks import RanksClient
from iads import iAdsClient, IADS_BY_DAY, IADS_BY_COUNTRY
from users import UsersClient, USERS_PRODUCTS, USERS_EXTERNAL_ACCOUNTS
from external_accounts import ExternalAccountsClient
from data import DataClient, CATEGORIES_DATA, COUNTRIES_DATA, CURRENCIES_DATA, \
                 LANGUAGES_DATA, APPLE_STORE_ID
from archive import ArchiveClient, LATEST_ARCHIVE_REPORTS, ALL_ARCHIVE_REPORTS, \
                    ALL_REPORT_TYPE
from services import create_default_result_service as create_rs


PODIO_API_URL_1_1 = "https://api.appfigures.com/v1.1"

DATASOURCE_HOURLY = "hourly"
DATASOURCE_DAILY = "daily"
DATASOURCE_WEEKLY = "weekly"
DATASOURCE_MONTHLY = "monthly"

TIMEZONE_USER = "user"
TIMEZONE_UTC = "utc"
TIMEZONE_EST = "est"

class Client:
    
    _client_settings = {
        '_sales': ('sales_client', sales.SalesClient),
        '_reviews': ('reviews_client', ReviewsClient),
        '_events': ('events_client', EventsClient),
        '_ranks': ('ranks_client', RanksClient),
        '_iads': ('iads_client', iAdsClient),
        '_users': ('users_client', UsersClient),
        '_external_accounts': ('external_accounts_client', ExternalAccountsClient),
        '_data': ('data_client', DataClient),
        '_archive': ('archive_client', ArchiveClient)
    }
    
    def __init__(self, user, password, base_url=PODIO_API_URL_1_1, **kwargs):
        result_service = kwargs.get("result_service", create_rs(user, password, base_url))
        self._init_api_clients(result_service, kwargs)
    
    #Sales API
    def get_sales_report_by_product(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by product. Returns a dict with product numbers as keys.
        
        Args:
            startdate -- Date object. Report start date.
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthy) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_PRODUCT, startdate, enddate, **kwargs)
    
    def get_sales_report_by_date(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by date. Returns a dict with date strings as keys.
        
        Args:
            startdate -- Date object. Report start date.
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_DATE, startdate, enddate, **kwargs)
    
    def get_sales_report_by_country(self, startdate=None, enddate=None, **kwargs):  
        """Get sales report grouped by country. Returns a dict with country names as keys.
        
        Args:
            startdate -- Date object. Report start date.
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_COUNTRY, startdate, enddate, **kwargs)
    
    def get_sales_report_by_product_and_date(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by product then date. Returns a dict with product numbers as keys. Each product has a dict with date strings as keys
        
        Args:
            startdate -- Date object. Report start date.
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_PRODUCT_AND_DATE, startdate, enddate, **kwargs)
    
    def get_sales_report_by_date_and_product(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by date then product. Returns a dict with date strings as keys. Each product has a dict with product numbers as keys
        
        Args:
            startdate -- Date object. Report start date.
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_DATE_AND_PRODUCT, startdate, enddate, **kwargs)
    
    def get_sales_report_by_product_and_country(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by product then country. Returns a dict with product numbers as keys. Each product has a dict with country names as keys
        
        Args:
            startdate -- Date object. Report start date.
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_PRODUCT_AND_COUNTRY, startdate, enddate, **kwargs)

    def get_sales_report_by_country_and_product(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by country then product. Returns a dict with country names as keys. Each product has a dict with product numbers as keys
        
        Args:
            startdate -- Date object. Report start date.
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_COUNTRY_AND_PRODUCT, startdate, enddate, **kwargs)
    
    #Reviews API
    def get_reviews_for_product_by_page(self, product_id, page, countries='major', **kwargs):
        """Get reviews for a single product grouped by country. Reviews can only be retrieved a day at a time.
        
        Args:
            product_id -- Number. id of app to pull reviews for.
            page -- Number. zero-based page number, truncated to highest possible value if it is higher than available pages
            countries -- Number, String, or List. Id or short-code of the country or countries to pull reviews from. "major" selects all high-volume countries. "minor" selects smaller countries. Android Market does not provide reviews by country
            
        Keyword arguments:
            language (optional) -- short code of language to translate reviews into (You can get supported languages via DataClient)
        
        """
        
        return self._reviews.get_reviews(product_id, page, countries, **kwargs)
    
    # Events API
    def get_all_events(self):
        """Get a list of all events. Events come in a dictionary with the event ID as the key."""
        
        return self._events.get_events()
    
    def create_new_event(self, caption, event_date, products):
        """Create a new event. The call returns the newly created event object.
        
        Args:
            caption -- String. The caption of the event.
            event_date -- Date object. Date for the event
            products -- List. Product Id(s) related to the event. The constant ALL_PRODUCTS will assume all products related to the account.
        """
        return self._events.create_event(caption, event_date, products)
    
    def update_event(self, event_id, caption, event_date, products):
        """Update info for an existing event. The call returns the updated event object
        
        Args:
            event_id -- Number. The Id of the event to update.
            caption -- String. The caption of the event.
            event_date -- Date object. Date for the event
            products -- List. Product Id(s) related to the event. The constant ALL_PRODUCTS will assume all products related to the account.
        """
        return self._events.update_event(event_id, caption, event_date, products)
    
    def delete_event(self, event_id):
        """Delete an existing event.
        
        Args:
            event_id -- Number. The Id of the event to delete.
        """
        return self._events.delete_event(event_id)
    
    #Ranks API
    def get_hourly_ranks(self, products, startdate, enddate, **kwargs):
        """Generate a Ranks Report by the hour.
        
        Args:
            products -- List. The product ID(s) to get ranks data for.
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format.            
        Keyword arguments:
            countries (optional) -- List of countryId or isoCode. Countries to run report on. (default: US)
            tz (optional) -- String. (user | utc | est) specifies which timezone to use. (default: est)
            filter (optional) -- Number (1 - 400). Top N ranks. A filter value of 100 will only show records where the rank position is better than 100. (default: 100)
        """
        return self._ranks.get_ranks(products, DATASOURCE_HOURLY, startdate, enddate, **kwargs)
    
    def get_daily_ranks(self, products, startdate, enddate, **kwargs):
        """Generate a Ranks Report by the day.
        
        Args:
            products -- List. The product ID(s) to get ranks data for.
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format.            
        Keyword arguments:
            countries (optional) -- List of countryId or isoCode. Countries to run report on. (default: US)
            tz (optional) -- String. (user | utc | est) specifies which timezone to use. (default: est)
            filter (optional) -- Number (1 - 400). Top N ranks. A filter value of 100 will only show records where the rank position is better than 100. (default: 100)
        """
        return self._ranks.get_ranks(products, DATASOURCE_DAILY, startdate, enddate, **kwargs)
    
    #iAds API
    def get_iads_by_day(self, startdate, enddate, **kwargs):
        """Get detail iAds data grouped by day.
        
        Args:
            startdate -- Date object. Report start date. 
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
        """
        
        return self._iads.get_iads(IADS_BY_DAY, startdate, enddate, **kwargs)
    
    def get_iads_by_country(self, startdate, enddate, **kwargs):
        """Get detail iAds data grouped by country.
        
        Args:
            startdate -- Date object. Report start date. 
            enddate -- Date object. Report end date. 
            
        Keyword arguments:
            products -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
        """
        return self._iads.get_iads(IADS_BY_COUNTRY, startdate, enddate, **kwargs)
    
    
    #Users API
    def get_user_details(self, email):
        """Get details for a user.
        
        Args:
            email -- String. The users email address. 
        """
        return self._users.get_user_info(email)
    
    def get_user_products(self, email):
        """Get a list of the user's products.
        
        Args:
            email -- String. The user's email address. 
        """
        return self._users.get_user_info(email, USERS_PRODUCTS)
    
    def get_user_external_accounts(self, email):
        """Get a list of the user's external accounts.
        
        Args:
            email -- String. The user's email address. 
        """
        return self._users.get_user_info(email, USERS_EXTERNAL_ACCOUNTS)
    
    
    #External Accounts API
    def get_all_external_accounts(self):
        """List existing external accounts."""
        
        return self._external_accounts.get_external_account()
    
    def get_external_account(self, account_id):
        """Get a single external account by account ID.
        
        Args:
            account_id -- Number. The ID of the external account.
        """
        return self._external_accounts.get_external_account(account_id)
    
    def create_external_account(self, nickname, username, 
                                password, auto_import, account_type):
        """Create a new external account.
        
        Args:
            nickname -- String. A friendly name for the account.
            username -- String. The username associated with the App Store.
            password -- String. The password for the App Store account.
            auto_import -- Boolean. Flag to have this account import reports automatically.
            account_type -- String. The type of account being linked. Options: itunes_connect, android_market, google_checkout     
        """
        return self._external_accounts.create_external_account(nickname, username, 
                                                               password, auto_import, account_type)
    
    def update_external_account(self, account_id, nickname, username, 
                                password, auto_import, account_type):
        """Update and existing external account.
        
        Args:
            account_id -- Number. The ID of the external account.
            nickname -- String. A friendly name for the account.
            username -- String. The username associated with the App Store.
            password -- String. The password for the App Store account.
            auto_import -- Boolean. Flag to have this account import reports automatically.
            account_type -- String. The type of account being linked. Options: itunes_connect, android_market, google_checkout     
        """
        return self._external_accounts.update_external_account(account_id, nickname, username, 
                                                               password, auto_import, account_type)
    
    def delete_external_account(self, account_id):
        """Delete an external account reference.
        
        Args:
            account_id -- Number. The ID of the external account.
        """
        return self._external_accounts.delete_external_account(account_id)
    
    
    #Data API
    def get_categories(self):
        """List all App Store categories."""
        return self._data.get_data(CATEGORIES_DATA)
    
    def get_languages(self):
        """Listing supported languages for review translation."""
        return self._data.get_data(LANGUAGES_DATA)
    
    def get_currencies(self):
        """Listing supported currencies. Returns a list."""
        return self._data.get_data(CURRENCIES_DATA)
    
    def get_countries(self):
        """Listing available countries. Returns dict keyed by ISO."""
        return self._data.get_data(COUNTRIES_DATA)
    
    def get_apple_stores(self):
        """Listing available Apple App Stores. Returns dict keyed by Apple's identifier."""
        return self._data.get_data(COUNTRIES_DATA, APPLE_STORE_ID)
    
    
    #Archive API
    def get_all_archived_reports(self, report_type=ALL_REPORT_TYPE):
        """Get all archived reports. At this time reports are 
        only available for Apple apps (via iTunes Connect).
        
        Args:
            report_type: (Optional) String. The report type to limit to. Supported values: daily, weekly, financial, payment, all. The default type is all
        """
        return self._archive.get_archive(ALL_ARCHIVE_REPORTS, report_type)
    
    def get_latest_archived_reports(self, report_type=ALL_REPORT_TYPE):
        """Get latest archived reports. At this time reports are 
        only available for Apple apps (via iTunes Connect).
        
        Args:
            report_type: (Optional) String. The report type to limit to. Supported values: daily, weekly, financial, payment, all. The default type is all
        """
        return self._archive.get_archive(LATEST_ARCHIVE_REPORTS, report_type)
    
    def get_archived_reports_for_date(self, report_date, report_type=ALL_REPORT_TYPE):
        """Get archived report by date. At this time reports are 
        only available for Apple apps (via iTunes Connect).
        
        Args:
            report_date: Date. Retrieves the headers for all reports on the given date.
            report_type: (Optional) String. The report type to limit to. Supported values: daily, weekly, financial, payment, all. The default type is all
        """
        return self._archive.get_archive(report_date, report_type)
    
    
    def _init_api_clients(self, result_service, overrides):
        for p,s in self._client_settings.iteritems():
            setattr(self, p, overrides.get(s[0], s[1](result_service)))
    