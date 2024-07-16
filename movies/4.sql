SELECT COUNT(movies.id) FROM movies WHERE movies.id IN (SELECT movie_id FROM ratings WHERE rating = 10.0);
