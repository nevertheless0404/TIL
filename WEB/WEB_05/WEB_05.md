# WEB

## HTML

### HTML 문서 구조화

- Table의 각 영역을 명시하기 위해 `<thead>` `<tbody>` `<tfoot>`요소를 활용

- table 태그 기본 구성
  - thead
    - tr > th
  - tbody
    - tr > td
  - tfoot
    - tr > td
  -  caption

```html
<body>
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Major</th>
      </tr>
    </thead>
    <tbody>
      <tr></tr>
      <tr>1</tr>
      <td>홍길동</td>
      <td>Computer Science</td>
      </tr>
  		<tr>
        <td>2</td>
        <td>김철수</td>
        <td>Business</td>
  		</tr>
    </tbody>
		<tfoot>
      <tr>
        <td>총계</td>
        <td colspan="2">2명</td>
      </tr>
		</tfoot>
		<caption>1반 학생 명단</caption>
  </table>
</body>
```



### Form

- < form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
- < form> 기본 속성
  - Action: form을 처리할 서버의 URL(데이터를 보낼 곳)
    - method: form을 제출할 때 사용하는 HTTP 메서드 (GET 혹은 POST)
  - Enctype: method가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded: 기본값
    - Multipart/form-data: 파일 전송시(input type이 file인 경우)

````html
<form action="/serch" method="GET">

</form>
````



#### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음

  - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음

  - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있게 함

  - `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴

    ```html
    <label for="agreement">개인정보 수집에 동의합니다.</label>
    <input type="checkbox" name"agreement" id="agreement">
    ```



#### input 유형 - 일반

- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
  - text : 일반 텍스트 입력
  - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  - email : 이메일 형식이 아닌 경우 form 제출 불가
  - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file : accept 속성을 활용하여 파일 타입 지정 기능



#### input 유형 - 항목 중 선택

- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함

- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 **value**를 지정해야 함

  - checkbox : 다중 선택

  - radio : 단일 선택

    ```html
    <label for="username">username</label>
    username : <input type="email" name="username" id="username" value="fx887722@naver.com">
    
    라디오 버튼을 사용할 때는 input name은 똑같이 지정해야 라디오 버튼의 용도에 맞게 동작이 가능 
    <label for="mincho">민초</label>
    <input type="radio" name="is_mincho" id="">
    <label for="notmincho">반민초</label>
    <input type="radio" name="is_mincho" id="">
    ```



#### input 유형 - 기타

- 다양한 종류의 input을 위한 picker를 제공
  - color : color picker
  - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden : 사용자에게 보이지 않는 input



## Bootstrap

#### Content Delivery(Distribution) Network

**컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템**

개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)

외부 서버를 활용함으로써 본인 서버의 부하가 적어짐



#### spacing(Margin and padding)

```html
 m				t			 -3
{property}{sides}-{size}
<div class="mt-3 ms-5">bootstrap-spacing</div>
```

| m    | margin  |
| ---- | ------- |
| p    | padding |

| t    | top         |
| ---- | ----------- |
| b    | bottom      |
| s    | left        |
| e    | right       |
| x    | left, right |
| y    | top, bottom |

| 0    | 0rem    | 0px  |
| ---- | ------- | ---- |
| 1    | 0.25rem | 4px  |
| 2    | 0.5rem  | 8px  |
| 3    | 1rem    | 16px |
| 4    | 1.5rem  | 24px |
| 5    | 3rem    | 48px |

.mx-auto

-> 블록 요소를 수평 중앙 정렬, 가로 가운데 정렬할때!

- 16* 0.25 = 4px
  - 브라우저`<html>`의

```html
<mx-auto>
  블록 요소, 수평 중앙 정렬, 가로 가운데 정렬

.mx-auto {
  margin-right: auto !important;
  margin-left: auto !important;
  }
```



#### Color

부트스트랩에 설정된 기본 컬러들

```css
:root {
	--primary: #007bff;
	--secondary: #6c757d;
	--success: #28a745;
  --info: #17a2b8;
  --warnung: #ffc107;
  --danger: #dc3545;
  --light: #f8f9fa;
  --dark: #343a40;
}
```



#### Text

```html
<p class="text-start">margin-top 3</p>
<p class="text-center">margin 4</p>
<p class="text-end">mx-auto, 가운데 정렬</p>
<a href="#" class="text-decoration-none">Non-underlined link</a>
<p class="fw-bold">Bold</p>
<p class="fw-normal">Normal weight text</p>
<p class="fw-light">Light weight text</p>
<p class="fw-italic">Italic text</p>
```







