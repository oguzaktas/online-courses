/*
Instructions
- Get the IMDB score and film ID for every film from the reviews table, sorted from highest to lowest score.
- Get the title for every film, in reverse order.
- Get the title and duration for every film, in order of longest duration to shortest.
*/

SELECT imdb_score, film_id
FROM reviews
ORDER BY imdb_score DESC;

SELECT title
FROM films
ORDER BY title DESC;

SELECT title, duration
FROM films
ORDER BY duration DESC;
