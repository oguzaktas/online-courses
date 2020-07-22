/*
Instructions
- Remove the comments around the second query and comment out the first query instead.
- Convert the GROUP BY code to use a subquery inside of SELECT, i.e. fill in the blanks 
to get a result that matches the one given using the GROUP BY code in the first query.
- Again, sort the result by cities_num descending and then by country ascending.
*/

SELECT countries.name AS country, COUNT(*) AS cities_num
  FROM cities
    INNER JOIN countries
    ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;

/* 
SELECT ___ AS ___,
  (SELECT ___
   FROM ___
   WHERE countries.code = cities.country_code) AS cities_num
FROM ___
ORDER BY ___ ___, ___
LIMIT 9;
*/

SELECT countries.name AS country,
  (SELECT COUNT(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country ASC
LIMIT 9;
