# Axiso 

- 브라우저를 위한 Promise 기반의 클라이언트 

- "XHR" 이라는 브라우저 내장 객체를 활용해 AJAX 요청을 처리하는데, 이보다 편리한 AJAX 요청이 가능하도록 도움을 줌 
  - 확장 가능한 인터페이솨 함께 패키지로 사용이 간편한 라이브러리를 제공

````django
<!--XMLHttpRequest-->

<script>
	const xhr = new XMLHttpRequest()
	const URL = 'https://jsonplaceholder.typicode.com/todos/1'
  
	xhr.open('GET', URL)
	xhr.send()

	xhr.onreadystatechange = function (event) {
		if (xhr.readyState === XMLHttpRequest.DONE) {
			const status = event.target.status
			if (status === 0 || (status >= 200 && status < 400)) {
				const res = event.target.response
				const data = JSON.parse(res)
				console.log(data.title)
			} else {
				console.error('Error!')
			}
		}		
	}
</script>
````

```django
<!--Axios-->

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
	const URL = 'https://jsonplaceholder.typicode.com/todos/1'
  
	axios.get(URL)
		.then(res => console.log(res.data.title))
		.catch(err => console.log('Error!’))
</script> 
```



### promise

- 비공기 작업을 관리하는 객체 
  - 미래의 완료 또는 실패와 그 결과 값을 나타냄
  - 미래의 어떤 상황에 대한 약속 

- 성공(이행)에 대한 약속
  - `.then(callback)`
    - 이전 작업(promise)이 성공했을 때(이행했을 때) 수행할 작업을 나타내는 callback 함수
    - 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음
    - 성공했을 때의 코드를 callback 함수 안에 작성

- 실패(거절)에 대한 약속
  - `.catch(callback)`
    - .then이 하나라도 실패하면(거부 되면) 동작 (동기식의 'try - except' 구문과 유사)
    - 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있음

- 각각의 `.then()` 블록은 서로 다른 promise를 반환
  - `.then()`을 여러 개 사용(chaining)하여 연쇄적인 작업을 수행할 수 있음
  - 여러 비동기 작업을 차례대로 수행할 수 있다는 뜻

- `.then()`과 `.catch()` 메서드는 모두 promise를 반환하기 때문에 chaining 가능
  - **반환 값이 반드시 있어야 함**
  - **없다면 callback 함수가 이전의 promise 결과를 받을 수 없음**

- `.finally(callback)`

  - Promise 객체를 반환
  - 결과와 상관없이 무조건 지정된 callback 함수가 실행
  - 어떠한 인자도 전달받지 않음
    - promise가 성공되었는지 거절되었는지 판단할 수 없기 때문

  - 무조건 실행되어야 하는 절에서 활용
    - `.then()`과 `.catch()`블록에서의 코드 중복을 방지

- .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining) 
- callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음 
- Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨 
- 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용한 경우도 마찬가지



## 비동기 적용하기 

> 자바스크립트의 비동기 처리란 특정 토드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 자바스크립트의 특성을 의미



### 콜백 함수 

> 데이터가 준비된 시점에서만 저희가 원하는 동작(특정 값을 출력한다 등)을 수행함 

#### 콜백 지옥 (Callback hell)

```js
$.get('url', function(response) {
      parseValue(response, function(id) {
  auth(id, function(result) {
    display(result, function(text) {
      console.log(text);
    	});
  	});
	});
});
```

- 가독성도 떨어지고 로직 변경도 어려움 

#### 콜백 지옥 해결

```js
function parseValueDone(id) {
  auth(id, authDone);
}
function authDone(result) {
  display(result, displayDone);
}
function displayDone(text) {
  console.log(text);
}
$.get('url', function(response) {
  parseValue(response, parseValueDone);
});
```

- 일반적으로 콜백 지옥을 해결하는 방법에는 Promise나 Async를 사용하는 방법이 있습니다. 만약 코딩 패턴으로만 콜백 지옥을 해결하려면 아래와 같이 각 콜백 함수를 분리
- ajax 통신으로 받은 데이터를 parseValue() 메서드로 파싱 합니다. parseValueDone()에 파싱 한 결과값인 id가 전달되고 auth() 메서드가 실행됩니다. auth() 메서드로 인증을 거치고 나면 콜백 함수 authDone()이 실행됩니다. 인증 결과 값인 result로 display()를 호출하면 마지막으로 displayDone() 메서드가 수행되면서 text가 콘솔에 출력



### 팔로우(follow)

- **date-test-value** 라는 이름의 특성을 지정했다면 JavaScript 에서 **element.dateset.testValue** 로 접근할 수 있음

- 속성명 작성 시 주의사항
  - 대소문자 여부에 상관없이 xml 시작하면 안 됨
  - 세미콜론을 포함해서는 안됨
  - 대문자를 포함해서는 안됨

- 팔로우 버튼을 토글하기 위해서는 현재 팔로우가 된 상태인지 여부 확인이 필요 
- Axis 요청을 통해 받는 response 객체를 활용해 view 함수를 통해서 팔로우 여부를 파악 할 수 있는 변수를 담아 JSON 타입으로 응답하기

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
		if request.user.is_authenticated:
				User = get_user_model()
				me = request.user
				you = User.objects.get(pk=user_pk)
				if me != you:
						if you.followers.filter(pk=me.pk).exists():
							 you.followers.remove(me)
							 is_followed = False
						else:
							you.followers.add(me)
							is_followed = True
						context = {
								'is_followed': is_followed,
								'followers_count': you.followers.count(),
								'followings_count': you.followings.count(),
						}
						return JsonResponse(context)
				return redirect('accounts:profile', you.username)
		return redirect('accounts:login')
```

````javascript
<!-- accounts/profile.html -->
const form = document.querySelector('#follow-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

form.addEventListener('submit', function (event) {
	event.preventDefault()
	const userId = event.target.dataset.userId

  axios({
		method: 'post＇,
		url: `/accounts/${userId}/follow/`,
		headers: {'X-CSRFToken': csrftoken,}
})
	.then((response) => {
	const isFollowed = response.data.is_followed
	const followBtn = document.querySelector('#follow-form > input[type=submit]＇)
	if (isFollowed === true) {
		followBtn.value = '언팔로우＇
	} else {
		followBtn.value = '팔로우＇
	}
	const followersCountTag = document.querySelector('#followers-count＇)
	const followingsCountTag = document.querySelector('#followings-count＇)
	const followersCount = response.data.followers_count
	const followingsCount = response.data.followings_count
	followersCountTag.innerText = followersCount
	followingsCountTag.innerText = followingsCount
})
  .catch((error) => {
	console.log(error.response)
	})
})
````