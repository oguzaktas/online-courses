/*
Instructions
- Include the name of region, its continent, and average fertility rate aliased as avg_fert_rate.
- Sort based on avg_fert_rate ascending.
- Remember that you'll need to GROUP BY all fields that aren't included in the aggregate function of SELECT.
*/

-- Select fields
SELECT region, continent, AVG(fertility_rate) AS avg_fert_rate
  -- From left table
  FROM countries AS c
    -- Join to right table
    INNER JOIN populations AS p
      -- Match on join condition
      ON c.code = p.country_code
  -- Where specific records matching some condition
  WHERE year = 2015
-- Group appropriately
GROUP BY region, continent
-- Order appropriately
ORDER BY avg_fert_rate;
