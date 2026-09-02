# Таблицы #

## Измерения ##

1\. __Table Name: DimSongs__
  * **Attributes**:
      - *SongSK*: INTEGER, PK, NOT NULL, UNIQUE
      - *SourceSongID*: INTEGER, NOT NULL
      - *SongTitle*: VARCHAR(100), NOT NULL
      - *DurationSeconds*: INTEGER, NOT NULL
      - *AlbumID*: INTEGER
      - *AlbumTitle*: VARCHAR(100)
      - *AlbumReleaseDate*: DATE
      - *ArtistID*: INTEGER, NOT NULL
      - *ArtistName*: VARCHAR(100), NOT NULL
  * **Constraints**:
      - *PK_DimSongs*: PRIMARY KEY ( SongSK )

2\. __Table Name: DimPlaylists__
  * **Attributes**:
      - *PlaylistSK*: INTEGER, PK, NOT NULL, UNIQUE
      - *SourcePlaylistID*: INTEGER, NOT NULL
      - *PlaylistTitle*: VARCHAR(100), NOT NULL
      - *UserID*: INTEGER, NOT NULL
      - *UserName*: VARCHAR(100), NOT NULL
      - *UserEmail*: VARCHAR(255), NOT NULL
  * **Constraints**:
      - *PK_DimPlaylist*: PRIMARY KEY ( PlaylistSK )

3\. __Table Name: DimDates__
  * **Attributes**:
      - *DateID*: INTEGER, PK, NOT NULL, UNIQUE
      - *FullDate*: DATE, NOT NULL
      - *DayOfWeek*: INTEGER, NOT NULL
      - *Month*: INTEGER, NOT NULL
      - *Quarter*: INTEGER, NOT NULL
      - *Year*: INTEGER, NOT NULL
  * **Constraints**:
      - *PK_DimDate*: PRIMARY KEY ( DateID )

## Факты ##

4\. __Table Name: FactPlaylistAdd__
  * **Attributes**:
      - *PlaylistAddID*: INTEGER, PK, NOT NULL, UNIQUE
      - *DateKey*: INTEGER, FK (REFERENCES DimDates), NOT NULL
      - *PlaylistSK*: INTEGER, FK (REFERENCES DimPlaylists), NOT NULL
      - *SongSK*: INTEGER, FK (REFERENCES DimSongs), NOT NULL
      - *AddCount*: INTEGER, NOT NULL, DEFAULT 1
  * **Constraints**:
      - *PK_FactPlaylistAdd*: PRIMARY KEY ( PlaylistAddID )
      - *FK_FactPlaylistAdd_DimDate*: FOREIGN KEY ( DateKey ) REFERENCES DimDates ( DateID )
      - *FK_FactPlaylistAdd_DimPlaylists*: FOREIGN KEY ( PlaylistSK ) REFERENCES DimPlaylists ( PlaylistSK )
      - *FK_FactPlaylistAdd_DimSongs*: FOREIGN KEY ( SongSK ) REFERENCES DimSongs ( SongSK )


# Схема #

![image](/images/dwh_schema.png)


# Примеры запросов #

```sql
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
```