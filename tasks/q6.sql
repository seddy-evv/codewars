-- For this challenge you need to create a SELECT statement, this SELECT statement will use an IN
-- to check whether a department has had a sale with a price over 90.00 dollars BUT the sql MUST use
-- the WITH statement which will be used to select all columns from sales where the price is greater than 90.00,
-- you must call this sub-query special_sales.
--
-- departments table schema
-- id
-- name
-- sales table schema
-- id
-- department_id (department foreign key)
-- name
-- price
-- card_name
-- card_number
-- transaction_date
-- resultant table schema
-- id
-- name

WITH special_sales (id)
AS
(
  SELECT department_id as id
  FROM sales
  WHERE price > 90
)
SELECT id, name
FROM departments
WHERE id IN
(
  SELECT id
  FROM special_sales
)
