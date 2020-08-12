/*
Instructions
Using the countries table, create a new field AS geosize_group that groups the countries into three groups:
- If surface_area is greater than 2 million, geosize_group is 'large'.
- If surface_area is greater than 350 thousand but not larger than 2 million, geosize_group is 'medium'.
- Otherwise, geosize_group is 'small'.
*/

SELECT name, continent, code, surface_area,
    -- 1. First case
    CASE WHEN surface_area > 2000000 THEN 'large'
        -- 2. Second case
        WHEN surface_area > 350000 AND surface_area < 2000000 THEN 'medium'
        -- 3. Else clause + end
        ELSE 'small' END
        -- 4. Alias name
        AS geosize_group
-- 5. From table
FROM countries;
