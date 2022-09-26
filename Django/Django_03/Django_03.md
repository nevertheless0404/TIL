# Django

## Variable routing

- URL 주소를 변수로 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view를 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
- 변수는 `"<>"`에 정의하며 

```html
# articles/views.py

def hello(request, name):
	context = {
		'name': name,
}
	return render(request, 'hello.html',context)

<!-- aricles/templates/hello.html -->

{% extends 'base.hteml'%}

{% block content%}
	<h1>만나서 반가워요 {{ name }}님!</h1>
{% endblock %}
```

#### 주소(누구에게?) => "http://search.naver.com"

#### 주소(무엇을) =>  "/search.naver ?query=아이유"

http://search.naver.com/search.naver => form의 action에 정의한 내용

? query => input으로 정의한 내용 

````
<form action="https://www.google.com/search">
Google 검색어: <input type="Text" name="q">

````

/ping: form 태그 및 input 태그를 통해 사용자의 입력을 받아 /pong 이라는 페이지를 



## Django Template

### variable

- 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작 할 수 없음
- Dot(.)를 사용하여 변수 속성에 접근할 수 있음
- Render()의 세번째 인자로{'key':value} 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨 

### Filters

```
{{ variable|filter}}
```

- 표시할 변수를 수정할 때 사용

- ```
  {{ name|lower }}
  ```

- 60개의 built-in-template filters를 제공

- chained가 가능하며 일부 필터를 인자를 받기도 함

  ```
  {{ name|truncatewords:30 }}
  ```



### Tags

```
{% tag %}
```

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행 

- 일부 태그는 시작과 종료 태그가 필요

  ```
  {% if %}{% endif %}
  ```

- 약 24개의 built-in template tags를 제공



## GET 메서드 작성

- GET과 get 모두 대문자가 관계없이 동일하게 동작하지만 명시적 표현을 이해 대문자 사용을 권장
- 데이터를 입력 후 submit 버튼을 누르고 URL의 변화를 확인

````html
<!-- throw.html -->

{% extends 'base.html' %}
{% block content %}
	<h1>Throw</h1>
	<form action="#" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
</form>
{% endblock %}
````

