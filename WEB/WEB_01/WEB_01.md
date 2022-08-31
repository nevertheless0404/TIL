# WEB 

## 웹사이트의 구성 요소

- HTML : 구조
- CSS : 표현
- Javascript : 동작



## HTML

웹 사이트와 브라우저 

- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간식 달라서 문제가 생기는 경우가 많음(파편화)
- 해결책으로 **웹 표준**이 등장



웹 표준 

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 한다.(크로스 브라우징)



HTML 이란?

> Hyper Text Markup Language
>
> 웹 페이지를 작성(구조화) 하기 위한 언어

- Hyper Text 란?

  - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- Markup Language

  - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 

  

- HTML의 기본 구조 

````html
소# HTML, Markdown
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hello, HTML</title>
  </head>
<body>
  </body>
</html>
````

- html: 문서의 최상위(root)요소
- head: 문서 메타데이터 요소 
  - 문서 제목, 인코딩, 스타일, 외부 파일 로팅 등 
  - 일반적으로 브라우저에 나타나지 않는 내용 

- body: 문서 본문 요소
  - 실제 화면 구성과 관련된 내용 



#### head 예시

- `<title>` : 브라우저 상단 타이틀
- `<meta>` : 문서 레벨 메타데이터 요소
- `<link>` : 외부 리소스 연결 요소(CSS 파일, favicon 등)
- `<script>` : 스크립트 요소(JavaScript 파일/코드)
- `<style>` : CSS 직접 작성

```html
<head>
  <title>HTML 수업</title>
  <meta charest="UTF-8"
  <link href="style.css" rel="stylesheet">
  <script src="javascript.js"></script>
  <style>
    p {
      color: black;
    }
  </style>
</head>
```



#### 요소(element)

```html
<h1>contemts</h1>
```

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재(닫는 태그가 없음)
  - br, hr, img, input, link, mete

- 요소는 중첩(nested) 될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음



#### 속성(attribute)

````html
<a href(속성명)="https://google.comt"(속성값)></a>
````

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음 
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재한다.
- 태그와 상관 없이 사용가능한 속성들도 있음



- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
  - id : 문서 전체에서 유일한 고유 식별자 지정
  - class : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)
  - data-*: 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
  - style: inline 스타일
  - title: 요소에 대한 추가 정보 지정
  - tabindex: 요소의 탭 순서 

#### 렌더링

- 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정 [브라우저는 어떻게 동작하는가? (naver.com)](https://d2.naver.com/helloworld/59361)

#### DOM(Documnet Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성
  - HTML 문서 내의 각 요소에 접근/수정에 필요한 프로퍼티와 메서드 제공

#### 인라인 / 블록 요소

- HTML 요소는 크게 인라인/ 블록 요소로 나눔
- 인라인 요소는 *글자* 취급
- 블록 요소는 *한 줄* 모두 사용



#### 텍스트 요소

```html
<!-- a태그(anchor) 링크를 표현> -->
<a href="https://google.com">구글</a> 

<!-- b태그(bold) -->
<b>굵은 글씨</b>
<!-- 강조 -->
<strong>강한 글씨?</strong>

<!-- i태그(italic) -->
<i>italic</i>
<!-- 기울임 강조 -->
<em>강한 글씨?</em>

<!-- heading -->
<h1></h1>
<h2></h2>
<h6></h6>

<!-- 줄바꿈 -->
<br>

<!-- 띄워쓰기 -->
&nbsp;

<!-- img -->
<!-- alt는 대체 텍스트 -->
<img src="https://item.kakaocdn.net/do/2e134bd9f0af46e1e661fcf6240cfebfa88f7b2cbb72be0bdfff91ad65b168ab" alt="농담곰">

<!-- 문단 -->
<p>
  문단
</p>

<!-- 수평선 -->
<hr>

<!-- ol(ordered list), ul(unordered list) -->
<ol>
	<li>순서가 있음</li>
</ol>

<ul>
  <li>순서가 없음</li>
</ul>

<!-- 인용문 -->
<blockquote></blockquote>
```



## CSS

> Cascading Style Sheet
>
> 스타일을 지정하기 위한 언어, 위에서 부터 아래도 흐르면서 스타일을 입혀줌 



#### CSS 구문

```css
h1(선택자) {
  color : bule;(선언)
  font-size(속성):15px;(값)
}
```

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍을 선택한 요소의 속성, 속성에 부여할 값을 의미 
  - 속성(property) : 어떤 스타일 기능을 변경할지 결정
  - 값(value) : 어떻게 스타일 기능을 변경할지 결정 

**1. 인라인 (사용하지 않음, 비효율적)**

```css
<body>
  <h1 style ="color: blue; font-size: 100px;">Hello</h1>
</body>
```

**2. 내부참조**

```css
<head>
  <title>Document</title>
  <style>
    h1 {
      color: blue;
      font-size: 15px;
    }
  </style>
```

**3. 외부참조(파일을 따로 만듦)**

```css
mystyle.css
  h1 {
  color: blue;
  font-size: 15px;
  }
<head>
  <title>Document</title>
  <link rel="stylesheet" href="mystle.css">
</head>
```



#### CSS 기초 선택자 

- 요소 선택자

  - HTML 태그를 직접 선택

- 클래스(class) 선택자

  - 마침표(.)문자로 시작하여, 해당 클래스가 적용된 항목을 선택

- 아이디(id) 선택자

  - #문자로 시작하며, 해당 아이디가 적용된 항목을 선택

  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해되 동작하지만, 단일 id를 사용하는 것을 권장