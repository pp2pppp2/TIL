// 변수와 식별자
// var로 선언된 변수의 범위는 현재 실행 문맥 -> 함수 or 함수 외부 전역
/*
var x = 1

if (x === 1){
  var x = 2
  console.log(x)
}
console.log(x)
*/

// let -> 값을 재할당 할 수 있는 변수 선언 키워드 (선언은 한번만, 할당은 여러번 가능)
// block scope

/*
let x = 1
console.log(x) // 1
x = 3

console.log(x) // 3
*/

/*
let x = 1
if (x === 1) {
  let x = 2
  console.log(x)
}
console.log(x)
*/

// const -> 상수, 값이 변하지 않는 상수를 선언하는 기워드
// block scope
// 담긴 값이 변하지 않는 다는 의미가 아니라 단지 상수의 값은 재할당을 통해 바뀔 수 없고
// 재선언 될 수 없다.

// const MY_FAV = 1
// if (MY_FAV === 1) {
//   const MY_FAV = 2
//   console.log(MY_FAV)
// }
// console.log(MY_FAV)

// let  vs  var

// var
/*
function varTest(){
  var x = 1
  if (true){
    var x = 2
    console.log(x)
  }
  console.log(x)
}

varTest()

function letTest(){
  let x = 1
  if (true){
    let x = 2
    console.log(x)
  }
  console.log(x)
}

letTest()
*/

// var a = 1
// var b = 2

// if (a === 1){
//   var a = 11
//   let b = 22
//   console.log(a)
//   console.log(b)
// }
// console.log(a)
// console.log(b)

// var : 할당 및 선언 자유, 함수 스코프(현재 실행 문맥)
// let: 할당 자유, 선언은 한번만, 블록 스코프
// const: 할당 선언 한번만 블록 스코프

// // 변수와 식별자 
// // 객체, 변수, 함수 -> 카멜 케이스 (lowerCamelCase)

// //숫자, 문자, 불리언

// let dog
// let variableName

// // 객체(Object)

// const memberInfo = {
//   id : 1,
//   password : 12345,
//   gender: 'male',
// }

// // 배열 - 배열은 보통 복수형으로 표현

// const dogs = []

// // 정규표현식 - 'r'로 시작

// const rDese = /ab+c/

// //함수
// function getPropertyName(){

// }

// // 이벤트 핸들러 - 이벤트 핸들러는 'on' 으로 시작
// const onClick = () => {}
// const onKeyDown = () => {}

// // boolean을 반환하는 함수 -> return 값이 불리언인 함수는 'is'로 시작
// let isAvailable = false

// // 파스칼 케이스(UpperCamelCase) - 클래스 / 생성자 

// class User{
//   constructor(options){
//     this.name = options.name
//   }
// }

// const good = new User({
//   name:'yup',
// })

// console.log(good)
// console.log(typeof good)

// 대문자 스네이크 케이스 - 상수
// export const API_KEY = 'SOMEKEY'

// export const MAPPING ={
//   key: 'value'
// }

