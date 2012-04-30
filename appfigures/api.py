from sales import SalesClient

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
    
    #Sales API
    def get_sales_report_by_product(self, startdate=None, enddate=None, **kwargs):
        return self._sales.get_sales_report("products", startdate, enddate, **kwargs)
    
    def get_sales_report_by_date(self, startdate=None, enddate=None, **kwargs):
        return self._sales.get_sales_report("dates", startdate, enddate, **kwargs)
    
    def get_sales_report_by_country(self, startdate=None, enddate=None, **kwargs):
        return self._sales.get_sales_report("countries", startdate, enddate, **kwargs)
    
    def get_sales_report_by_product_and_date(self, startdate=None, enddate=None, **kwargs):
        return self._sales.get_sales_report("products+dates", startdate, enddate, **kwargs)
    
    def get_sales_report_by_date_and_product(self, startdate=None, enddate=None, **kwargs):
        return self._sales.get_sales_report("dates+products", startdate, enddate, **kwargs)
    
    def get_sales_report_by_product_and_country(self, startdate=None, enddate=None, **kwargs):
        return self._sales.get_sales_report("products+countries", startdate, enddate, **kwargs)

    def get_sales_report_by_country_and_product(self, startdate=None, enddate=None, **kwargs):
        return self._sales.get_sales_report("countries+products", startdate, enddate, **kwargs)