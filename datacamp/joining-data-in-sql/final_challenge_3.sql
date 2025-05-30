/*
Instructions
- Select the city name, country code, city proper population, and metro area population.
- Calculate the percentage of metro area population composed of city proper population for each city in cities, aliased as city_perc.
- Focus only on capital cities in Europe and the Americas in a subquery.
- Make sure to exclude records with missing data on metro area population.
- Order the result by city_perc descending.
- Then determine the top 10 capital cities in Europe and the Americas in terms of this city_perc percentage.
*/

-- Select fields
SELECT name, country_code, city_proper_pop, metroarea_pop,  
      -- Calculate city_perc
      city_proper_pop / metroarea_pop * 100 AS city_perc
  -- From appropriate table
  FROM cities
  -- Where 
  WHERE name IN
    -- Subquery
    (SELECT capital
     FROM countries
     WHERE continent = 'Europe'
        OR continent LIKE '%America%')
       AND metroarea_pop IS NOT NULL
-- Order appropriately
ORDER BY city_perc DESC
-- Limit amount
LIMIT 10;
