/*
Instructions
- Get the release year and count of films released in each year.
- Get the release year and average duration of all films, grouped by release year.
- Get the release year and largest budget for all films, grouped by release year.
- Get the IMDB score and count of film reviews grouped by IMDB score in the reviews table.
*/

SELECT release_year, COUNT(*)
FROM films
GROUP BY release_year;

SELECT release_year, AVG(duration)
FROM films
GROUP BY release_year;

SELECT release_year, MAX(budget)
FROM films
GROUP BY release_year;

SELECT imdb_score, COUNT(*)
FROM reviews
GROUP BY imdb_score;
