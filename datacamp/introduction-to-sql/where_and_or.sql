/*
Instructions
- Get the title and release year for films released in the 90s.
- Now, build on your query to filter the records to only include French or Spanish language films.
- Finally, restrict the query to only return films that took in more than $2M gross.
*/

SELECT title, release_year
FROM films
WHERE (release_year >= 1990 AND release_year < 2000);

SELECT title, release_year
FROM films
WHERE (release_year >= 1990 AND release_year < 2000)
AND (language = 'French' OR language = 'Spanish');

SELECT title, release_year
FROM films
WHERE (release_year >= 1990 AND release_year < 2000)
AND (language = 'French' OR language = 'Spanish')
AND (gross >= 2000000);
