ALTER TABLE dim_users
ALTER COLUMN first_name TYPE varchar(255);

ALTER TABLE dim_users
ALTER COLUMN last_name TYPE varchar(255);

ALTER TABLE dim_users
ALTER COLUMN date_of_birth TYPE date;

ALTER TABLE dim_users
ALTER COLUMN country_code TYPE varchar(2);

ALTER TABLE dim_users
ALTER COLUMN user_uuid TYPE uuid USING user_uuid::uuid;

ALTER TABLE dim_users
ALTER COLUMN join_date TYPE date;
