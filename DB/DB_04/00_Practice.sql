
-- 모든 데이블의 이름을 출력
.tables

-- 앨범(albums) 테이블의 데이터를 출력
SELECT AlbumID, Title, ArtistID
FROM albums 
ORDER BY Title DESC LIMIT 5;

-- 고객(customers) 테이블의 행 개수를 출력
SELECT COUNT(*) AS "고객 수" FROM customers;

-- 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력
SELECT FirstName, LastName
FROM customers
WHERE Country = 'USA'
ORDER BY FirstName DESC LIMIT 5;

-- 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력
SELECT COUNT(*) AS "송장수" FROM invoices
WHERE BillingpostalCode IS NOT NULL;

-- 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력
SELECT * FROM invoices
WHERE BillingState ISNULL ORDER BY InvoiceDate DESC LIMIT 5;
-- InvoiceId  CustomerId  InvoiceDate          BillingAddress                            BillingCity   BillingState  BillingCountry  BillingPostalCode  Total
-- ---------  ----------  -------------------  ----------------------------------------  ------------  ------------  --------------  -----------------  -----
-- 412        58          2013-12-22 00:00:00  12,Community Centre                       Delhi                       India           110017             1.99 
-- 411        44          2013-12-14 00:00:00  Porthaninkatu 9                           Helsinki                    Finland         00530              13.86
-- 410        35          2013-12-09 00:00:00  Rua dos Campeões Europeus de Viena, 4350  Porto                       Portugal                           8.91 
-- 404        6           2013-11-13 00:00:00  Rilská 3174/6                             Prague                      Czech Republic  14300              25.86
-- 403        56          2013-11-08 00:00:00  307 Macacha Güemes                        Buenos Aires                Argentina       1106               8.91 

-- 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력
SELECT COUNT(*) FROM invoices WHERE strftime('%Y', InvoiceDate) = '2013';

-- 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력
SELECT CustomerID, FirstName, LastName FROM customers WHERE FirstName LIKE 'L%' ORDER BY CustomerID ASC;

-- 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력
SELECT COUNT(Country) AS "고객 수", Country AS "나라"
FROM customers GROUP BY Country ORDER BY COUNT(Country) DESC LIMIT 5;

-- 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력
SELECT ArtistId, COUNT(*) FROM albums GROUP BY ArtistId 
ORDER BY COUNT(ArtistID) 
DESC LIMIT 1;

-- 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력
SELECT ArtistId, COUNT(*) FROM albums GROUP BY ArtistId HAVING COUNT(ArtistId) >= 10
ORDER BY COUNT(ArtistId) DESC;

-- 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 
-- 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력
SELECT COUNT(*) AS "고객수", Country, State FROM customers WHERE State != '' GROUP BY Country, State
ORDER BY COUNT(*) DESC, Country DESC LIMIT 5;

-- 고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력
SELECT CustomerId, 
CASE 
WHEN Fax ISNULL THEN 'X'
WHEN Fax != '' THEN 'O'
END AS "Fax유/무"
FROM customers
ORDER BY customerId ASC LIMIT 5;

-- 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력
SELECT LastName, FirstName, DATETIME("now")- CAST(BirthDate AS DATETIME) +1
"나이" FROM employees ORDER BY EmployeeId;

-- 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력
SELECT ArtistId, Name 
FROM artists 
WHERE ArtistId = 
(SELECT ArtistId FROM albums 
GROUP BY ArtistId ORDER BY COUNT(*) DESC LIMIT 1);

-- 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력
SELECT GenreId, Name
FROM Genres
WHERE GenreId =
(SELECT GenreId FROM tracks GROUP BY GenreId ORDER BY COUNT(*) ASC LIMIT 1);

