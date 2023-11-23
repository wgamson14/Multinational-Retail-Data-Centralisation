ALTER TABLE dim_store_details
ALTER COLUMN locality TYPE varchar(255);

ALTER TABLE dim_store_details
ALTER COLUMN store_code TYPE varchar(12);

ALTER TABLE dim_store_details
ALTER COLUMN staff_numbers TYPE smallint;

ALTER TABLE dim_store_details
ALTER COLUMN opening_date TYPE date;

ALTER TABLE dim_store_details
ALTER COLUMN store_type TYPE varchar(255);

ALTER TABLE dim_store_details
ALTER COLUMN country_code TYPE varchar(2);

ALTER TABLE dim_store_details
ALTER COLUMN continent TYPE varchar(255);

