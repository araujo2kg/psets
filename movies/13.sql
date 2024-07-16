SELECT name FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.id IN
(SELECT stars.movie_id FROM stars WHERE stars.person_id IN
(SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958))
GROUP BY name
HAVING name <> 'Kevin Bacon';
