SELECT country_code,
       COUNT(country_code)
FROM 
    dim_store_details
GROUP BY
    country_code;

-- displays 266 because of the web store
------------------------------------------------------------------------

SELECT locality,
       COUNT(locality) AS no_stores
FROM   
    dim_store_details
GROUP BY
    locality
ORDER BY
    no_stores DESC
LIMIT 7;

-- Returns the areas with th emost number of stores

------------------------------------------------------------------------

SELECT dim_date_times.month,
       SUM(orders_table.product_quantity * dim_products.product_price) AS order_price
FROM
    orders_table
LEFT OUTER JOIN
    dim_date_times ON dim_date_times.date_uuid = orders_table.date_uuid
LEFT OUTER JOIN
    dim_products ON dim_products.product_code = orders_table.product_code
GROUP BY
    dim_date_times.month
ORDER BY
    order_price DESC;

-- Returns the months with the most sales
    
------------------------------------------------------------------------


SELECT store_code,
       COUNT(store_code) AS store_orders
FROM
    orders_table
WHERE
    store_code = 'WEB-1388012W'
GROUP BY
    store_code;

-- Returns number of orders from web store

WITH cte AS (
    SELECT store_code,
       COUNT(store_code) AS store_orders
FROM
    orders_table
GROUP BY
    store_code
)
SELECT 
       SUM(store_orders)
FROM 
    cte
WHERE
    store_code != 'WEB-1388012W';

-- Returns number of orders made in person/offline

SELECT SUM(product_quantity)
FROM 
    orders_table
WHERE
    store_code = 'WEB-1388012W'; 

-- Returns total product quantity count of orders made from the web

SELECT SUM(product_quantity)
FROM 
    orders_table
WHERE
    store_code != 'WEB-1388012W'; 

-- Returns total product quantity count of orders made in person/offline

------------------------------------------------------------------------

SELECT dim_store_details.store_type,
       SUM(orders_table.product_quantity * dim_products.product_price) AS total_sales,
CAST(COUNT(*) AS NUMERIC) / CAST((SELECT COUNT(*) FROM orders_table) AS NUMERIC) * 100 as percentage_total
FROM
    orders_table
LEFT OUTER JOIN
    dim_date_times ON dim_date_times.date_uuid = orders_table.date_uuid
LEFT OUTER JOIN
    dim_products ON dim_products.product_code = orders_table.product_code
LEFT OUTER JOIN
    dim_store_details ON dim_store_details.store_code = orders_table.store_code
GROUP BY
store_type;

-- Returns total sales for a store type as a percentage of all sales

------------------------------------------------------------------------

SELECT dim_date_times.month,
       dim_date_times.year,
       SUM(orders_table.product_quantity * dim_products.product_price) AS order_price
FROM
    orders_table
LEFT OUTER JOIN
    dim_date_times ON dim_date_times.date_uuid = orders_table.date_uuid
LEFT OUTER JOIN
    dim_products ON dim_products.product_code = orders_table.product_code
GROUP BY
    dim_date_times.month,
    dim_date_times.year
ORDER BY
    order_price DESC;

-- Returns which month in each year produced highest cost of sales

------------------------------------------------------------------------

SELECT country_code,
       SUM(staff_numbers)
FROM 
    dim_store_details
GROUP BY
    country_code;

-- Returns number of staff within each country code

------------------------------------------------------------------------

SELECT dim_store_details.store_type,
       country_code,
       SUM(orders_table.product_quantity * dim_products.product_price) AS total_sales
FROM    
    orders_table
LEFT OUTER JOIN
    dim_date_times ON dim_date_times.date_uuid = orders_table.date_uuid
LEFT OUTER JOIN
    dim_products ON dim_products.product_code = orders_table.product_code
LEFT OUTER JOIN
    dim_store_details ON dim_store_details.store_code = orders_table.store_code
WHERE
    dim_store_details.country_code = 'DE'
GROUP BY
    store_type,
    country_code;

-- Return which type of store generates most sales in Germany

------------------------------------------------------------------------

WITH cte AS (
        SELECT dim_date_times.year,
               dim_date_times.date
        FROM
            dim_date_times
        LEFT OUTER JOIN
            orders_table ON orders_table.date_uuid = dim_date_times.date_uuid
            ), cte2 AS (
                    SELECT year,
                           date,
                    LEAD(date, 1) OVER (
                        ORDER BY year
                    )
                    FROM cte
                    GROUP BY
                        year,
                        date
            )
SELECT year,
       AVG(lead - date) AS actual_time_taken
FROM cte2
GROUP BY
    year
ORDER BY
    actual_time_taken DESC;

-- Returns the avergae time taken between each sale grouped by the year

------------------------------------------------------------------------










