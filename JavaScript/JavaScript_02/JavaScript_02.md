# 자바스크랩트

## 변수와 식별자

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 **문자, 달러($), 밑줄(_)** 로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 수문자로 시작
- 예약어 사용 불가 (for, if, function) 등 

````javascript
let foo          // 선언
console.log(foo) // undefined

foo = 11          // 할당
console.log(foo)  // 11

let bar = 0        // 선언 + 할당
console.log(bar)   // 0
````



### let,const

````javascript
const(재할당 불가능)
// Immutable
const number = 10  // 1. 선언 및 초기값 할당
const number = 30  // 2. 재선언 불가능

=> Uncaught TypeError
   :Assignment to constant variable.
````

````javascript
let (재할당 가능)
// Mutable
let number = 10   // 1. 선언 및 초기값 할당
number = 10       // 2. 재할당

console.log(number) // 10 
````

- 재선언은 둘 다 (let, const) 불가능 

- 블록 스코프(block scope)
  - if, for, 함수 등의 중괄호 내부를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능 

````javascript
let x = 1
if (x == 1) {
  let x = 2
  console.log(x)  // 2
}

console.log(x)   // 1

// let (added in ES6)
let globalName = 'global name';
{
  let name = 'ellie';
  console.log(name);
  name = 'helle';
  console.log(name);
  console.log(gobalNAme);
}
console.log(name);
console.log(globalName)
````



### var

- Var로 선언한 변수는 재선언 및 재할당 모두 가능

- ES6 이전에 변수를 선언할 떄 사용되던 키워드

- 호이스팅 되는 특성으로 인해 예기치 못한 문제 발생 가능 

- 함수 스코프(function scope)

  - 함수의 중괄호 내부를 가리킴
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능 

  ```javascript
  function foo() {
      var x = 5;
      console.log(x); // 5
  };
  
  console.log(x)
  // ReferenceError: x is not defined
  ```

  

### 호이스팅

- 호이스팅(hoisting)
  - 변수를 선언 이전에 참조할 수 있는 현상
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
  - Ver, lat, const  모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대가 존대하지 않음
  - Ver hoisting => 어디에 선언했냐에 상관없이 젤 쉬에 선언 끌어올려줌
  - Ver 는 블록 스콥이 없음 



## 데이터 타입

### 원시 타입(Primitive type)

> 객체가 아닌 기본타입 : 변수에 해당 타입의 값이 담기며 다른 변수에 복사할 때 실제 값이 복사됨

- 숫자(number) : 따옴표 없이 표기한 숫자
- 문자열(string) : 작은 따옴표(')나 큰 따옴포(")로 묶어 나타냄
- 논리형(boolean) : 참(true)/거짓(false)란 두 값만 가지고 있는 유형
- undefined : 변수를 선언하고 값을 저장하지 않는 등의 자료형을 지정하지 않았을 때.
- null : 값이 유효하지 않을 때



### 참조 타입(Reference type)

> 객체 타입의 자료형 : 변수에 해당 객체의 참조 값이 담기며 다른 변수에 복사할 때 참조 값이 복사됨

- 배열(array) : 하나의 변수에 여러 값을 저장하는 유형
- 객체(object) : 함수의 속성이 함께 포함된 유형



### 숫자(Number) 타입

- 정수, 실수 구분없는 하나의 숫자 타입

- 부동소수점 형식을 따름 

  ````javascript
  const a = 13         // 양의 정수
  const b = -5         // 음의 정수
  const c = 3.14       // 실수
  const d = 2.998e8    // 거듭제곱
  const e = Infinity   // 양의 무한대
  const f = -Infinity  // 음의 무한대
  const g = NaN        // 산술 연산 불가



### 문자열(String) 타입

- 텍스트 데이터를 나타내는 타입
- 작은 따옴표(' '), 큰 따옴표(" ")로 묶은 자료
- 숫자도 따옴표로 묶으면 문자형이 됨
- 16bit 유니코드 문자의 집합

````javascript
const firstName = 'Brandon';
const lastName = 'Elch';
const fullName = '${firstName} ${lastName}'
````

#### 문자열 관련 주요 메서드

- `.includes`(value) => 문자열에 value가 존재하지 판별 후 참 또는 거짓 

- `.split`(value)  => value가 없을 경우, 기존 문자열을 배열에 담아 반환

  ​                           => value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환

  ​                           => value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환	

- `replace`(from, to)  => 문자열에 from 값이 존재할 경우, 1개만 to 값으로 교체
- `replaceAll`(from, to) => 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체
- `trim()`=> 문자열 **시작과 끝**의 모든 공백문자(스테이스, 탭, 엔터 등)를 제거
- `trimStart()`=> 문자열 **시작**의 공백문자를 제거
- `trimEnd()`=> 문자열 **끝**의 공백문자 를 제거 



### Boolean 타입

- 논리적 참 또는 거짓을 나타내는 타입
- true 또는 false로 표현
- 조건문 또는 반복문으로 유용하게 사용 

````javascript
let isAdmin = true
console.log(isAdmin)  // true

is Admin = false
console.log(isAmin)  // false
````



| 데이터 타입 | 참                              | 거짓          |
| ----------- | ------------------------------- | ------------- |
| 불리언      | True                            | False         |
| 문자열      | 비어 있지 않는 모든 문자열      | ""(빈 문자열) |
| 숫자        | 0이 아닌 모든 숫자(무한대 포함) | 0, NaN        |
| 객체        | 모든 객체                       | Null          |
| Underfined  | 해당 없음                       | Nudefined     |

### Null 

- 의도적으로 변수에 값이 없다는 것을 명시할 때 사용

- 의도적으로 값이 없음을 표현하고 싶을 때 대입 

- `typeOf`연산자로 null 값을 연산해오면 null이 아닌 object가 나온다.

  따라서 null 타입을 확일 할때는 typeOf 연산자 대신 일치 연산자(`===`)를 사용

### underfined

- 정의되지 않음, 값이 대입되지 않은 상태 
- 어떤 변수를 만들고 그 값을 정의해주지 않을 때 사용 



## 연산자

### 할당 연산자 

> 복합대입연산자, 변수에 값을 할당하는 연산자, 사직 연산자와 조합해서 사용할 수 있음

| 할당 연산자 | 의미                    |
| ----------- | ----------------------- |
| +=          | a = a + b               |
| -=          | a = a - b               |
| *=          | a = a * b               |
| /=          | a = a / b               |
| %=          | a = a % b               |
| ++          | a = a + b (값을 1 증가) |
| --          | a = a - b (값을 1 감소) |

### 비교 연산자

- 피연산자를 비교하고 결과값을 boolean으로 반환
- 문자열은 유니코드 값을 사용 
  - 알파벳 순서상 후순위가 더 크다 (a <  z => Ture)
  - 소문자가 대문자보다 더 크다 

### 동등 비교 연산자(`==`)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 암묵적인 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예상치 못한 결과가 발생할 수 있으므로 특별한 경우 제외하고 

### 일치 비교 연산자(`===`)

- 두 연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 엄격한 비교(두 비교 대상의 타입과 값 모두 같은지 비교)가 이뤄지며 암묵적 타입 변환이 발생하지 않음

### 논리 연산자

> 연산자는 왼쪽부터 오른쪽으로 평가를 진행 
>
> 중간에 평가 결과가 나오면 오른쪽 끝까지 가지 않고 평가 결과를 반환해 버림 
>
> 이를 '단축 평가(short circuit evaluation)'라고 하며, 피연산자의 타입을 변화하지 않고 그대로 반환 

- And/ or / not
  - and => &&
  - or => ||
  - not => !

### 삼항 연산자

- 세 개의 피연산자를 사용하여 조건에 따라 겂을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 (:) 뒤의 값을 사용
- 삼항 연산자의 결과 값이기 떄문에 변수에 할당 가능 

````javascript
console.log(true ? 1 : 2);  // 1
console.log(false ? 1 : 2); // 2

const result = Math.PI > 4 ? 'Yes' : 'No';
console.log(result); // No
````



## 조건문

### if 문

- 괄호 안의 조건이 true이면 {} 사이의 명령을 처리하고, false이면 {} 안의 명령 무시 

- If ... else 문
  - 조건은 ()에 작성
  - 실행할 코드는 {} 안에
  - 블록 스코프 생성

```javascript
const a = 10;
if (a === 5) {
  console.log('5입니다!');
} else if (a === 10) {
  console.log('10입니다!');
} else {
  console.log('5도 아니고 10도 아닙니다.');
}

// 결과!
// "10입니다!"
```

### switch / case

- 표현식의 결과값을 이용

- 표현식의 결과값과 case문의 오른쪽 값을 비교 

- break 및 default 문은 [선택적]으로 사용 가능

- break문을 만나거나 default 문을 실행할 떄까지 다음 조건문 실행 

  ````javascript
  switch (조건 값) {
      case 값1:
          조건 값이 값1일 때 실행하고자 하는 실행문;
          break;
      case 값2:
          조건 값이 값2일 때 실행하고자 하는 실행문;
          break;
      default:
          조건 값이 어떠한 case 절에도 해당하지 않을 때 실행하고자 하는 실행문;
          break;
  ````

  ````HTML
  <!DOCTYPE html>
  <html lang="ko">
  <head>
  	<meta charset="UTF-8">
  	<title>JavaScript Conditional Statement</title>
  </head>
  <body>
  	<h1>switch 문</h1>
  	<script>
  		var x = 10;
  
  		switch (typeof x) {
  		case "number":
  			document.write("변수 x의 타입은 숫자입니다.");
  			break;
  		case "string":
  			document.write("변수 x의 타입은 문자열입니다.");
  			break;
  		case "object":
  			document.write("변수 x의 타입은 객체입니다.");
  			break;
  		default:
  			document.write("변수 x의 타입을 잘 모르겠네요...");
  			break;
  		}
  	</script>
  </body>
  </html>
  
  <!-- 결과 -->
  변수 x의 타입은 숫자입니다.



## 반복문

### While

- 조건문이 True인 동안 반복 시행
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성
- While 문을 작성할 때는 표현식의 결과가 어느 순간에는 거짓을 갖도록 표현식을 변경하는 실행문을 포함 

````javascript
var i = 1;
while (i < 10) { // 변수 i가 10보다 작을 때만 while 문을 반복함.
    document.write(i + "<br>");
    i++; // 반복할 때마다 변수 i를 1씩 증가시켜 변수 i가 10보다 커지면 반복문을 종료함.
}
````

### for 

- 세미콜론(;)으로 구분되는 세 부분을 구성
- initialization
  - 최초 반복문 진입 시 1회만 실행되는 부분  

- condition 
  - 매 반복 시행 전 평가되는 부분

- expression 
  - 매 반복 시행 이후 평가되는 부분 

```javascript
for (initialization; condition; expression){
  // do something
}

// for문을 사용하면 더욱 더 간결하게 표현할 수 있음 
// 1. 반복문 진입 및 변수 i 선언
// 2. 조건문 평가 후 코드 블럭 실행
// 3. 코드 블록 실행 이후 i 값 증가 

for (var i = 1; i < 10; i++) {
    document.write(i + "<br>");
}
```

### for ... in 

- 일반적인 for 과는 전혀 다른 형태의 반복문
- 객체(object)의 속성(key)들을 순회할 때 사용 
- 배열도 순회 가능하지만 권장하지 않음 
- 실행할 코드는 중괄호 안에 작성 
-  블록 스코프 생성

```javascript
// object(객체) => key-value로 이루어진 자료구조
const capitals = {
korea: 'seoul',
france: 'paris',
USA: 'washington D.C.'
}
for (let capital in capitas) {
  console.log(capital) // korea, france, USA
}
```

### for .. of 

- 반복할 수 있는 객체를 순회할 수 있도록 해주는 반복문
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성 

````javascript
var arr = [3, 4, 5];
for (var i = 0; i < arr.length; i++) { // 배열 arr의 모든 요소의 인덱스(index)를 출력함.
    document.write(arr[i] + " ");
}
for (var value of arr) { // 위와 같은 동작을 하는 for / of 문
    document.write(value + " ");
}

// 정답! 
345
345
````



## 함수 

### 함수 표현식

- 함수의 이름을 생략하고 익명 함수로 정의 가능
  - 익명 함수: 이름이 없는 함수 
  - 익명 함수는 함수 표션식에서만 가능

- 기본 인자 

  - 인자 작성 시 `=` 문자 뒤 기본 인자 선언 가능

    ```javascript
    const greeting = function (name = 'Anonymous'){
      return 'Hi ${name}'
    }
    greeting()  // Hi Anonymous
    ```

- 매개변수와 인자의 개수 불일치 허용 

````javascript
// 인자의 개수가 많을 경우 

const noArgs = function () {
  return 0 
}
noArgs(1, 2, 3) // 0
const twoArgs = funcion (arg1, arg2) {
  return [arg1, arg2]
}
twoArge(1, 2, 3) // [1, 2]

// 인자의 개수가 적을 경우 
const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3]
}

threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(1, 2) // [1, 2, undefined]
````

- Rest Parameter

  - Rest parameter(...)를 사용하면 함수가 정해지지 않음 수의 매개변수를 배열로 받음
  - 매개변수에 인자가 넘어오지 않을 경우에는 빈 배열로 처리

  ````javascript
  const restOpr = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, restArgs]
  }
  restArgs(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
  restArgs(1, 2) // [1, 2, []]
  ````

- Spread Operator

  - spread operator(…)를 사용하면 배열 인자를 전개하여 전달 가능

    ```javascript
    const spreadOpr = function (arg1, arg2, arg3) {
        return arg1 + arg2 + arg3;
    };
    
    const numbers = [1, 2, 3];
    spreadOpr(...numbers) //6
    ```

- 선언식 vs 표현식

  - 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

    ```javascript
    // 함수 표현식
    const add = function (ages) { }
    
    // 함수 선언식
    function sub(ages) { }
    
    console.log(typeof add) // function 
    console.log(typeof sub) // function 

  -  호이스팅(hoisting)) 

    - **선언식**

      => 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생

      => 함수 호출 이후에 선언 해도 동작 

    - **표현식**

      => 함수 정의 전에 호출 시 에러 발생

      => 변수로 평가되어 변수의 scope 규칙을 따름



## Arrow Function 

### 화살표 함수 

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 함수의 매개변수가 단 하나 뿐이라면, () 생략 가능 
- 함수 몸통이 표현식 하나라면 {}과 return 도 생략 가능

```javascript
const arrow1 = function (name) {
return `hello, ${name}`
}
// 1. function 키워드 삭제
const arrow2 = (name) => { return `hello, ${name}` }
// 2. 매개변수가 1개일 경우에만 ( ) 생략 가능
const arrow3 = name => { return `hello, ${name}` }
// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 { } & return 삭제
가능
const arrow4 = name => `hello, ${name}`
```



## 배열 

> 키와 속성들을 담고 있는 참조 타입의 객체(object)

> 순서를 보장하는 특징이 있음

> 주로 대괄호를 이용하여, 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능

> 배열의 길이는 `length` 형태로 접근 가능 

- `reverse()` => 원본 배열의 요소들의 순서를 반대로 정렬
- `push()` => 배열의 가장 뒤에 요소 추가
- `pop()` => 배열의 마지막 요소 제거 
- `unshift()` => 배열의 가장 앞에 요소 추가
- `shift()` => 배열의 첫번째 요소 제거 

- `includes(value)` => 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환 

- `indexOf(value)` => 배열에 특정 값이 존재하는지 확인 후 가장 첫 번쨰로 찾은 요소의 인덱스 반환

  ​	                          => 해당 값이 없을 경우 -1 반환

- `join([separator])` => 배열의 모든 요소를 연결하여 반환

​                                           =>  `separator(구분자)`는 선택적으로 지정 가능, 생략 시 쉼표를 기본 값으로 사용

- Spread operator 

  - Spread operator(...) 를 사용 하면 배열 내부에서 배열 전개 가능 

    ```javascript
    onst array = [1, 2, 3]
    const newArray = [0, ...array, 4]
    console.log(newArray) // [0, 1, 2, 3, 4]
    
    ```

- `.forEach(callback(element[,index[,array]]))`

  - 배열의 각 요소에 대한 콜백 함수를 한 번씩 실행

  - 콜백 함수는 3가지 매개변수로 구성

      • element: 배열의 요소 

      • index: 배열 요소의 인덱스

      • array: 배열 자체 

    - 반환 값(return)이 없는 메서드

```javascript
array.forEach((element, index, array)) => {
  // do something
}

const fruits = ['딸기', '수박', '사과', '체리']
fruits.forEach((fruit, index) => {
console.log(fruit, index)
// 딸기 0
// 수박 1
// 사과 2
// 체리 3
})
```

- `.map(callback(element[,index[,array]]))`

  - 배열의 각 요소에 대한 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

  ```javascript
  array.map((element, index, array) => {
      //do sth
  })
  ```

  ```javascript
  const numbers = [1, 2, 3, 4, 5]
  
  const doubleNums = numbers.map((num) => {
      return num * 2
  })
  
  console.log(doubleNums) //[2, 4, 6, 8, 10]
  ```

- `.filter(callback(element[, index[, array]]))`
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
  - 기존 배열의 요소들을 필터링할 때 유용

```javascript
array.filter((element, index, array) =>{
    // do sth
})
```

```javascript
const numbers = [1, 2, 3, 4, 5]
const oddNums = numbers.filter((num, index) => {
    return num % 2
})
console.log(oddNums) // 1, 3, 5
```

- `.reduce(callback(acc, element, [index[, array]])[, initialValue])`
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
  - reduce 메서드의 주요 매개변수
    - acc
    - 이전 callback 함수의 반환 값이 누적되는 변수
    - initialValue(optional)
      - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
  - 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

```javascript
array.reduce((acc, element, index, array) => {
    //do sth
}, initialValue)
```

```javascript
const numbers = [1, 2, 3]
const result = numbers.reduce((acc, num) => {
    return acc + num
}, 0)
console.log(result) // 6
```

- `.find(callback(element[, index[, array]]))`
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
  - 찾는 값이 배열에 없으면 undefined 반환

```javascript
array.find((element, index, array) {
     // do sth
})
```

```javascript
const avengers = [
    { name: 'Tony Stark', age: 45}
    { name: 'Steve Rogers', age: 32}
    { name: 'Thor', age: 40}
]
const result = avengers.find((avenger) => {
    return avenger.name === 'Tony Stark'
})
console.log(result) // { name: "Tony Stark", age: 45 }
```

- `.some(callback(element[, index[, array]]))`
  - 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
  - 모든 요소가 통과하지 못하면 거짓 반환
  - 빈 배열은 항상 거짓 반환

```javascript
array.some((element, index, array) => {
    // do sth
})
```

```javascript
const numbers = [1, 3, 5, 7, 9]

const hasEvenNumber = numbers.some((num) => {
    return num % 2 === 0
})
console.log(hasEvenNumber) // false

const hasOddNumber = numbers.some((num) => {
    return num % 2
})
console.log(hasOdddNumber) // true
```

- `.every(callback(element[, index[, array]]))`
  - 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환
  - 하나의 요소라도 통과하지 못하면 거짓 반환
  - 빈 배열은 항상 참 반환

```javascript
array.every((element, index, array) => {
    // do sth
})
```

```javascript
const numbers = [2, 4, 6, 8, 10]

const isEveryNumberEven = numbers.every((num) => {
    return num % 2 === 0
})
console.log(isEveryNumberEven) // false

const isEveryNumberOdd = numbers.every((num) => {
    return num % 2
})
console.log(isEveryNumberOdd) // false
```



## 객체

- 여러 자료를 중괄호({ })로 묶은 것
- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입(함수포함) 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```javascript
const me = {
    name: 'jack',
    phoneNumber: '01012345678', 'samsung': {
    	buds: 'galaxy buds pro',
    	galaxy: 'galaxy S20'
	}
}

console.log(me,name) // jack
console.log(me,phoneNumber)
console.log(me['samsung']) // {buds: 'galaxy buds pro', galaxy: 'galaxy S20'}
console.log(me['samsung'].buds) // galaxy buds pro
```

- 메서드는 객체의 속성이 참조하는 함수
- 객체.메서드명() 으로 호출 가능
- 메서드 내부에서는 this 키워드가 객체를 의미함

```javascript
const me = {
    firstName: 'John',
    lastName: 'Doe',
    getFullName: function () {
        return this.firstName + this.lastName
    }
}
```

