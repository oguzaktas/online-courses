/*
Instructions
- Order the resulting field in ascending order.
- Can you spot the city/cities that are actually capital cities which this query misses?
*/

-- Select field
SELECT name
  -- From cities
  FROM cities
	-- Set theory clause
	EXCEPT
-- Select field
SELECT capital
  -- From countries
  FROM countries
-- Order by result
ORDER BY name;
