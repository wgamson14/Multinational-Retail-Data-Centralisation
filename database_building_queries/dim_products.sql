
UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');

ALTER TABLE dim_products
    ADD COLUMN weight_class text;

UPDATE dim_products
SET weight_class = CASE
                    WHEN weight_kg < 2 THEN 'Light'
                    WHEN weight_kg >= 2 AND weight_kg < 40 THEN 'Mid_Sized'
                    WHEN weight_kg >= 40 AND weight_kg < 140 THEN 'Heavy'
                    ELSE 'Truck_Required'
                END;


SELECT * FROM dim_products ORDER BY index ASC;


--------------------------------------------------------------------------------

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE float USING product_price::float;

ALTER TABLE dim_products
ALTER COLUMN weight_kg TYPE float USING weight_kg::float;

ALTER TABLE dim_products
ALTER COLUMN ean TYPE varchar(17);

ALTER TABLE dim_products
ALTER COLUMN product_code TYPE varchar(11);

ALTER TABLE dim_products
ALTER COLUMN date_added TYPE date;

ALTER TABLE dim_products
ALTER COLUMN uuid TYPE uuid USING uuid::uuid;

ALTER TABLE dim_products
RENAME removed TO still_available;


ALTER TABLE dim_products
ALTER COLUMN still_available TYPE boolean
USING CASE still_available 
        WHEN 'Still_avaliable' THEN TRUE
        WHEN 'Removed' THEN FALSE
    END;

ALTER TABLE dim_products
ALTER COLUMN weight_class TYPE varchar(14);




