/*
Instructions
- Begin by calculating the average life expectancy across all countries for 2015.
- Select all fields from populations with records corresponding to larger than 1.15 times the average you calculated 
in the first task for 2015. In other words, change the 100 in the example above with a subquery.
*/

-- Select average life_expectancy
SELECT AVG(life_expectancy)
  -- From populations
  FROM populations
-- Where year is 2015
WHERE year = 2015;


-- Select fields
SELECT *
  -- From populations
  FROM populations
-- Where life_expectancy is greater than
WHERE life_expectancy > 1.15 * (
  -- 1.15 * subquery
  SELECT AVG(life_expectancy)
   FROM populations
   WHERE year = 2015)
  AND year = 2015;
