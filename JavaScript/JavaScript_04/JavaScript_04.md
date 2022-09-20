# 자바스트랩트

## JavaScript Library 활용

````html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>프로젝트</title>
  <style>
    .ball {
      width: 10rem;
      height: 10rem;
      backgroud-color: yellowgreen;
      border-radius: 50%;
      text-align: center;
      line-height: 10rem;
      font-size: xx-large;
      font-weight: bold;
    }
    .ball-container {
      display: flex;
    }
  </style>
</head>
<body>
  <h1>로또 추천 번호</h1>
  <div class="ball">5</div>
  
  <script>
    const button = document.querySelector('#lotto-btn')
    button.addEventListener('clikc',function(){
      // 요소를 만들어서
      const ballContainer = document.createElement('div')
      ballContainer.classList.add('ball-container')
      // 공을 만들어서
      const ball = document.creatElement('div')
      ball.classList.add('ball')
      ball.innerText = 5
      // 컨테이너에 붙인다.
      ballContainer.appendChild(ball)
      // 컨테이너를 결과 영역에 붙인다.
      const result = document.querySelector('#result')
      result.appendChild(ballContainer)
      })
  </script>
</body>
</html>
````