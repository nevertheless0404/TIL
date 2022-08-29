# HTML (HyperText Markup Language)

> 웹을 이루는 가장 기초적인 구성요소 

> 웹 콘텐츠의 의미와 구조를 정의

 ### HyperText ?

- 웹 페이지를 다른 페이지로 연결하는 링크 

### Markup ?

- 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위함

### HTML 요소

- **태그**를 사용 하며 문서의 다른 텍스트와 구분 
- 태그안의 요소 이름은 대소문자를 구분하지 않음

 ##### - **주요 부분**

1. 여는 태그 `<p>` : 요소의 이름으로 구성, 요소가 시작되는 곳
2. 닫는 태크 `</p>` : 여는 태그와 같지만, 요소의 이름 앞에 전방향 슬래시 포함. 요소의 끝
3. 컨텐츠 : 요소의 내용
4. 요소 : 여는 태그와 닫는 태그, 그리고 컨텐츠로 이루어짐  

##### - 요소는 속성을 가질 수 있음 

- 속성이 가져야 하는 것!
  - 요소 이름 ( 요소가 하나 이상 속성을 이미 가지고 있다면 이전 속성) 과 속성 사이에 공백
  - 속성 이름 뒤에는 `등호(=)`
  - 속성 값의 앞 뒤에 열고 닫는 인용부호 `"",''`



#### - 요소 중첩

- 요소를 다른 요소 안에 넣는 것!

##### < strong > : 중요도 요소

````html
<p>... the most important rule, the rule you can never forget, no matter how much he cries, no matter how much he begs: <strong>never feed him after midnight</strong>.</p>
````

- < strong > 매우 심각하거나 긴급한 내용을 포함 `매우 중요함` 
- `<b>` vs `strong` : `<strong>`요소는 더 중요한 내용을 위한 것이고 요소 `<b>`는 더 중요한 것을 나타내지 않고 텍스트에 주의를 끌기 위해 사용됩니다. 
- `<em>` vs `<strong>` : `<em>`구어 강조처럼 문장의 의미를 바꾸는 데 사용되며("I *love* 당근" vs. "I love *당근* "), `<strong>`문장의 일부에 중요성을 추가하는 데 사용됩니다(예: " **경고!** 이것은 **매우 위험합니다.** ") 



#### - 이미지

##### **< img >** : 이미지 삽입

````html
<img class="fit-pictrue"
     src="/media/cc0-images/grapefruit-slice-332-332.jpg"
     alt="Grapefrtir slice atop a plie of other slices"
````

- `src` : **필수**, 포함하고자 하는 이미지의 경로를 지정

- `alt` : 값을 읽어 사용자에게 이미지를 설명하므로, 접근성 차원에서 **매우 유용** 

- 이미지를 가져올 수 없을 때
  - `src` 속성이 비었거나 `null`
  - `src`의 URL이 현재 사용자가 보는 페이지의 URL이 같음
  - 지정한 이미지가 손상돼 불러올 수 없음
  - 이미지의 메타데이터가 손상되어 원본 크기를 알아낼 수 없음, `<img>`요소의 속성에도 크기를 지정하지 않음
  - 사용자 에이전트가 지원하지 않는 이미지 형식



#### - HTML 문서 해부 

````html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
````

- `<html></html>` —`<html>` 이 요소는 페이지 전체의 컨텐츠를 감싸며, 루트(root) 요소
- `<head></head>` — `head` 이 요소는 HTML 페이지에 포함되어 있는 모든 것들(여러분의 페이지를 조회하는 사람들에게 보여주지 않을 컨텐츠)의 컨테이너 역할을 합니다.
- `<body></body>` —`body` 이것은 페이지에 방문한 모든 웹 사용자들에게 보여주길 원하는 *모든* 컨텐트를 담고 있으며, 그것이 텍스트일 수도, 이미지, 비디오, 게임, 플레이할 수 있는 오디오 트랙이나 다른 무엇이든 될 수 있습니다.

- `< meta charset="utf-8" >` — 이 요소는 문서가 사용해야 할 문자 집합을 utf-8으로 설정합니다(utf-8 문자 집합에는 인간의 방대한 주류 기록언어에 있는 대부분의 문자가 포함되어 있습니다) 

- `<title></title>` — `<title>` 이 요소는 페이지의 제목을 설정하는 것으로 페이지가 로드되는 브라우저의 탭에 이 제목이 표시됩니다.



#### - 문자 나타내기

- `< h1 > - < h6 >` : HTML 구획 제목 요소

````html
<h1>Heading level 1</h1>
<h2>Heading level 2</h2>
<h3>Heading level 3</h3>
<h4>Heading level 4</h4>
<h5>Heading level 5</h5>
<h6>Heading level 6</h6>
````

# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6



#### - 문단

- `<p>` : 하나의 문단을 나타냅니다. 시각적인 매체에서, 문단은 보통 인접 블록과의 여백과 첫 줄의 들여쓰기로 구분하지만, HTML에서 문단은 이미지나 입력 폼 등 서로 관련있는 콘텐츠 무엇이나 될 수 있습니다.

````html
<p>첫 번째 문단입니다.
  첫 번째 문단입니다.
  첫 번째 문단입니다.
  첫 번째 문단입니다.</p>
<p>두 번째 문단입니다.
  두 번째 문단입니다.
  두 번째 문단입니다.
  두 번째 문단입니다.</p>
````

첫 번째 문단입니다. 첫 번째 문단입니다. 첫 번째 문단입니다. 첫 번째 문단입니다.

두 번째 문단입니다. 두 번째 문단입니다. 두 번째 문단입니다. 두 번째 문단입니다.



#### - 목록

1. 순서 없는 목록 : 쇼핑 목록과 같이 항목의 순서에 관계가 없는 목록 
   - `<ul>`

````html
<ul>
  <li>first item</li>
  <li>second item</li>
  <li>third item</li>
</ul>
````

- first item
- second item
- third item

````html
<ul>
  <li>first item</li>
  <li>second item
  <!-- Look, the closing </li> tag is not placed here! -->
    <ul>
      <li>second item first subitem</li>
      <li>second item second subitem
      <!-- Same for the second nested unordered list! -->
        <ul>
          <li>second item second subitem first sub-subitem</li>
          <li>second item second subitem second sub-subitem</li>
          <li>second item second subitem third sub-subitem</li>
        </ul>
      </li> <!-- Closing </li> tag for the li that
                  contains the third unordered list -->
      <li>second item third subitem</li>
    </ul>
  <!-- Here is the closing </li> tag -->
  </li>
  <li>third item</li>
</ul>
````

- first item
- second item
  - second item first subitem
  - second item second subitem
    - second item second subitem first sub-subitem
    - second item second subitem second sub-subitem
    - second item second subitem third sub-subitem
  - second item third subitem
- third item

```html
<ul>
  <li>first item</li>
  <li>second item
  <!-- Look, the closing </li> tag is not placed here! -->
    <ol>
      <li>second item first subitem</li>
      <li>second item second subitem</li>
      <li>second item third subitem</li>
    </ol>
  <!-- Here is the closing </li> tag -->
  </li>
  <li>third item</li>
</ul>
```

- first item
- second item
  1. second item first subitem
  2. second item second subitem
  3. second item third subitem
- third item



2. 정렬된 목록, 보통 숫자 목록 

   - `<ol>`

     - reversed : 목록의 순서 역전 여부. 즉, 내부에 지정한 항목이 역순으로 배열된 것인지 나타냅니다.

     - start :  항목을 셀 때 시작할 수. `type`이 로마 숫자나 영어 문자인 경우에도 아라비아 숫자로 나타낸 정수(1, 2, 3...)만 가능합니다. 그러므로 영어 문자 "d"나 로마 숫자 "iv"부터 세려고 한다면 `start="4"`를 사용하세요.

     - type : 항목을 셀 때 사용하는 카운터 

       `'a'`는 소문자 알파벳

       `'A'`는 대문자 알파벳

       `'i'`는 소문자 로마 숫자

       `'I'`는 대문자 로마 숫자

       `'1'` 는 숫자(기본값)을 나타냅니다.



#### - 연결

- `<a>` : **요소**(앵커 요소)는 `href` 특성을 통해 다른 페이지나 같은 페이지의 어느 위치, 파일, 이메일 주소와 그 외 다른 URL로 연결할 수 있는 하이퍼링크를 만듭니다. `<a>` 안의 콘텐츠는 링크 목적지의 설명을 **나타내야 합니다**

```html
<p>You can reach Michael at:</p>

<ul>
  <li><a href="https://example.com">Website</a></li>
  <li><a href="mailto:m.bluth@example.com">Email</a></li>
  <li><a href="tel:+123456789">Phone</a></li>
</ul>

```

- `donwload`
  - 링크로 이동하는 대신 사용자에게 URL을 저장할지 물어본다.

- `href`
  - 하이퍼링크가 가리키는 URL. 링크는 HTTP 기반 URL 일 필요가 없고, 브라우저가 지원하는 모든 URL 스킴을 사용 