/*
Instructions
- Get all details for all films released in 2016.
- Get the number of films released before 2000.
- Get the title and release year of films released after 2000.
*/

SELECT *
FROM films
WHERE release_year = 2016

SELECT COUNT(*)
FROM films
WHERE release_year < 2000

SELECT title, release_year
FROM films
WHERE release_year > 2000
