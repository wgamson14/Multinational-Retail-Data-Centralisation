# Multinational Retail Data Centralisation

**Overview:** In this project the aim the commpile together different forms of data from various sources, for a fictional retail company. The data must be download using the correct extraction method before being cleaned and eventually upload to the correct *sales_data* database on *pgAdmin*.

## Contents
- File Structure
- Extracting and Cleaning
- Changing Datatypes
- Querying the Data


# File Structure
## List of the  Relevant Files
Files containing the classes and method for extracting, cleaning the data and connecting the database:
- database_utils.py
- data_cleaning.py
- data_extraction.py

Files used to chnage the data types in the respectve table using SQL:
- dim_cards.sql
- dim_date.sql
- dim_products.sql
- dim_store.sql
- dim_users.sql
- orders_table.sql

Files used to create keys for the database:
- primary_keys.sql
- foregin_keys.sql

File used to query the data for the retail company:
- querying_data.sql


# Extracting and Cleaning
A database first had to be initialised which will allows us to uplaod and store the data and 3 classes were created each having a different function; *Connecting, Extracting* and *Cleaning*.

Data was first extracted from a secondary database and was downloaded and read as a *.yaml* file. To do this an engine was creeated using the database's credential, which in turn are stored in a .gitignore file for security purposes. Methods were created in the *DataExtracting* class to allow the file to be read and converted into a *pandas DataFrame*. the *DataCleaning* class can then be utilised to clean the table before using a separate method to upload to our own *sales_data* database.
Data was further extracted from and AWS S3 bucket and converted directly to a DataFrame using *tabula-py* package. Other data was extracted from an AWS S3 bucet as well, this time it was downloaded and saved to a file in the local computer using *boto3* package. Finally, data was extract through the use of an api, a for loop was created to allow each data set retrieved to be appended to the empty DataFrame.

All data was now extracted so can be passed through the *DataCleaning* class, each *pandas DataFrame(df)* has an individual method to be cleaned which can be called from the main file.Finally, *DataConnector* class was initialise and called to allow each newly cleaned table to be uploaded to the *sales-data* database.

# Changing Datatypes
SQL tools were used to enable us to change the datatypes within each of our tables, utilsing *ALTER COLUMN to TYPE* allowed the changing. A connection was set up the the pgAdmin database, *sales_data*, and the changes were done directly in VSCode with the changes being checked directly in pgAdmin. 
Once all the columns were of the correct datatype, primary and foreign keys were set up to finlise the star-based schema, making sure each foreign key referenced the ocrrect primary key in the corresponding table.

# Querying the Data
Finally, the retail company wanted to use the freshly cleaned data to enhance their outlook on the store. Mutiple questions can be resolved based on querying the data by highlighting areas for imporvemnt iin sales etc. Examples included, finding which month is the most profitable for the company or finding the precentage of sales that were made from the website to analyse their online sales. 

