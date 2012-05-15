from sales import SalesClient
from reviews import ReviewsClient

PODIO_API_URL_1_1 = "https://api.appfigures.com/v1.1/"

class Client():
    
    DATASOURCE_DAILY = "daily"
    DATASOURCE_WEEKLY = "weekly"
    DATASOURCE_MONTHLY = "monthly"
    
    def __init__(self, user, password, base_url=PODIO_API_URL_1_1):
        self._user = user
        self._password = password
        self._base_url = base_url
        self._sales = SalesClient(user, password, base_url)
        self._reviews = ReviewsClient(user, password, base_url)
    
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
        
        return self._sales.get_sales_report("products", startdate, enddate, **kwargs)
    
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
        
        return self._sales.get_sales_report("dates", startdate, enddate, **kwargs)
    
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
        
        return self._sales.get_sales_report("countries", startdate, enddate, **kwargs)
    
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
        
        return self._sales.get_sales_report("products+dates", startdate, enddate, **kwargs)
    
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
        
        return self._sales.get_sales_report("dates+products", startdate, enddate, **kwargs)
    
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
        
        return self._sales.get_sales_report("products+countries", startdate, enddate, **kwargs)

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
        
        return self._sales.get_sales_report("countries+products", startdate, enddate, **kwargs)
    
    #Reviews API
    def get_reviews_for_product_by_page(self, product_id, page, countries='major', **kwargs):
        """Get reviews for a single product grouped by country. Reviews can only be retrieved a day at a time.
        
        Args:
            product_id -- Number. id of app to pull reviews for.
            page -- Number. zero-based page number, truncated to highest possible value if it is higher than available pages
            countries -- Number, String, or List. Id or short-code of the country or countries to pull reviews from. "Major" selects all high-volume countries. "Minor" selects smaller countries. Android Market does not provide reviews by country
            
        Keyword arguments:
            language (optional) -- short code of language to translate reviews into (You can get supported languages via DataClient)
        
        """
        
        return self._reviews.get_reviews(product_id, page, countries, **kwargs)
    
    
    
    