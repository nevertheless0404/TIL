-- AC/DC의 모든 앨범
-- AC/DC (artists)
-- 앨범(albums)

-- 앨범 검색하려고 했는데..
-- 아티스는 id로 저장되어있네요.
-- AC/DC는 아는데 ID를 모름

-- id 조회
SELECT ArtistID
FROM artists
WHERE Name = 'AC/DC';
-- rtistId
-- --------
-- 1   

-- 서브쿼리
SELECT * 
FROM albums
WHERE ArtistId = (SELECT ArtistId 
FROM artists
WHERE Name = 'Cake');
-- AlbumId  Title                       ArtistId
-- -------  --------------------------  --------
-- 260      Cake: B-Sides and Rarities  196