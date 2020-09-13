/*
Instructions
- Get the title and release year for all Spanish language films released before 2000.
- Get all details for Spanish language films released after 2000.
- Get all details for Spanish language films released after 2000, but before 2010.
*/

SELECT title, release_year
FROM films
WHERE release_year < 2000 AND language = 'Spanish'

SELECT *
FROM films
WHERE language = 'Spanish' AND release_year > 2000

SELECT *
FROM films
WHERE release_year > 2000 AND release_year < 2010 AND language = 'Spanish'
