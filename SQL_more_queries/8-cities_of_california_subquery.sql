-- lists all the cities of California that can be found.
SELECT id, name
FROM cities
WHERE cities_id = (
	SELECT id
	FROM states
	WHERE name = 'California')
GROUP BY id ORDER BY id ASC;
