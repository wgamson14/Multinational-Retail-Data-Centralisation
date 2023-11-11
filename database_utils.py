import yaml
from yaml.loader import SafeLoader
from sqlalchemy import create_engine

class DatabaseConnector:
    def read_db_creds(self, file_name):
        with open(file_name) as f:
            creds = yaml.load(f, Loader=SafeLoader)
            return creds
    
    def init_db_engine(self):
        creds = self.read_db_creds('db_creds.yaml')
        self.engine = create_engine(f"postgresql+psycopg2://{creds['USER']}:{creds['PASSWORD']}@{creds['HOST']}:{creds['PORT']}/{creds['DATABASE']}")
        self.engine.connect()
        return self.engine

    def upload_to_db(self, dataframe, table_name):
        self.dataframe = dataframe
        self.table_name = table_name
        creds = self.read_db_creds('sales_db_creds.yaml')
        upload = create_engine(f"postgresql://{creds['USER']}:{creds['PASSWORD']}@{creds['HOST']}:{creds['PORT']}/{creds['DATABASE']}")
        self.dataframe.to_sql(name=self.table_name, con=upload, if_exists='replace')













        

        
        

