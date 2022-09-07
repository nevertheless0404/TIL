# Bootstrap

## Grid System

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본 요소
  - Column : 실제 컨텐츠를 포함하는 부분
  - Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
  - Container : column들을 담고 있는 공간 



## Bootstrap grid system 

- Bootstrap Grid system은 flexbox로 제작됨 
- container, rows, column으로 컨텐츠를 배치하고 정렬
- 그리드 옵션
  - Extra small (xs)
  - Small (sm)
  - Medium (md)
  - Large (lg)
  - Extra large (xl)
  - Extra extra large (xxl)
- **⭐️ 반드시 기억해야 할 2가지!**
  - 12개의 colum
  - 6개의 grid breakponits 

````html
     <h2>기본</h2>
    <!-- flex만 한 일반적인 box의 배치 -->
    <div class="d-flex">
      <div class="box">col</div>
      <div class="box">col</div>
      <div class="box">col</div>
    </div>
    <!--Bootstrap grid System, 자동으로 화면에서 12등분 된 화면을 균등하게 나눠가짐 -->
    <div class="row my-3">
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
    </div>
    <!-- 4개로 늘려도 화면에 맞게 나눠짐 -->   
    <div class="row my-3">
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
    </div>
    
    <div class="row my-3">
      <div class="col-2"><div class="box">col-2</div></div>
      <div class="col-6"><div class="box">col-6</div></div>
    </div>     
    <!-- 12를 넘으면 아래로 흘러내려감 -->   
    <div class="row my-3">
      <div class="col-5"><div class="box">col-5</div></div>
      <div class="col-6"><div class="box">col-6</div></div>
      <div class="col-4"><div class="box">col-4</div></div>
    </div>   
    
    <!-- 총 6개 배치를 할건데, 한 줄에 가장 작은 화면 : 한개, 모바일 : 2개, 태블릿 : 3개, PC : 4개를 보여주게 하고싶다면? -->
    <h2>breakpoint</h2>
    <div class="row my-3"> 
      <div class="col-12 col-sm6 col-md-4 col-lg-3">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm6 col-md-4 col-lg-3">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm6 col-md-4 col-lg-3">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm6 col-md-4 col-lg-3">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm6 col-md-4 col-lg-3">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm6 col-md-4 col-lg-3">
        <div class="box">col</div>
      </div>
  </div>
  <h2>offset</h2>
  <div class="row my-3">
    <div class="col-4">
      <div class="box">col-4</div>
    </div>
    <div class="col-4 offset-4">
      <div class="box">col-4</div>
    </div>
    <div class="col-3">
      <div class="box">col-3</div>
    </div>
    <div class="col-3 offset-3">
      <div class="box">col-3</div>
    </div>
    <h2>Gutter vs no_gutter</h2>
    <div class="row my-3">
      <div class="col-6"><div class="box">col-6</div></div>
      <div class="col-6"><div class="box">col-6</div></div> 
    </div>
    <div class="row g-0 my-3">
      <div class="col-6"><div class="box">col-6</div></div>
      <div class="col-6"><div class="box">col-6</div></div> 
    </div>
````

| Extra small <576px                     | Small ≥576px                         | Medium ≥768px | Large ≥992px | Extra large ≥1200px |            |
| -------------------------------------- | ------------------------------------ | ------------- | ------------ | ------------------- | ---------- |
| Max container width 실제 적용되는 너비 | None (auto)                          | 540px         | 720px        | 960px               | 1140px     |
| Class prefix                           | `.col-`                              | `.col-sm-`    | `.col-md-`   | `.col-lg-`          | `.col-xl-` |
| # of columns                           | 12분할                               |               |              |                     |            |
| Gutter width                           | 30px (15px on each side of a column) |               |              |                     |            |
| Nestable                               | Yes                                  |               |              |                     |            |
| Column ordering                        | Yes                                  |               |              |                     |            |



## Box model 박스모델

- margin : border를 기준으로 박스의 여백을 지정, 시각적인 요소는 없음
- border : 박스의 테두리
- padding : 테두리와 content간의 간격
- content : 엘리먼트 안에 포함되는 컨텐츠

![스크린샷 2022-09-07 오후 4.06.10](/Users/yuyeong/Desktop/TIL/WEB/WEB_07/WEB_07.assets/스크린샷 2022-09-07 오후 4.06.10.png)

### M/P

- M : Margin
- P : Padding

### t , b , l , r ,x , y

- t : top
- b : bottom
- l : left
- r : right
- x : x축 -> left , right
- y : y축 -> top , bottom

### 0, 1, 2, 3, 4, 5, auto

- 0 : 0
- 1 : .25rem( font-size가 16px이면, 4px) 크기
- 2 : .5rem( font-size가 16px이면, 8px) 크기
- 3 : 1rem( font-size가 16px이면, 16px) 크기
- 4 : 1.5rem( font-size가 16px이면, 24px) 크기
- 5 : 3rem( font-size가 16px이면, 48px) 크기
- auto : margin의 자동으로 세팅

### n1, n2, n3, n4, n5

- n : negative을 의미
- n1 : -.25rem( font-size가 16px이면, -4px) 크기
- n2 : -.5rem( font-size가 16px이면, -8px) 크기
- n3 : -1rem( font-size가 16px이면, -16px) 크기
- n4 : -1.5rem( font-size가 16px이면, -24px) 크기
- n5 : -3rem( font-size가 16px이면, -48px) 크기