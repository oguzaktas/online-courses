/*
Instructions
- Use the SUM function to get the total amount grossed by all films made in the year 2000 or later.
- Get the average amount grossed by all films whose titles start with the letter 'A'.
- Get the amount grossed by the worst performing film in 1994.
- Get the amount grossed by the best performing film between 2000 and 2012, inclusive.
*/

SELECT SUM(gross)
FROM films
WHERE release_year >= 2000;

SELECT AVG(gross)
FROM films
WHERE title LIKE 'A%';

SELECT MIN(gross)
FROM films
WHERE release_year = 1994;

SELECT MAX(gross)
FROM films
WHERE release_year BETWEEN 2000 AND 2012;
