# 자바스크랩트

## Event

> 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

- 이벤트 역할
  - "~하면 ~한다"
  - "클릭하면, 경고창을 띄운다"
  - "특정 이벤트가 발생하면 할 일(함수)을 등록한다."

- EventTarget.`addEventListener()`

  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
  - 이벤트를 지원하는 모든 객체(Element, Document, Window)를 대상으로 지정 가능

- target.`addEventListener(Type, listener[, options])`

  - Type : 반응 할 이벤트 유형 (대소문자 구분 문자열 )

  - listener: 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체

    EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함

- Event.`preventDefault()`
  - 현재 이벤트의 기본 동작을 중단 
  - HTML 요소의 기본 동작을 작동하지 않게 막음
  - 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소 
    - ✔️ 이벤트의 취소 가능 여부 `event.cancelable`을 사용해 확인 할 수 있음 

### 대상에 특정이벤트가(type) 발생하면, 할일(listener)을 등록하자

```HTML
// button

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button id="btn">버튼</button>
  <p id="counter">0</p>
  <script>
    // 초기값
    let countNumber = 0;
    // ID가 btn인 요소를 선택
    const btn = documet.querySelector('#btn')
    console.log(btn)
    // btn이 클릭 되었을 때마다 함수가 실행됨
    btn.addEventlistener('click', function() {
      console.log('버튼 클릭!')
      // countNumber를 증가시키고 
      countNumber += 1
      // id가 counter안의 내용을 변경 시킨다.
      const document.querSelector('#counter')
      counter.innerText = countNumber
    })
  </script>
</body>
</html>
```

```html
// input

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
   <input type="text" id="text-input">
  <script>
    // 1. input 선택
    const textInput = documet.querySelector('#text-input')
    // 2.
    textInput.addEventListener('input', function(event) {
      // input의 value를 받아오고 싶음
      // input은 이벤트의 대상!
      // 이벤트가 타겟으로 들어감
      console.log(event)
      console.log(event.target.value)
    })
  </script>
</body>
</html>
```

```html
// prevent

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>정말 중요한 내용</h1>
  <p>lorem</p>
  <script>
    const h1 = document.querySelect('h1')
    h1.addEventListener('copy', function(event) {
      // event의 기본 동작을 막고, 
      event.preventDefalut()
      console.log('삐빅 복사를 할 수 없습니다.')
    })
    
    h1.addEventListener('click',function(event) {
      event.preventDefalut()
      console.log('드래그가 금지되어 있습니다.')
    })
  </script>
</body>
</html>
```

```html
// modal

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .modal-overlay {
      /* position */
      position: fixed;
      top: 0;
      left: 0;
      /* 배경색, 너비, 높이 */
      backgroud-color: rgba(0, 0, 0, 0.5);
      width: 100%
      height: 100vh
      /* 세부 내용 */
      color: white;
      display: flex;
      justify-content: center;
      align-itmes: center;
      /* 기본은 안보이게 */
      display: none;
    }
    .active {
      display: flex;
      transition: display 3;
    }
  </style>
</head>
<body>
  <button id="modal-btn">모달 버튼</button>
  <div class="modla-overlay">모달</div>
  	<buttn>취소 버튼</buttn>
  <script>
    const modalBtn = document.querySelector('#model-btn')
    // 모달 버튼이 클릭되면
    modalBtn.addEventListener('click', function() {
      // 모달 글씨가 나오게!
      // 클래스 active를 토글
      document.querySelector('#modal-content').classList.toggle('active')
    })
    
    // 모달 취소 버튼이 클릭되면
    const modalCancelBtn = document.querySelector('#modal-cancel-btn')
    modalCancelBtn.addEventListener('click',function(){
      document.querySelector('#modal-content').classList.toggle('active')
    })
    
    // 모달 오버레이를 클릭하면
    const modalOverlay = document.querySelector('#modal-content')
    modalOerlay.addEventListener('click', function(){
      document.querySelector('#modal-content').classList.toggle('active')
    })

    // 깔끔하게 정리
    // 모달 버튼이 클릭 되면
    const modalToggle = function(){
      document.querySelector('#modal-content').classList.toggle('active')
    }

    const modalBtn = document.querySelector('#model-btn')
    modalBtn.addEventListener('click', modalToggle)
    
    // 모달 취소 버튼이 클릭되면
    const modalCancelBtn = document.querySelector('#modal-cancel-btn')
    modalCancelBtn.addEventListener('click',modalToggle)
    
    // 모달 오버레이를 클릭하면
    const modalOverlay = document.querySelector('#modal-content')
    modalOerlay.addEventListener('click', modalToggle)
  </script>
</body>
</html>
```

```html
// carousel

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .carousel-items {
      position: relative;
      display: flex;
      width: 10rem;
      height: 10rem;
      overflow: hidden;
    }
    .carousel-item {
      position: absolute;
      top: 0;
      width: 10rem;
      height: 10rem;
      background-color: bisque;
      display: none;
    }
    .active {
      display: block;
      animation: active 1.5s;
    }
    @keyframes active {
      0% {
        transform: translateX(100%);
      }
      100% {
        transform: translateX(0);
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="carousel-items">
      <div class="carousel-item active">1</div>
      <div class="carousel-item">2</div>
      <div class="carousel-item">3</div>
      <div class="carousel-item">4</div>
    </div>
  </div>
    <button id="nextBtn">next</button>
  <script>
    const nextBtn = document.querySelector('#nextBtn')
    nextBtn.addEventListener('click', function() {
      // 지금 active인 것은 어떻게 암..?
      const currentElement = document.querySelector('.active')
      // 전체 item 중에 ... 이 Element의 인덱스?????
      const items = document.querySelectorAll('.carousel-item')
      const idx = [...items].indexOf(currentElement)
      console.log(currentElement, items, idx)
      currentElement.classList.toggle('active')
      items[(idx+1)%items.length].classList.toggle('active')
    })
  </script>
</body>
</html>
```

