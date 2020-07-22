/*
Instructions
- Get the title and net profit (the amount a film grossed, minus its budget) for all films. Alias the net profit as net_profit.
- Get the title and duration in hours for all films. The duration is in minutes, so you'll need to divide by 60.0 to get the duration in hours. Alias the duration in hours as duration_hours.
- Get the average duration in hours for all films, aliased as avg_duration_hours.
*/

SELECT title, (gross - budget) AS net_profit
FROM films;

SELECT title, (duration / 60.0) AS duration_hours
FROM films;

SELECT AVG(duration) / 60.0 AS avg_duration_hours
FROM films;
