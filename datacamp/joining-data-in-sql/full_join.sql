/*
Instructions
- Choose records in which region corresponds to North America or is NULL.
- Repeat the same query as above but use a LEFT JOIN instead of a FULL JOIN. Note what has changed compared to the FULL JOIN result!
- Repeat the same query as above but use an INNER JOIN instead of a FULL JOIN. Note what has changed compared to the FULL JOIN and LEFT JOIN results!
*/

SELECT name AS country, code, region, basic_unit
-- 3. From countries
FROM countries
  -- 4. Join to currencies
  FULL JOIN currencies
    -- 5. Match on code
    USING (code)
-- 1. Where region is North America or null
WHERE region = 'North America' OR region IS NULL
-- 2. Order by region
ORDER BY region;


SELECT name AS country, code, region, basic_unit
-- 1. From countries
FROM countries
  -- 2. Join to currencies
  LEFT JOIN currencies
    -- 3. Match on code
    USING (code)
-- 4. Where region is North America or null
WHERE region = 'North America' OR region IS NULL
-- 5. Order by region
ORDER BY region;


SELECT name AS country, code, region, basic_unit
FROM countries
  -- 1. Join to currencies
  INNER JOIN currencies
    USING (code)
-- 2. Where region is North America or null
WHERE region = 'North America' OR region IS NULL
-- 3. Order by region
ORDER BY region;
