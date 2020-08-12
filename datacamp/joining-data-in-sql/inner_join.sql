/*
Instructions
- Begin by selecting all columns from the cities table.
- Inner join the cities table on the left to the countries table on the right, keeping all of the fields in both tables.
- You should match the tables on the country_code field in cities and the code field in countries.
- Do not alias your tables here or in the next step. Using cities and countries is fine for now.
- Modify the SELECT statement to keep only the name of the city, the name of the country, and the name of the region the country resides in.
- Recall from our Intro to SQL for Data Science course that you can alias fields using AS. Alias the name of the city AS city and the name of the country AS country.
*/

-- Select all columns from cities
SELECT *
FROM cities;

SELECT * 
FROM cities
  -- 1. Inner join to countries
  INNER JOIN countries
    -- 2. Match on the country codes
    ON cities.country_code = countries.code;

-- 1. Select name fields (with alias) and region 
SELECT cities.name AS city, countries.name AS country, countries.region
FROM cities
  INNER JOIN countries
    ON cities.country_code = countries.code;
