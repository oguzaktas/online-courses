/*
Instructions
- Get the country, average budget, and average gross take of countries that have made more than 10 films. 
Order the result by country name, and limit the number of results displayed to 5. 
You should alias the averages as avg_budget and avg_gross respectively.
*/

-- select country, average budget, average gross
SELECT country, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
-- from the films table
FROM films
-- group by country 
GROUP BY country
-- where the country has more than 10 titles
HAVING COUNT(*) > 10
-- order by country
ORDER BY country
-- limit to only show 5 results
LIMIT 5;
