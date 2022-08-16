-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- 나이 그룹이 10미만인 사람의 수 
SELECT COUNT(*) FROM healthcare WHERE age < 10;

-- 성별이 1인 사람의 수
SELECT COUNT(*) FROM healthcare WHERE gender =1;

-- 흡연수치가 3이면서 음주가 1인 사람의 수를 출력 
SELECT COUNT(*) FROM healthcare WHERE smoking=3 AND is_drinking=1;

-- 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 AND va_right >= 2.0; 

-- 시도(sido)를 모두 중복 없이 출력
SELECT DISTINCT sido FROM healthcare;

-- 몸무게가 50 이상이면서 키가 160 이상인 사람 수를 출력
SELECT COUNT(*) FROM healthcare WHERE weight >= 50 AND height >= 60;
