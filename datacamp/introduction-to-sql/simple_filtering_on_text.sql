/*
Instructions
- Get all details for all French language films.
- Get the name and birth date of the person born on November 11th, 1974. Remember to use ISO date format ('1974-11-11')!
- Get the number of Hindi language films.
- Get all details for all films with an R certification.
*/

SELECT *
FROM films
WHERE language = 'French'

SELECT name, birthdate
FROM people
WHERE birthdate = ('1974-11-11')

SELECT COUNT(*)
FROM films
WHERE language = 'Hindi'

SELECT *
FROM films
WHERE certification = 'R'
