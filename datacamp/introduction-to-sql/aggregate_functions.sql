/*
Instructions
- Use the SUM function to get the total duration of all films.
- Get the average duration of all films.
- Get the duration of the shortest film.
- Get the duration of the longest film.
*/

SELECT SUM(duration)
FROM films;

SELECT AVG(duration)
FROM films;

SELECT MIN(duration)
FROM films;

SELECT MAX(duration)
FROM films;
