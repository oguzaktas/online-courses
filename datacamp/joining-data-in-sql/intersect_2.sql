/*
Instructions
- Use INTERSECT to answer this question with countries and cities!
*/

-- Select fields
SELECT name
  -- From countries
  FROM countries
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT name
  -- From cities
  FROM cities;
