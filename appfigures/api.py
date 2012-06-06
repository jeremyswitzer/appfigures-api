import sales
from reviews import ReviewsClient
from events import EventsClient
from services import create_default_result_service as create_rs


PODIO_API_URL_1_1 = "https://api.appfigures.com/v1.1/"

DATASOURCE_DAILY = "daily"
DATASOURCE_WEEKLY = "weekly"
DATASOURCE_MONTHLY = "monthly"

class Client:
    
    _client_settings = {
        '_sales': ('sales_client', sales.SalesClient),
        '_reviews': ('reviews_client', ReviewsClient),
        '_events': ('events_client', EventsClient)
    }
    
    def __init__(self, user, password, base_url=PODIO_API_URL_1_1, **kwargs):
        result_service = kwargs.get("result_service", create_rs(user, password))
        self._init_api_clients(base_url, result_service, kwargs)
    
    #Sales API
    def get_sales_report_by_product(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by product. Returns a dict with product numbers as keys.
        
        Args:
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthy) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            product_ids -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_PRODUCT, startdate, enddate, **kwargs)
    
    def get_sales_report_by_date(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by date. Returns a dict with date strings as keys.
        
        Args:
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            product_ids -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_DATE, startdate, enddate, **kwargs)
    
    def get_sales_report_by_country(self, startdate=None, enddate=None, **kwargs):  
        """Get sales report grouped by country. Returns a dict with country names as keys.
        
        Args:
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            product_ids -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_COUNTRY, startdate, enddate, **kwargs)
    
    def get_sales_report_by_product_and_date(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by product then date. Returns a dict with product numbers as keys. Each product has a dict with date strings as keys
        
        Args:
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            product_ids -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_PRODUCT_AND_DATE, startdate, enddate, **kwargs)
    
    def get_sales_report_by_date_and_product(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by date then product. Returns a dict with date strings as keys. Each product has a dict with product numbers as keys
        
        Args:
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            product_ids -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_DATE_AND_PRODUCT, startdate, enddate, **kwargs)
    
    def get_sales_report_by_product_and_country(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by product then country. Returns a dict with product numbers as keys. Each product has a dict with country names as keys
        
        Args:
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            product_ids -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
            country -- (isoCode) Country to limit the report to.
        
        """
        
        return self._sales.get_sales_report(sales.SALES_BY_PRODUCT_AND_COUNTRY, startdate, enddate, **kwargs)

    def get_sales_report_by_country_and_product(self, startdate=None, enddate=None, **kwargs):
        """Get sales report grouped by country then product. Returns a dict with country names as keys. Each product has a dict with product numbers as keys
        
        Args:
            startdate -- Report start date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc.
            enddate -- Report end date. Date object or string in "yyyy-MM-dd" format. Will also accept "today," "tomorrow," "yesterday," etc. 
            
        Keyword arguments:
            data_source -- (daily,weekly,monthly) Whether to use daily or weekly reports. Monthly used for financial reports. (default: daily)
            product_ids -- [product_id1,product_id2,product_id3...] List of specific products to include in the response.
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
            event_date -- Date object or string in "yyyy-MM-dd" format. Date for the event
            products -- List. Product Id(s) related to the event. The constant ALL_PRODUCTS will assume all products related to the account.
        """
        return self._events.create_event(caption, event_date, products)
    
    def update_event(self, event_id, caption, event_date, products):
        """Update info for an existing event. The call returns the updated event object
        
        Args:
            event_id -- Number. The Id of the event to update.
            caption -- String. The caption of the event.
            event_date -- Date object or string in "yyyy-MM-dd" format. Date for the event
            products -- List. Product Id(s) related to the event. The constant ALL_PRODUCTS will assume all products related to the account.
        """
        return self._events.update_event(event_id, caption, event_date, products)
    
    def delete_event(self, event_id):
        """Delete an existing event.
        
        Args:
            event_id -- Number. The Id of the event to delete.
        """
        return self._events.delete_event(event_id)
    
    
    
    def _init_api_clients(self, base_url, result_service, overrides):
        for p,s in self._client_settings.iteritems():
            setattr(self, p, overrides.get(s[0], s[1](base_url, result_service)))
    