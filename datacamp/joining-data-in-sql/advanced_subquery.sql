/*
Instructions
- Now it's time to append the second part's query to the first part's query using AND and IN to obtain 
the name of the country, its continent, and the maximum inflation rate for each continent in 2015!
- For the sake of practice, change all joining conditions to use ON instead of USING (based upon the same column, code).
- Revisit the sample output in the assignment text at the beginning of the exercise to see how this matches up.
Select the maximum inflation rate in 2015 AS max_inf grouped by continent using the previous step's query as a subquery in the FROM clause.
- Thus, in your subquery you should:
    - Create an inner join with countries on the left and economies on the right with USING (without aliasing your tables or columns).
    - Retrieve the country name, continent, and inflation rate for 2015.
    - Alias the subquery as subquery.
- This will result in the six maximum inflation rates in 2015 for the six continents as 
one field table. Make sure to not include continent in the outer SELECT statement.
- Now it's time to append your second query to your first query using AND and IN to obtain the name of the country, its continent, and the maximum inflation rate for each continent in 2015.
- For the sake of practice, change all joining conditions to use ON instead of USING.
*/

-- Select fields
SELECT name, continent, inflation_rate
  -- From countries
  FROM countries
  	-- Join to economies
  	INNER JOIN economies
    -- Match on code
    ON countries.code = economies.code
-- Where year is 2015
WHERE year = 2015;


-- Select the maximum inflation rate as max_inf
SELECT MAX(inflation_rate) AS max_inf
  -- Subquery using FROM (alias as subquery)
  FROM (
      SELECT name, continent, inflation_rate
      FROM countries
      INNER JOIN economies
      USING(code)
      WHERE year = 2015) AS subquery
-- Group by continent
GROUP BY continent;


-- Select fields
SELECT name, continent, inflation_rate
  -- From countries
  FROM countries
	-- Join to economies
	INNER JOIN economies
	-- Match on code
	ON countries.code = economies.code
  -- Where year is 2015
  WHERE year = 2015
    -- And inflation rate in subquery (alias as subquery)
    AND inflation_rate IN (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
             SELECT name, continent, inflation_rate
             FROM countries
             INNER JOIN economies
             ON countries.code = economies.code
             WHERE year = 2015) AS subquery
      -- Group by continent
        GROUP BY continent);
