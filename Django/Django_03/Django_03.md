# Django

## Variable routing

- URL 주소를 변수로 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view를 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
- 변수는 `"<>"`에 정의하며 



#### 주소(누구에게?) => "http://search.naver.com"

#### 주소(무엇을) =>  "/search.naver ?query=아이유"

http://search.naver.com/search.naver => form의 action에 정의한 내용

? query => input으로 정의한 내용 

````
<form action="https://www.google.com/search">
Google 검색어: <input type="Text" name="q">

````

/ping: form 태그 및 input 태그를 통해 사용자의 입력을 받아 /pong 이라는 페이지를 