-- Топ-10 самых добавляемых артистов
SELECT s.ArtistName, SUM(f.AddCount) AS total_adds, COUNT(DISTINCT p.UserID) AS unique_users_add
FROM FactPlaylistAdd AS f
JOIN DimSongs AS s ON f.SongSK = s.SongSK
JOIN DimPlaylists AS p ON f.PlaylistSK = p.PlaylistSK
GROUP BY s.ArtistName
ORDER BY total_adds DESC
LIMIT 10;


-- Среднее кол-во песен в плейлистах и их средняя продолжительность
WITH playlist_aggs AS (
    SELECT PlaylistSK, SUM(AddCount) AS songs_in_playlist, SUM(SongDurationSeconds) / 60 AS total_minutes
    FROM FactPlaylistAdd
    GROUP BY PlaylistSK
)
SELECT ROUND(AVG(songs_in_playlist), 1) AS avg_songs_per_playlist,
ROUND(AVG(total_minutes), 1) AS avg_playlist_duration_minutes
FROM playlist_aggs;


-- Статистика добавлений песен в плейлисты по годам, кварталам и дням недели
SELECT c.Year, c.Quarter, c.DayOfWeek, SUM(f.AddCount) AS total_adds
FROM FactPlaylistAdd AS f
JOIN DimCalendar AS c ON f.DateKey = c.DateID
GROUP BY c.Year, c.Quarter, c.DayOfWeek
ORDER BY c.Year DESC, c.Quarter DESC, total_adds DESC;


-- Топ-5 пользователей по добавлению песен из уникальных альбомов в плейлисты в 2020 году
SELECT p.UserName, p.UserEmail, SUM(f.AddCount) AS total_songs_add, COUNT(DISTINCT s.AlbumSK) as unique_albums_viewed
FROM FactPlaylistAdd AS f
JOIN DimPlaylists AS p ON f.PlaylistSK = p.PlaylistSK
JOIN DimSongs AS s ON f.SongSK = s.SongSK
JOIN DimCalendar AS c ON f.DateKey = c.DateID
WHERE c.Year = 2020
GROUP BY p.UserName, p.UserEmail
ORDER BY unique_albums_viewed DESC
LIMIT 5;