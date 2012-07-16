import unittest
from appfigures.api import Client
from datetime import date
from mock import MagicMock


class ApiClientTest(unittest.TestCase):


    def setUp(self):
        self.client_mock = MagicMock()
        cm = self.client_mock
        self.client_overrides = {
            "result_service": cm,
            "sales_client": cm,
            "reviews_client": cm,
            "events_client": cm,
            "ranks_client": cm,
            "iads_client": cm,
            "users_client": cm,
            "external_accounts_client": cm,
            "data_client": cm
        }
        self.api_client = Client("test", "test", **self.client_overrides)
        self.result_dict = { "Success": True }
        self.startdate = date(2012, 1, 1)
        self.enddate = date(2012, 2, 2)
        self.mock_id = 111111
        self.mock_string = "Test String"
        self.mock_list = [11111, 22222, 33333]
        self.email = u"testing@appfigures.com"
        self.password = "abc123"
        self.flag = True

    def test_get_sales_report_by_product(self):
        from appfigures.sales import SALES_BY_PRODUCT as datasource
        
        self.client_mock.get_sales_report.return_value = self.result_dict
        
        result = self.api_client.get_sales_report_by_product(self.startdate, 
                                                             self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_sales_report.assert_called_once_with(datasource, 
                                                                  self.startdate, 
                                                                  self.enddate)
        
    def test_get_sales_report_by_date(self):
        from appfigures.sales import SALES_BY_DATE as datasource
        
        self.client_mock.get_sales_report.return_value = self.result_dict
        
        result = self.api_client.get_sales_report_by_date(self.startdate, self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_sales_report.assert_called_once_with(datasource, 
                                                                  self.startdate, 
                                                                  self.enddate)
        
    def test_get_sales_report_by_country(self):
        from appfigures.sales import SALES_BY_COUNTRY as datasource
        
        self.client_mock.get_sales_report.return_value = self.result_dict
        
        result = self.api_client.get_sales_report_by_country(self.startdate, self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_sales_report.assert_called_once_with(datasource, 
                                                                  self.startdate, 
                                                                  self.enddate)
    
    def test_get_sales_report_by_product_and_date(self):
        from appfigures.sales import SALES_BY_PRODUCT_AND_DATE as datasource
        
        self.client_mock.get_sales_report.return_value = self.result_dict
        
        result = self.api_client.get_sales_report_by_product_and_date(self.startdate, 
                                                                      self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_sales_report.assert_called_once_with(datasource, 
                                                                  self.startdate, 
                                                                  self.enddate)
        
    def test_get_sales_report_by_date_and_product(self):
        from appfigures.sales import SALES_BY_DATE_AND_PRODUCT as datasource
        
        self.client_mock.get_sales_report.return_value = self.result_dict
        
        result = self.api_client.get_sales_report_by_date_and_product(self.startdate, 
                                                                      self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_sales_report.assert_called_once_with(datasource, 
                                                                  self.startdate, 
                                                                  self.enddate)
        
    def test_get_sales_report_by_product_and_country(self):
        from appfigures.sales import SALES_BY_PRODUCT_AND_COUNTRY as datasource
        
        self.client_mock.get_sales_report.return_value = self.result_dict
        
        result = self.api_client.get_sales_report_by_product_and_country(self.startdate, 
                                                                         self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_sales_report.assert_called_once_with(datasource, 
                                                                  self.startdate, 
                                                                  self.enddate)
        
    def test_get_sales_report_by_country_and_product(self):
        from appfigures.sales import SALES_BY_COUNTRY_AND_PRODUCT as datasource
        
        self.client_mock.get_sales_report.return_value = self.result_dict
        
        result = self.api_client.get_sales_report_by_country_and_product(self.startdate, 
                                                                         self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_sales_report.assert_called_once_with(datasource, 
                                                                  self.startdate, 
                                                                  self.enddate)
        
    def test_get_reviews_for_product_by_page(self):
        #TODO: Fix API not to have a country default
        page = 0
        countries = 'major'
        
        self.client_mock.get_reviews.return_value = self.result_dict
        result = self.api_client.get_reviews_for_product_by_page(self.mock_id, page)
        
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_reviews.assert_called_once_with(self.mock_id, page, countries)
        
    def test_get_all_events(self):
        self.client_mock.get_events.return_value = self.result_dict
        
        result = self.api_client.get_all_events()
        
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_events.assert_called_once_with()
        
    def test_create_new_event(self):
        self.client_mock.create_event.return_value = self.result_dict
        
        result = self.api_client.create_new_event(self.mock_string, 
                                                  self.startdate, 
                                                  self.mock_list)
        
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.create_event.assert_called_once_with(self.mock_string, 
                                                              self.startdate, 
                                                              self.mock_list)
        
    def test_update_event(self):
        self.client_mock.update_event.return_value = self.result_dict
        
        result = self.api_client.update_event(self.mock_id, self.mock_string, 
                                              self.startdate, self.mock_list)
        
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.update_event.assert_called_once_with(self.mock_id, self.mock_string, 
                                                              self.startdate, self.mock_list)
        
    
    def test_delete_event(self):
        self.client_mock.delete_event.return_value = True
        
        result = self.api_client.delete_event(self.mock_id)
        
        self.assertTrue(result)
        self.client_mock.delete_event.assert_called_once_with(self.mock_id)
        
    
    def test_get_hourly_ranks(self):
        from appfigures.api import DATASOURCE_HOURLY as datasource
        
        self.client_mock.get_ranks.return_value = self.result_dict
        
        result = self.api_client.get_hourly_ranks(self.mock_list, self.startdate, self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_ranks.assert_called_once_with(self.mock_list, datasource, 
                                                           self.startdate, self.enddate)
        
    def test_get_daily_ranks(self):
        from appfigures.api import DATASOURCE_DAILY as datasource
        
        self.client_mock.get_ranks.return_value = self.result_dict
        
        result = self.api_client.get_daily_ranks(self.mock_list, self.startdate, self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_ranks.assert_called_once_with(self.mock_list, datasource, 
                                                           self.startdate, self.enddate)
        
    def test_get_iads_by_day(self):
        from appfigures.iads import IADS_BY_DAY as report_type
        
        self.client_mock.get_iads.return_value = self.result_dict
        
        result = self.api_client.get_iads_by_day(self.startdate, self.enddate, 
                                                 products=self.mock_list)
        
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_iads.assert_called_once_with(report_type, self.startdate, 
                                                          self.enddate, products=self.mock_list)
        
    def test_get_iads_by_country(self):
        from appfigures.iads import IADS_BY_COUNTRY as report_type
        
        self.client_mock.get_iads.return_value = self.result_dict
        
        result = self.api_client.get_iads_by_country(self.startdate, self.enddate)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_iads.assert_called_once_with(report_type, self.startdate, self.enddate)
        
        
    def test_get_user_details(self):
        self.client_mock.get_user_info.return_value = self.result_dict
        
        result = self.api_client.get_user_details(self.email)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_user_info.assert_called_once_with(self.email)
        
    def test_get_user_products(self):
        from appfigures.users import USERS_PRODUCTS as info_type
        
        self.client_mock.get_user_info.return_value = self.result_dict
        
        result = self.api_client.get_user_products(self.email)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_user_info.assert_called_once_with(self.email, info_type)
        
    def test_get_user_external_accounts(self):
        from appfigures.users import USERS_EXTERNAL_ACCOUNTS as info_type
        
        self.client_mock.get_user_info.return_value = self.result_dict
        
        result = self.api_client.get_user_external_accounts(self.email)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_user_info.assert_called_once_with(self.email, info_type)
        
    def test_get_all_external_accounts(self):
        self.client_mock.get_external_account.return_value = self.result_dict
        
        result = self.api_client.get_all_external_accounts()
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_external_account.assert_called_once_with()
        
    def test_get_external_account(self):
        self.client_mock.get_external_account.return_value = self.result_dict
        
        result = self.api_client.get_external_account(self.mock_id)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_external_account.assert_called_once_with(self.mock_id)
        
    def test_create_external_account(self):
        from appfigures.external_accounts import ITUNES_CONNECT as account_type
        
        self.client_mock.create_external_account.return_value = self.result_dict
        args = (self.mock_string, self.email, self.password, self.flag, account_type)
        
        result = self.api_client.create_external_account(*args)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.create_external_account.assert_called_once_with(*args)
        
    def test_update_external_account(self):
        from appfigures.external_accounts import ANDROID_MARKET as account_type

        self.client_mock.update_external_account.return_value = self.result_dict
        args = (self.mock_id, self.mock_string, self.email, self.password, self.flag, account_type)
        
        result = self.api_client.update_external_account(*args)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.update_external_account.assert_called_once_with(*args)
        
    def test_delete_external_account(self):
        self.client_mock.delete_external_account.return_value = self.result_dict
        
        result = self.api_client.delete_external_account(self.mock_id)
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.delete_external_account.assert_called_once_with(self.mock_id)
        
    def test_get_categories(self):
        from appfigures.data import CATEGORIES_DATA as data_type
        
        self.client_mock.get_data.return_value = self.result_dict
        
        result = self.api_client.get_categories()
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_data.assert_called_once_with(data_type)
        
    def test_get_currencies(self):
        from appfigures.data import CURRENCIES_DATA as data_type
        
        self.client_mock.get_data.return_value = self.result_dict
        
        result = self.api_client.get_currencies()
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_data.assert_called_once_with(data_type)
        
    def test_get_languages(self):
        from appfigures.data import LANGUAGES_DATA as data_type
        
        self.client_mock.get_data.return_value = self.result_dict
        
        result = self.api_client.get_languages()
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_data.assert_called_once_with(data_type)
        
    def test_get_countries(self):
        from appfigures.data import COUNTRIES_DATA as data_type
        
        self.client_mock.get_data.return_value = self.result_dict
        
        result = self.api_client.get_countries()
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_data.assert_called_once_with(data_type)
        
    def test_get_apple_stores(self):
        from appfigures.data import APPLE_STORE_ID, COUNTRIES_DATA as data_type
        
        self.client_mock.get_data.return_value = self.result_dict
        
        result = self.api_client.get_apple_stores()
        self.assertDictEqual(result, self.result_dict)
        self.client_mock.get_data.assert_called_once_with(data_type, APPLE_STORE_ID)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()