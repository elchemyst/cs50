SELECT COUNT(*) AS Rating_10 FROM movies
  JOIN ratings ON movies.id = ratings.movie_id
 WHERE rating = 10;
