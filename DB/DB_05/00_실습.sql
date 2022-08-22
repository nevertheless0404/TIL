-- playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력
SELECT *
FROM playlist_track A
ORDER BY A.playlistId DESC LIMIT 5;

-- tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력 
SELECT * 
FROM tracks B
ORDER BY B.TrackID ASC LIMIT 5;

-- 각 playlist_track 해당하는 track 데이터를 함께 출력
SELECT A.playlistId, B.Name FROM playlist_track A
JOIN  tracks B 
ON A.TrackId = B.TrackId
ORDER BY playlistId DESC LIMIT 10;

--`PlaylistId`가 `10`인 track 데이터를 함께 출력
SELECT A.playlistId, B.Name FROM playlist_track A
JOIN tracks B
ON A.TrackId = B.TrackId
WHERE A.playlistId = 10
ORDER BY B.Name DESC LIMIT 5;

-- tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 
-- `INNER JOIN`해서 데이터를 출력
SELECT COUNT(*) FROM tracks A
JOIN artists B
ON A.Composer = B.Name;

-- tracks 테이블을 기준으로 tracks `Composer` 와 
-- artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력
SELECT COUNT(*) FROM tracks A
LEFT JOIN artists B
ON A.Composer = B.Name;

-- invoice_items 테이블의 데이터를 출력
SELECT InvoiceLineId, InvoiceId FROM invoice_items 
ORDER BY InvoiceId LIMIT 5;

-- invoices 테이블의 데이터를 출력
SELECT InvoiceId, CustomerId FROM invoices 
ORDER BY InvoiceId LIMIT 5;

-- 각 invoices_item에 해당하는 invoice 데이터를 함께 출력
SELECT A.InvoiceLineId, B.InvoiceId FROM invoice_items A
JOIN invoices B 
ON A.InvoiceId = B.InvoiceId
ORDER BY B.InvoiceId DESC LIMIT 5;

-- 각 invoice에 해당하는 customer 데이터를 함께 출력
SELECT A.InvoiceId, B.CustomerId FROM invoices A
JOIN customers B
ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 각 invoices_item(상품)을 포함하는 invoice(송장)와 
-- 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력
SELECT A.InvoiceLineId, B.InvoiceId, C.CustomerId 
FROM invoice_items A
JOIN invoices B 
ON A.InvoiceId = B.InvoiceId 
JOIN customers C
ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 각 cusotmer가 주문한 invoices_item의 개수
SELECT C.CustomerId, COUNT(*) FROM invoice_items A
JOIN (SELECT * FROM invoices A
JOIN customers B 
ON A.CustomerId = B.CustomerId) C
ON A.InvoiceId = C.InvoiceId 
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC LIMIT 5;

