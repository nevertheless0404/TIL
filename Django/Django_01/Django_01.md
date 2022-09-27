# .Django

## 개발 환경 만들기 

1. Django 프로젝트 관리를 위한 디렉토리 생성

````
> mkdir djangoPrj01 <-(디렉토리 이름)
````

2. 가상환경 만들기
   - 생성성된 디렉토리로 이동 (cd  djangoPrj01)로 이동하여 장고를 위한 가상 환경 만들기

````
djangoPrj01> python3 -m venv (venv01) <- 가상환경이름

<전체>
> mkdir djangoPrj01
> cd  djangoPrj01
/djangoPrj01 > ls
/djangoPrj01 > python -m venv venv01
/djangoPrj01 >ls
venv01
/djangoPrj01  > cd venv01
djangoPrj01/venv01  > ls
bin		include		lib		pyvenv.cfg
````

3. 가상환경 활성화 하기

````
> cd ~
> cd djangoPrj01
djangoPrj01> source venv01/bin/activate
(venv01) .../djangoPrj01  
````

4. 장고 설치하기

````
(venv01) djangoPrj01> pip install django==3.2.13 
````

5. 장고 프레임워크 로드하기

````
(venv01) djangoPrj01> django-admin startproject web01 .
(venv01) djangoPrj01> ls
manage.py. venv01  web01
(venv01) djangoPrj01> cd web01
(venv01) djangoPrj01> ls
__init__.py settings.py urls.py.  wsgi.py
(venv01) djangoPrj01>
````

6. 구동하기!

````
(venv01) djangoPrj01> python manage.py runserver
````

7. Locahost:8000 을 브라우저에 넣기



## 서버 기초

Q. IP와 도메인은 무엇일까요?

- IP => 인터넷 프로토콜을 나타냄  ('google.com')

- 도메인 => 사람이 읽을 수 있는 IP 주소의 이름을 지정 ('173.194.121.32')



Q. 클라이언트와 서버는 무엇일까요?

> 웹에 연결된 컴퓨터는 클라이언트와 서버라고 함

- 클라이언트  =>인터넷이 연결된 장치들(WIFI, 모바일 네트워크) 과 이용가능한 윕에 접근하는 소프트웨어

- 서버 => 웹페이지, 사이트, 또는 앱을 저장하는 컴퓨터 



Q. 정적 웹 사이트와 동적 웹 사이트의 차이점은 무엇일까요? Django는 무엇을 위한 도구인가요?

- 정적 웹 사이트 => 사용자가 페이지를 탐색하거나, 브라우저가 지정된 URL에서 HTTP "GET"요청을 보낼 때 서버는 파일 시스템에서 요청한 문서를 검색하고 문서와 success status 를 포함한 HTTP응답을 반환

- 동적 웹 사이트 => 동적 웹 사이트는 필요할 때에 동적으로 응답 콘텐츠가 생성, 사용자또는 저장된 환경을 기반으로 URL에 대해 다른 데이터를 반환 할 수 있으며, 응답을 반환하는 과정에서 다른 작업을 수행 할 수 있음

- Django => 웹 프레임 워크는 다른 유용한 도구와 함께 즉시 사용할 수 있는 도구를 제공



Q. HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?

-  **HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는** 프로토콜, HTTP는 웹에서 이루어지는 모든 데이터 교환의 기초이며, 클라이언트-서버 프로토콜이기도 함

- 요청 

  -  HTTP메서드, 클라이언트가 수행하고자 하는 동작을 정의한 GET,POST 같은 동사나 OPTIONS나 HEAD와 같은 명사
  - HTTP 프로토콜의 버전
  - POST와 같은 몇 가지 메서드를 위한, 전송된 리소스를 포함하는 응답의 본문과 유사한 본문

  

- 응답 
  - HTTP 프로토콜의 버전
  - 요청의 성공 여부과, 그 이유를 나타내는 상태 코드
  - 아무런 영향력이 없는, 상태 코드의 짧은 설명을 나타내는 상태 메시지
  - 가져온 리소스가 포함되는 본문



Q. 프레임워크는 무엇일까요?

- 어떤한 목적을 달성하기 위해 복잡하게 얽혀있는 문제를 해결하기 위한 구조, 소프트웨어 개발에 있어 하나의 뼈대 역할을 함

