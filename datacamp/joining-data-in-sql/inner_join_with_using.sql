/*
Instructions
- Inner join countries on the left and languages on the right with USING(code).
- Select the fields corresponding to:
    - country name AS country,
    - continent name,
    - language name AS language, and
    - whether or not the language is official.
- Remember to alias your tables using the first letter of their names.
*/

-- 4. Select fields
SELECT c.name AS country, continent, l.name AS language, official
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join to languages (as l)
  INNER JOIN languages AS l
    -- 3. Match using code
    USING(code)