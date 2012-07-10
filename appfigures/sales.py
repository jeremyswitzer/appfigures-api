from base import BaseClient

SALES_BASE_URI = "sales"

SALES_BY_PRODUCT = "products"
SALES_BY_DATE = "dates"
SALES_BY_COUNTRY = "countries"
SALES_BY_PRODUCT_AND_DATE = "products+dates"
SALES_BY_DATE_AND_PRODUCT = "dates+products"
SALES_BY_PRODUCT_AND_COUNTRY = "products+countries"
SALES_BY_COUNTRY_AND_PRODUCT = "countries+products"

class SalesClient(BaseClient):
    def __init__(self, result_service, uri=SALES_BASE_URI, **kwargs):
        super(SalesClient, self).__init__(uri, result_service)

    def get_sales_report(self, report_type, startdate, enddate, **kwargs):
        args = (report_type, startdate, enddate)
        result = self.get_response(args, kwargs)
        return result