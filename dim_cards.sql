ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE varchar(19); 

ALTER TABLE dim_card_details
ALTER COLUMN expiry_date TYPE date; 

ALTER TABLE dim_card_details
ALTER COLUMN date_payment_confirmed TYPE date; 