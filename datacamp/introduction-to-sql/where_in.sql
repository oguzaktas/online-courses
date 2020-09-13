/*
Instructions
- Get the title and release year of all films released in 1990 or 2000 that were longer than two hours. Remember, duration is in minutes!
- Get the title and language of all films which were in English, Spanish, or French.
- Get the title and certification of all films with an NC-17 or R certification.
*/

SELECT title, release_year
FROM films
WHERE (release_year = 1990 OR release_year = 2000)
AND duration > 120;

SELECT title, language
FROM films
WHERE language IN ('English', 'Spanish', 'French');

SELECT title, certification
FROM films
WHERE certification = 'NC-17' OR certification = 'R';
