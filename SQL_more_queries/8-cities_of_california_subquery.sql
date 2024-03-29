-- A script that lists all cities of California that can be found in the database
SELECT cities.id, cities.name
FROM cities, states
WHERE states.name = 'California' AND cities.state_id = states.id
ORDER BY cities.id ASC;
