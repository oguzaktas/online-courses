/*
Instructions
- Get the names of all people whose names begin with 'B'. The pattern you need is 'B%'.
- Get the names of people whose names have 'r' as the second letter. The pattern you need is '_r%'.
- Get the names of people whose names don't start with A. The pattern you need is 'A%'.
*/

SELECT name
FROM people
WHERE name LIKE 'B%';

SELECT name
FROM people
WHERE name LIKE '_r%';

SELECT name
FROM people
WHERE name NOT LIKE 'A%';
