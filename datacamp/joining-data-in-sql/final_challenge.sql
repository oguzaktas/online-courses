/*
Instructions
- Select unique country names. Also select the total investment and imports fields.
- Use a left join with countries on the left. (An inner join would also work, but please use a left join here.)
- Match on code in the two tables AND use a subquery inside of ON to choose the appropriate languages records.
- Order by country name ascending.
- Use table aliasing but not field aliasing in this exercise.
*/

-- Select fields
SELECT DISTINCT name, total_investment, imports
  -- From table (with alias)
  FROM countries AS c
    -- Join with table (with alias)
    LEFT JOIN economies AS e
      -- Match on code
      ON (c.code = e.code
      -- and code in Subquery
        AND c.code IN (
          SELECT l.code
          FROM languages AS l
          WHERE official = 'true'
        ) )
  -- Where region and year are correct
  WHERE region = 'Central America' AND year = 2015
-- Order by field
ORDER BY name;
