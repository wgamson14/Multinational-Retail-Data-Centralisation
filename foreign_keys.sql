ALTER TABLE dim_date_times
ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);

ALTER TABLE dim_users
ADD FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);

ALTER TABLE dim_card_details
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);

ALTER TABLE dim_store_details
ADD FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);

ALTER TABLE dim_products
ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code);