# [WEB]

## CSS Position 

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때 는 부모 요소의 위치를 기준으로 배치 됨

- 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능

  1. relative : 상대 위치 
     - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
     - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)
  2. absolute : 절대 위치
     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
     - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동 )
  3. Fixed : 고정 위치
     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
     - 부모 요소와 관계없이 viewport를 기준으로 이동
     - 스크롤 시에도 항상 같은 곳에 위치

  4. sticky : 스크롤에 따라 static -> fixed로 변경
     - 속성을 적용한 박스는 평소에 문서 안에서 position : static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position : fixed와 같이 박스를 화면에 고정할 수 있는 속성



- absolute vs relative

````html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meat name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
    <style>
      .parent{
        width: 10rem;
        height: 10rem;
        border: 1px solid red;
      }
      .child{
        width: 10rem;
        height: 1rem;
        backgroud-color: bisque;
      }
      .relative{
        position: relative;
        top: 4rem;
      }
      .absolute {
        position: absolute;
        top: 4rem;
      }
      .parent-relative {
        position: relative;
      }
    </style>
  </head>
  <body>
    <!-- 기본 -->
    <div class="parent">
      <div class="child"></div>
    </div>
    <div class="parent">
      <div class="child relative"><div>
      <div class="child"></div>
     </div>
     <!-- absolute -->
     <div class="parent parent-relative">
       <div class="child absolute"></div>
       <div class="child"></div>
        </div>  
</body>
</html>
````

### position sticky

- Sticky: 스크롤에 따라 static -> fixed로 변경
  - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐르에 따르지만, 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성
  - 일반적으로 Navigation Bar에서 사용됨



## CSS 원칙

- CSS 원칙: Normal flow
  - 모든 요소는 네모(박스모델), 좌측상단에 배치
  - display에 따라 크기와 배치가 달라짐

- CSS 원칙 2
  - **position으로 위치의 기준을 변경**
    - Relative: 본인의 원래 위치
    - Absolute: 특정 부모의 위치
    - Fixed: 화면의 위치
    - Sticky: 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경 



## Flexbox

### CSS Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축 
  - Main axis (메인 축)
  - cross axis (교차 축)

- 구성 요소
  - Flex Container(부모 요소)
  - Flex item (자식요소)

![스크린샷 2022-08-31 오후 2.39.26](/Users/yuyeong/Desktop/TIL/WEB/WEB_03/WEB_03.assets/스크린샷 2022-08-31 오후 2.39.26.png)

![01](/Users/yuyeong/Desktop/TIL/WEB/WEB_03/WEB_03.assets/01.png)

- [출처](https://ostraining.com/blog/webdesign/css-flexbox-3-the-align-items-property/)

### Flexbox 구성 요소

- Flex Container(부모 요소)
  - flexbox 레이아웃을 형성한느 가장 기본적인 모델
  - Flex Item 들이 놓여 있는 영역
  - Display 속성을 flex 혹은 inline-flex로 지정

- Flex Item (자식 요소)
  - 컨테이너에 속해 있는 컨텐츠(박스)

````css
<!-- flexbox 시작 -->
.flex-container{
		display: flex;
}
````



### Flex 속성

- 배치 설정
  - Flex-direction 
  - Flex-wrap

- 공간 나누기
  - Justify-content (main axis)
  - Align-content (cross axis)

- 정렬
  - Align-items (모든 아이템을 cross axis 기준으로 )
  - Align-self (개별 아이템)

#### align-items

- 모든 아이템을 Cross axis 를 기준으로 정렬
- Flex-direction: row 좌에서 우 

![images_bochodev_post_21522fb9-35fe-4b7b-afbb-da2d84a346a2_justify-content](/Users/yuyeong/Desktop/TIL/WEB/WEB_03/WEB_03.assets/images_bochodev_post_21522fb9-35fe-4b7b-afbb-da2d84a346a2_justify-content.svg)

- [출처](https://velog.io/@bochodev/CSS-%EA%B8%B0%EC%B4%887)



#### justify-content & align-content

- 공간 배분 
  - flex-start (기본 값) : 아이템들을 axis 시작점으로 
  -  flex-end : 아이템들을 axis 끝 쪽으로 
  - center : 아이템들을 axis 중앙으로
  - space-between : 아이템 사이의 간격을 균일하게 분배 
  -  space-around : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에) 
  -  space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배



#### align - items

- 모든 아이템을 Cross axis를 기준으로 정렬

- **아래 그림은 `flex-direction: row` 위에서 아래다**

![images_bochodev_post_9494a49e-ffc0-496d-8571-06f82b5e6c49_align-items](/Users/yuyeong/Desktop/TIL/WEB/WEB_03/WEB_03.assets/images_bochodev_post_9494a49e-ffc0-496d-8571-06f82b5e6c49_align-items.svg)



#### align-self

- 개별 아이템을 Cross axis 기준으로 정렬
  - **해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용**

![images_bochodev_post_51ef1f70-8ab1-435e-927e-8c3b4db01e35_align-self](/Users/yuyeong/Desktop/TIL/WEB/WEB_03/WEB_03.assets/images_bochodev_post_51ef1f70-8ab1-435e-927e-8c3b4db01e35_align-self.svg)

#### align-items & align-self

- Cross axis를 중심으로 
  - Stretch( 기본 값) : 컨테이너를 가득 채움
  - Flex-start: 위
  - Flex-end : 아래
  - Center: 가운데
  - Baseline : 텍스트 baseline 에 기준선을 맞춤

- 기타 속성
  - flex-grow : 남은 영역을 아이템에 분배
  - order : 배치 순서
- 활용 레이아웃 - 카드 배치

```css
#layout_03 {
  display : flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-around;
  align-content: space-around;
}
```

![스크린샷 2022-08-31 오후 4.58.07(2)](/Users/yuyeong/Desktop/TIL/WEB/WEB_03/WEB_03.assets/스크린샷 2022-08-31 오후 4.58.07(2).png)