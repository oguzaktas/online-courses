/*
Instructions
- Get the percentage of people who are no longer alive. Alias the result as percentage_dead. Remember to use 100.0 and not 100!
- Get the number of years between the newest film and oldest film. Alias the result as difference.
- Get the number of decades the films table covers. Alias the result as number_of_decades. The top half of your fraction should be enclosed in parentheses.
*/

-- get the count(deathdate) and multiply by 100.0
-- then divide by count(*)

SELECT (COUNT(deathdate) * 100.0) / COUNT(*) AS percentage_dead
FROM people;

SELECT MAX(release_year) - MIN(release_year) AS difference
FROM films;

SELECT (MAX(release_year) - MIN(release_year)) / 10 AS number_of_decades
FROM films;
