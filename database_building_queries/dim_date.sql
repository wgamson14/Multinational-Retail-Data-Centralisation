ALTER TABLE dim_date_times
ALTER COLUMN time_period TYPE varchar(10); 

ALTER TABLE dim_date_times
ALTER COLUMN date_uuid TYPE uuid USING date_uuid::uuid; 

ALTER TABLE dim_date_times
ALTER COLUMN month TYPE varchar(2);

ALTER TABLE dim_date_times
ALTER COLUMN year TYPE varchar(4);

ALTER TABLE dim_date_times
ALTER COLUMN day TYPE varchar(2);
