SELECT title, rating FROM movies
JOIN ratings on movies.id = ratings.movie_id
WHERE movies.year = 2010 AND ratings.rating NOT NULL
ORDER BY ratings.rating DESC, title
LIMIT 30;
