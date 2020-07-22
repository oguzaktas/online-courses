/*
Instructions
- Begin by determining for each country code how many languages are listed in the languages table using SELECT, FROM, and GROUP BY.
- Alias the aggregated field as lang_num.
- Include the previous query (aliased as subquery) as a subquery in the FROM clause of a new query.
- Select the local name of the country from countries.
- Also, select lang_num from subquery.
- Make sure to use WHERE appropriately to match code in countries and in subquery.
- Sort by lang_num in descending order.
*/

-- Select fields (with aliases)
SELECT code, COUNT(name) AS lang_num
  -- From languages
  FROM languages
-- Group by code
GROUP BY code;


-- Select fields
SELECT local_name, lang_num
  -- From countries
  FROM countries,
  	-- Subquery (alias as subquery)
  	(SELECT code, COUNT(name) AS lang_num
  	 FROM languages
  	 GROUP BY code) AS subquery
  -- Where codes match
  WHERE countries.code = subquery.code
-- Order by descending number of languages
ORDER BY lang_num DESC;
