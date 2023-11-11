from sqlalchemy import inspect 
import pandas as pd
import tabula
import requests
import numpy as np
import boto3

class DataExtractor:
    def list_db_tables(self, engine):
        inspector = inspect(engine)
        print(inspector.get_table_names())

    def read_rds_table(self, table_name, engine):
        self.table_name = table_name
        self.df = pd.read_sql_table(self.table_name, engine)
        return self.df

    def retrieve_pdf_data(self):
        self.pdf_path = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
        self.card_df = tabula.read_pdf(self.pdf_path, pages='all', stream=False)
        self.card_df = pd.concat(self.card_df)
        return self.card_df

    def list_number_of_stores(self, endpoint, header_dict):
        self.endpoint = endpoint
        self.header_dict = header_dict
        self.num_of_stores = requests.get(self.endpoint, headers=self.header_dict)
        return self.num_of_stores.content

    def retrieve_stores_data(self, endpoint, header_dict):
        self.header_dict = header_dict
        self.store_df = pd.DataFrame()
        for self.store_number in range(0, 451):
            self.endpoint = endpoint + str(f'{self.store_number}')
            self.response = requests.get(self.endpoint, headers=self.header_dict).json()
            self.store_df =  pd.concat([self.store_df, pd.DataFrame(self.response, index=[np.NaN])], ignore_index=True)
        return self.store_df

    def extract_from_s3(self, file_path, bucket, object):
        self.s3 = boto3.client('s3')
        with open(file_path, 'wb') as f:
            self.s3.download_fileobj(bucket, object, f)




        

