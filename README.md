# Multinational Retail Data Centralisation

**Overview:** In this project the aim the commpile together different forms of data from various sources, for a fictional retail company. The data must be download using the correct extraction method before being cleaned and eventually upload to the correct *sales_data* database on *pgAdmin*.

## Contents
- Extracting and Cleaning



# Extracting and Cleaning
A database first had to be initialised which will allows us to uplaod and store the data and 3 classes were created each having a different function; *Connecting, Extracting* and *Cleaning*.

Data was first extracted from a secondary database and was downloaded and read as a *.yaml* file. To do this an engine was creeated using the database's credential, which in turn are stored in a .gitignore file for security purposes. Methods were created in the *DataExtracting* class to allow the file to be read and converted into a *pandas DataFrame*. the *DataCleaning* class can then be utilised to clean the table before using a separate method to upload to our own *sales_data* database.
Data was further extracted from and AWS S3 bucket and converted directly to a DataFrame using *tabula-py* package. Other data was extracted from an AWS S3 bucet as well, this time it was downloaded and saved to a file in the local computer using *boto3* package. Finally, data was extract through the use of an api, a for loop was created to allow each data set retrieved to be appended to the empty DataFrame.

All data was now extracted so can be passed through the *DataCleaning* class, each *pandas DataFrame(df)* has an individual method to be cleaned which can be called from the main file.Finally, *DataConnector* class was initialise and called to allow each newly cleaned table to be uploaded to the *sales-data* database.

