/*
Instructions
- Again, order by code and then by year, both in ascending order.
- Note the number of records here (given at the bottom of query result) compared to the similar UNION ALL query result (814 records).
*/

-- Select fields
SELECT code, year
  -- From economies
  FROM economies
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT country_code, year
  -- From populations
  FROM populations
-- Order by code, year
ORDER BY code, year;
