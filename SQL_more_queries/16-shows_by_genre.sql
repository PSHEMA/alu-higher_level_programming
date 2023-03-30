-- A script that lists all shows and all genres linked to them
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.tv_show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
