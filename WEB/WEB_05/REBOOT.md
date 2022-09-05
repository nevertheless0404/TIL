# Bootstrap 문서 탐색

- **프로젝트 루트에 새 파일** 만드고, 적장한 방한 동작을 위해 < meta name="viewport">

````html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
````

- **Bootstrap의 CSS 및 JS를 포함합니다.** CSS에 대한 태그 `<link>`와 닫기 전에 JavaScript 번들에 대한 태그(드롭다운, 팝퍼 및 툴팁 위치 지정을 위한 Popper 포함)를 배치

````html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  </body>
</html>
````



## Layout - Breakpoints

### ✅Point

- **중단점은 반응형 디자인의 빌딩 블록**
- **미리어 쿼리를 사용하여 중단점으로 CSS를 설계**
- **모바일 우선, 반응형 디자인의 목표**



### 미디어 쿼리

| 중단점    | 클래스 중위 |
| --------- | ----------- |
| 엄청 작은 | 없음        |
| 작은      | sm          |
| 중간      | md          |
| 크기가 큰 | lg          |
| 특대      | xl          |
| 특대형    | xxl         |



#### 최소 너비

```css
// Source mixins

// No media query necessary for xs breakpoint as it's effectively `@media (min-width: 0) { ... }`
@include media-breakpoint-up(sm) { ... }
@include media-breakpoint-up(md) { ... }
@include media-breakpoint-up(lg) { ... }
@include media-breakpoint-up(xl) { ... }
@include media-breakpoint-up(xxl) { ... }

// Usage

// Example: Hide starting at `min-width: 0`, and then show at the `sm` breakpoint
.custom-class {
  display: none;
}
@include media-breakpoint-up(sm) {
  .custom-class {
    display: block;
  }
}
```



#### 최대 너비

````CSS
// No media query necessary for xs breakpoint as it's effectively `@media (max-width: 0) { ... }`
@include media-breakpoint-down(sm) { ... }
@include media-breakpoint-down(md) { ... }
@include media-breakpoint-down(lg) { ... }
@include media-breakpoint-down(xl) { ... }
@include media-breakpoint-down(xxl) { ... }

// Example: Style from medium breakpoint and down
@include media-breakpoint-down(md) {
  .custom-class {
    display: block;
  }
}
````



### 단일 중단점

````css
@include media-breakpoint-only(xs) { ... }
@include media-breakpoint-only(sm) { ... }
@include media-breakpoint-only(md) { ... }
@include media-breakpoint-only(lg) { ... }
@include media-breakpoint-only(xl) { ... }
@include media-breakpoint-only(xxl) { ... }

@media (min-width: 768px) and (max-width: 991.98px) { ... }
````



#### 인라인 텍스트 요소

````html
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><s>This line of text is meant to be treated as no longer accurate.</s></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
<p><u>This line of text will render as underlined.</u></p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p><strong>This line rendered as bold text.</strong></p>
<p><em>This line rendered as italicized text.</em></p>
````

- `<mark>`참조 또는 표기를 위해 표시되거나 강조 표시된 텍스트를 나타냅니다.
- `<small>`저작권 및 법률 텍스트와 같은 보조 설명 및 작은 글씨를 나타냅니다.
- `<s>`더 이상 관련이 없거나 더 이상 정확하지 않은 요소를 나타냅니다.
- `<u>`텍스트가 아닌 주석이 있음을 나타내는 방식으로 렌더링되어야 하는 인라인 텍스트의 범위를 나타냅니다.

텍스트의 스타일을 지정하려면 대신 다음 클래스를 사용해야 합니다.

- `.mark`와 같은 스타일을 적용합니다 `<mark>`.
- `.small`와 같은 스타일을 적용합니다 `<small>`.
- `.text-decoration-underline`와 같은 스타일을 적용합니다 `<u>`.
- `.text-decoration-line-through`와 같은 스타일을 적용합니다 `<s>`.

위에 표시되지 않았지만 HTML5에서 `<b>`자유롭게 사용하십시오. 추가적인 중요성을 전달하지 않고 단어나 구를 강조하기 위한 것이며 주로 음성, 기술 용어 등을 위한 것입니다.`<i><b><i>`



### 텍스트 유틸리티

- 약어 : 기본 밑줄이 있으며 호버 및 보조 기술 사용자에게 추가 컨텍스트를 제공 
- `.initialism`약간 더 작은 글꼴 크기에 대한 약어에 추가 합니다.

````html
<p><abbr title="attribute">attr</abbr></p>
<p><abbr title="HyperText Markup Language" class="initialism">HTML</abbr></p>
````



- 인용구 : 문서 내의 다른 소스에서 콘텐츠 블록을 인용 `<blockquote class="blockquote">`

````html
<blockquote class="blockquote">
  <p>A well-known quote, contained in a blockquote element.</p>
</blockquote>
````



- 조정

````html
<figure class="text-center">
  <blockquote class="blockquote">
    <p>A well-known quote, contained in a blockquote element.</p>
  </blockquote>
  <figcaption class="blockquote-footer">
    Someone famous in <cite title="Source Title">Source Title</cite>
  </figcaption>
</figure>
````



