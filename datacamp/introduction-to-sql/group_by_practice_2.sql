/*
Instructions
- Get the release year and lowest gross earnings per release year.
- Get the language and total gross amount films in each language made.
- Get the country and total budget spent making movies in each country.
- Get the release year, country, and highest budget spent making a film for each year, for each country. Sort your results by release year and country.
- Get the country, release year, and lowest amount grossed per release year per country. Order your results by country and release year.
- Finally, modify your query to order the results from highest average gross earnings to lowest.
*/

SELECT release_year, MIN(gross)
FROM films
GROUP BY release_year;

SELECT language, SUM(gross)
FROM films
GROUP BY language;

SELECT country, SUM(budget)
FROM films
GROUP BY country;

SELECT release_year, MAX(budget), country
FROM films
GROUP BY release_year, country
ORDER BY release_year, country;

SELECT country, release_year, MIN(gross)
FROM films
GROUP BY release_year, country
ORDER BY country, release_year;

SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
GROUP BY release_year
HAVING AVG(budget) > 60000000;

SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
GROUP BY release_year
HAVING AVG(budget) > 60000000
ORDER BY avg_gross DESC;
