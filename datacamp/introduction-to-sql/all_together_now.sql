/*
Instructions
- Get the release year, budget and gross earnings for each film in the films table.
- Modify your query so that only records with a release_year after 1990 are included.
- Remove the budget and gross columns, and group your results by release year.
- Modify your query to include the average budget and average gross earnings for the results you have so far. 
Alias the average budget as avg_budget; alias the average gross earnings as avg_gross.
- Modify your query so that only years with an average budget of greater than $60 million are included.
- Finally, modify your query to order the results from highest average gross earnings to lowest.
*/

SELECT release_year, budget, gross
FROM films;

SELECT release_year, budget, gross
FROM films
WHERE release_year > 1990;

SELECT release_year
FROM films
WHERE release_year > 1990
GROUP BY release_year;

SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year;

SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
GROUP BY release_year
HAVING AVG(budget) > 60000000
ORDER BY avg_gross DESC;
