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


-- I love Fibonacci numbers in general, but I must admit I love some more than others.
--
-- I would like for you to write me a function that, when given a number n (n >= 1 ),
-- returns the nth number in the Fibonacci Sequence.
--
-- For example:
--
--   nthFibo(4) == 2
--
-- Because 2 is the 4th number in the Fibonacci Sequence.
--
-- For reference, the first two numbers in the Fibonacci sequence are 0 and 1,
-- and each subsequent number is the sum of the previous two.

--# write your SQL statement here:
-- you are given a table 'fibo' with column 'n'.
-- return a table with:
--   this column and your result in a column named 'res'
--   ordered ascending by 'n'
--   distinct results (remove duplicates)

create or replace function fibo (n bigint)

returns bigint
language plpgsql
as $$
declare
  first_var bigint := 0;
  second_var bigint := 1;
  third_var bigint := 0;
begin
  if n = 1
    then return first_var;
  elsif n = 2
    then return second_var;
  else
    begin
      for i in 3..n loop
        third_var := first_var + second_var;
        first_var := second_var;
        second_var := third_var;
      end loop;
      return second_var;
    end;
  end if;
end $$;

select distinct
  n,
  fibo(n) res
from
  fibo
order by
  n;
