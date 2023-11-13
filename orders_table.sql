ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE uuid USING date_uuid::uuid; 

ALTER TABLE orders_table
ALTER COLUMN user_uuid TYPE uuid USING user_uuid::uuid; 

ALTER TABLE orders_table
ALTER COLUMN card_number TYPE varchar(19);

ALTER TABLE orders_table
ALTER COLUMN store_code TYPE varchar(12);

ALTER TABLE orders_table
ALTER COLUMN product_code TYPE varchar(11);

ALTER TABLE orders_table
ALTER COLUMN product_quantity TYPE smallint;