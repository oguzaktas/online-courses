/*
Instructions
- Get the names of people from the people table, sorted alphabetically.
- Get the names of people, sorted by birth date.
- Get the birth date and name for every person, in order of when they were born.
*/

SELECT name
FROM people
ORDER BY name ASC;

SELECT name
FROM people
ORDER BY birthdate;

SELECT name, birthdate
FROM people
ORDER BY birthdate;
