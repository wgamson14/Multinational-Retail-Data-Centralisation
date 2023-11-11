from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning


engine_1 = DatabaseConnector()
tables = DataExtractor()
cleaned = DataCleaning()

# EXTRACTING ------------------------------------------------------------------------------------------------------------------------

test = engine_1.init_db_engine()
tables.list_db_tables(test)
user_df = tables.read_rds_table('legacy_users', test)

card_df = tables.retrieve_pdf_data()

endpoint_1 = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
endpoint_2 = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/'
header_dict = {'x-api-Key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
num_stores = tables.list_number_of_stores(endpoint_1, header_dict)
store_df = tables.retrieve_stores_data(endpoint_2, header_dict)
store_df.to_csv('store_df.csv')

file_path = '/Users/willgamson/Desktop/Centralisation/products.csv'
bucket = 'data-handling-public'
object = 'products.csv'
products_df = tables.extract_from_s3(file_path, bucket, object)

orders_df = tables.read_rds_table('orders_table', test)

dates_file_path = '/Users/willgamson/Desktop/Centralisation/date_details.json'
dates_object = 'date_details.json'
dates_df = tables.extract_from_s3(dates_file_path,  bucket, dates_object)

# CLEANING ------------------------------------------------------------------------------------------------------------------------

cleaned_users = cleaned.clean_user_data(user_df)

cleaned_cards = cleaned.clean_card(card_df)

cleaned_stores = cleaned.clean_store_data()

almost_cleaned_products = cleaned.clean_products_data(products_df)
cleaned_products = cleaned.convert_product_weights(almost_cleaned_products)

cleaned_orders = cleaned.clean_orders_data(orders_df)

cleaned_dates = cleaned.clean_dates_data(dates_df)

# UPLOADING ------------------------------------------------------------------------------------------------------------------------

engine_1.upload_to_db(cleaned_users, 'dim_users')
engine_1.upload_to_db(cleaned_cards, 'dim_card_details')
engine_1.upload_to_db(cleaned_stores, 'dim_store_details')
engine_1.upload_to_db(cleaned_products, 'dim_products')
engine_1.upload_to_db(cleaned_orders, 'orders_table')
engine_1.upload_to_db(cleaned_dates, 'dim_date_times')