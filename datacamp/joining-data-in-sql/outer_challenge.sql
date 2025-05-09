/*
Instructions
- Select country name AS country, region, and life expectancy AS life_exp.
- Make sure to use LEFT JOIN, WHERE, ORDER BY, and LIMIT.
*/

-- Select fields
SELECT c.name AS country, region, p.life_expectancy AS life_exp
-- From countries (alias as c)
FROM countries AS c
  -- Join to populations (alias as p)
  LEFT JOIN populations AS p
    -- Match on country code
    ON c.code = p.country_code
-- Focus on 2010
WHERE year = 2010
-- Order by life_exp
ORDER BY life_exp
-- Limit to 5 records
LIMIT 5;
