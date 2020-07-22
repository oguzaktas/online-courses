/*
Instructions
- Get the title and release year of all films released between 1990 and 2000 (inclusive).
- Now, build on your previous query to select only films that have budgets over $100 million.
- Now restrict the query to only return Spanish language films.
- Finally, modify to your previous query to include all Spanish language or French language films with the same criteria as before. Don't forget your parentheses!
*/

SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000;

SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000;

SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000
AND language = 'Spanish';

SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000
AND (language = 'Spanish' OR language = 'French');
