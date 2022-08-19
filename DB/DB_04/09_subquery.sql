-- 가장 나이가 작은 사람의 수 
-- 1
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;
-- age  COUNT(*)
-- ---  --------
-- 15   39

-- 확인
SELECT MIN(age) 
FROM users;
-- MIN(age)
-- --------
-- 15

SELECT COUNT(*)
FROM users 
WHERE age = 15;
-- COUNT(*)
-- --------
-- 39

SELECT COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);
-- COUNT(*)
-- --------
-- 39  

-- 평균 계좌 잔고가 높은 사람 수?
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);
-- COUNT(*)
-- --------
-- 222 

-- 유은정과 같은 지역에 사는 사람 수는?
SELECT 
    country
FROM users
WHERE last_name = '유' AND first_name = '은정';
-- country
-- -------
-- 강원도 

SELECT COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '유' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 101  

-- 이은정과 같은 지역에 사는 사람 수는?
SELECT 
    country
FROM users
WHERE last_name = '이' AND first_name = '은정');
-- country
-- -------
-- 전라북도   
-- 경상북도 

SELECT COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 218   

-- 특정 성씨별로 가장 적은 나이 사람 모두 
-- 확인
SELECT last_name, MIN(age)
FROM users
GROUP BY last_name;

-- 결과
SELECT last_name, first_name, age
FROM users
WHERE (last_name, age) IN (SELECT last_name, MIN(age) FROM users
GROUP BY last_name)
ORDER BY last_name;
