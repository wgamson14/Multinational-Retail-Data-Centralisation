import pandas as pd
import numpy as np

class DataCleaning:
    def clean_user_data(self, user_df):
        self.user_df = user_df
        self.user_df['date_of_birth'] = self.user_df['date_of_birth'].apply(pd.to_datetime, errors='ignore')
        self.user_df['join_date'] = self.user_df['join_date'].apply(pd.to_datetime, errors='ignore')
        self.user_df['country_code'] = self.user_df['country_code'].str.replace('GGB', 'GB', regex=False)
        self.user_df = self.user_df.drop(self.user_df[self.user_df['country_code'] == 'NULL'].index)
        self.user_df = self.user_df[self.user_df['country_code'].isin(['DE', 'GB', 'US'])]

        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace('+49', '0', regex=False)
        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace('+44', '0', regex=False)
        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace('+1', '0', regex=False)
        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace('(0)', '', regex=False)
        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace('(', '', regex=False)
        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace(')', '', regex=False)
        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace('-', '', regex=False)
        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace(' ', '', regex=False)
        self.user_df['phone_number'] = self.user_df['phone_number'].str.replace('.', '', regex=False)

        self.user_df = self.user_df.reset_index(drop=True)
        self.user_df = self.user_df.drop(columns=['index'])
        
        return self.user_df
    
    def clean_card(self, card_df):
        self.card_df = card_df
        self.card_df = self.card_df.reset_index(drop=True)
        self.card_df = self.card_df.drop(self.card_df[self.card_df['card_provider'] == 'NULL'].index)
        providers = ['Diners Club / Carte Blanche', 'American Express', 'JCB 16 digit', 'JCB 15 digit', 'Mastercard', 'Discover', 'Maestro', 'VISA 19 digit',
        'VISA 16 digit', 'VISA 13 digit']
        self.card_df = self.card_df[self.card_df['card_provider'].isin(providers)]

        self.card_df['date_payment_confirmed'] = self.card_df['date_payment_confirmed'].apply(pd.to_datetime, errors='ignore')
        self.card_df['card_number'] = pd.to_numeric(self.card_df['card_number'], errors='coerce')
        self.card_df = self.card_df.dropna()
        self.card_df['card_number'] = self.card_df['card_number'].astype(int)

        self.card_df.loc[:,'expiry_date'] = self.card_df.loc[:,'expiry_date'].apply(pd.to_datetime, format='%m/%y', errors='coerce')

        return self.card_df

    def clean_store_data(self):
        self.store_df = pd.read_csv('store_df.csv')

        self.store_df = self.store_df.set_index(['index'])

        self.store_df['continent'] = self.store_df['continent'].str.replace('eeEurope', 'Europe', regex=False)
        self.store_df['continent'] = self.store_df['continent'].str.replace('eeAmerica', 'America', regex=False)
        self.store_df = self.store_df[self.store_df['continent'].isin(['Europe', 'America'])]

        self.store_df['opening_date'] = self.store_df['opening_date'].apply(pd.to_datetime, errors='ignore')
        self.store_df['longitude'] = pd.to_numeric(self.store_df['longitude'], errors='coerce')
        self.store_df['latitude'] = pd.to_numeric(self.store_df['latitude'], errors='coerce')

        self.store_df['staff_numbers'] = self.store_df['staff_numbers'].replace({r'J': '', r'e': '', r'R': '', r'A': '', r'n': ''}, regex=True)
        self.store_df['staff_numbers'] = self.store_df['staff_numbers'].astype('int64')

        self.store_df = self.store_df.drop(columns=['lat'])

        return self.store_df

    def clean_products_data(self, products_df):
        self.products_df = products_df
        self.products_df = pd.read_csv('products.csv')
        self.products_df = self.products_df.rename(columns={'Unnamed: 0': 'index'})
        self.products_df = self.products_df.rename(columns={'EAN': 'ean'})
        self.products_df = self.products_df.set_index(['index'])
        self.products_df['date_added'] = self.products_df['date_added'].apply(pd.to_datetime, errors='ignore')
        self.categories = ['toys-and-games', 'sports-and-leisure', 'pets', 'homeware', 'health-and-beauty', 'food-and-drink', 'diy']
        self.products_df = self.products_df[self.products_df['category'].isin(self.categories)]

        return self.products_df

    def convert_product_weights(self, final_product_df):
        self.final_product_df = final_product_df

        self.final_product_df['in_kg'] = self.final_product_df['weight'].str.contains('kg')
        self.final_product_df['weight_units'] = np.where(self.final_product_df['weight'].str.contains('kg'), 'kg', 'not in kg')

        self.final_product_df['weight'] = self.final_product_df['weight'].replace({'16oz': '0.454', '77g .': '77g'})
        self.final_product_df['weight'] = self.final_product_df['weight'].replace({r'kg': '', r'g': '', r'ml': ''}, regex=True)
        self.final_product_df['weight'] = self.final_product_df['weight'].replace({r'12 x 100': '1200', r'8 x 150': '1200', r'6 x 412': '2472', r'6 x 400': '2400', r'8 x 85': '680', r'40 x 100': '4000', r'12 x 85': '1020', r'3 x 2': '6', r'3 x 90': '270', r'16 x 10': '160', r'3 x 132': '396', r'5 x 145': '725', r'4 x 400': '1600', r'2 x 200': '400'})
        self.final_product_df['weight'] = pd.to_numeric(self.final_product_df['weight'], errors='coerce')

        self.final_product_df['weight'] = np.where(self.final_product_df['weight_units'] == 'not in kg', self.final_product_df['weight'] / 1000, self.final_product_df['weight'])

        self.final_product_df = self.final_product_df.rename(columns={'weight': 'weight_kg'})
        self.final_product_df = self.final_product_df.drop(columns=['in_kg', 'weight_units'])

        return self.final_product_df

    def clean_orders_data(self, orders_df):
        self.orders_df = orders_df
        self.orders_df = self.orders_df.drop(columns=['index', 'level_0', 'first_name', 'last_name', '1'])
        self.orders_df['card_number'] = pd.to_numeric(self.orders_df['card_number'], errors='coerce')

        return self.orders_df

    def clean_dates_data(self, dates_df):
        self.dates_df = dates_df
        self.dates_df = pd.read_json('date_details.json')

        self.dates_df = self.dates_df[self.dates_df['time_period'].isin(['Evening', 'Morning', 'Midday', 'Late_Hours'])]

        self.dates_df['date'] = pd.to_datetime(self.dates_df[['year', 'month', 'day']])
        self.dates_df['date'] = self.dates_df['date'].astype(str)
        self.dates_df['date'] = pd.to_datetime(self.dates_df['date'] + ' ' + self.dates_df['timestamp'])

        return self.dates_df

