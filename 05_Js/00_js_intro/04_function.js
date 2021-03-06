// 함수

// 선언식

// function add (num1, num2){
//   return num1 + num2
// }

// console.log(add(2,7))

// const sub =  function(num1, num2){
//   return num1 - num2
// }

// console.log(sub(7,2))

// // Js 도 함수의 하나의 값!!

// console.log(typeof sub)

// Arrow function (화살표 함수)
// why arrow function
// 항상 익명 함수
//1. function keyword 생략 가능
//2. 함수의 매개변수가 1개라면 () 생략 가능
//3. 함수 바디의 표현식이 하나라면 {} 와 return 생략 가능


// 함수 표현식
// const ssafy1 = function() {
//   return hello
// }
// console.log(ssafy1())

// 화살표 함수로 바꿔보기!
//1. function 키워드를 삭제할 수 있음!
// const ssafy1 = (name) => { return `Hello ${name}`}
// console.log(ssafy1('pppp2'))

// const ssafy2 = name => {return `Hello ${name}`}
// console.log(ssafy2('pppp2'))

// const ssafy3 = name => `Hello ${name}`
// console.log(ssafy3('pppp2'))

// let square = function(num){
//   return num ** 2
// }
// console.log(square(2))

// square = (num) => {return num**2 } //화살표
// console.log(square(2))

// square = num => {return num**2 } // 매개변수
// console.log(square(2))

// square = num => num**2 // return
// console.log(square(2))

// 인자가 없을때 -> (), _ 표현가능

// let noArgs = () => 'No Args'

// console.log(noArgs())

// noArgs = _ => 'No Args'

// console.log(noArgs())

// // 5 - 1 object를 리턴하려고 한다면?
// let returnObject = () => { return {key: 'value'}}
// console.log(returnObject())
// console.log(typeof returnObject())

// // 5-2 return을 적지 않고 object를 return 하고 싶다면 ()을 활용하세요
// returnObject = () => ({key: 'value'})
// console.log(returnObject())
// console.log(typeof returnObject())

// // 5- 3return문을 적지 않았을때
// returnobject = () => {key: 'value'}
// console.log(returnObject())
// console.log(typeof returnObject())

// 기본 인자
// 기본 인자를 줄 때는 인자 개수와 상관없이 괄호를 꼭 해야 한다.
// 괄호가 없으면 syntax error 발생
// const sayHello = (name="noName") => `hi ${name}`

// console.log(sayHello('ppp2'))
// console.log(sayHello())

// 익명함수 or 1회용 함수
// 즉시 실행 함수는 초기화에 많이 사용 된다.

// function (num) {return num ** 3}

// 1. 기명함수로 만등러 보자

// const cube = function (num) {return num ** 3}
// const squareRoot = num => num ** 0.5

// 2. 즉시실행함수 -> 주로, 초기화에 많이 사용
// console.log((function (num) { return num ** 3})(2))
// console.log((num => num ** 0.5)(4))


// 함수 hoisting

// ssafy()

// function ssafy(){
//   console.log('hoisting!')
// }

// ssafy2()

// let ssafy2 = function () {
//   console.log('hoisting!')
// }

// // Js 엔진이 코드를 해석하는 과정

// let ssafy2 // 변수 선언 let 은 var 와 다르게 초기화가 동시에 진행되지 않음!

// ssafy2() // 2함수 호출 -> ssafy2 가 초기화가 안됨! -> TDZ

// ssafy2 = function() {
//   console.log('hoisting')
// }

// ssafy3()

// var ssafy3 = function(){
//   console.log('hst')
// }

// // Js 엔진이 코드를 해석하는 과정

// var ssafy3 // 변수 선언 초기화 ok

// ssafy3() // 2함수 호출 -> ssafy3 = undefined

// ssafy3 = function() {
//   console.log('hoisting')
// }

