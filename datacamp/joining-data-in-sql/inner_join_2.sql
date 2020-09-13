/*
Instructions
- Inner join countries (left) and populations (right) on the code and country_code fields respectively.
- Alias countries AS c and populations AS p.
- Select code, name, and region from countries and also select year and fertility_rate from populations (5 fields in total).
*/

-- 6. Select fields
SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join to populations (as p)
  INNER JOIN populations AS p
    -- 3. Match on country code
    ON c.code = p.country_code
  -- 4. Join to economies (as e)
  INNER JOIN economies AS e
    -- 5. Match on country code and year
    ON c.code = e.code AND p.year = e.year;