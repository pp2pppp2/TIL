// 애열로 이루어진 숫자를 다 더하는 함수
// const numbersAddEach = numbers =>{
//   let sum = 0
//   for ( const number of numbers){
//     sum += number
//   }
//   return sum
// }
// // 배열로 이로어진 숫자를 다 빼는 함수
// const numbersSubEach = numbers =>{
//   let sub = 0
//   for ( const number of numbers){
//     sub -= number
//   }
//   return sub
// }

// // 배욜로 이류오잔 슛저둘울 다 곱한 함수
// const numbersMulEach = numbers =>{
//   let mul = 1
//   for ( const number of numbers){
//     mul *= number
//   }
//   return mul
// }

// console.log(numbersAddEach([1,2,3,4,5]))
// console.log(numbersSubEach([1,2,3,4,5]))
// console.log(numbersMulEach([1,2,3,4,5]))

// 숫자로 이루어진 배열의 요소를 [??????] 한다.

const NUMBERSS =[1,2,3,4,5]

const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers){
    acc = callback(number, acc)
  }
  return acc
}

// //더한다

// const addEach = (number, acc=0) => {
//   return acc + number
// }

// console.log(numbersEach(NUMBERSS, addEach))

// // 밴다
// const subEach = (number, acc=0) => {
//   return acc - number
// }

// console.log(numbersEach(NUMBERSS, subEach))

// // 곱한다
// const mulEach = (number, acc=1) => {
//   return acc * number
// }

// console.log(numbersEach(NUMBERSS, mulEach))

// 리팩토링

// console.log(numbersEach(NUMBERSS, (number, acc = 0) => acc + number ))
// console.log(numbersEach(NUMBERSS, (number, acc = 0) => acc - number ))
// console.log(numbersEach(NUMBERSS, (number, acc = 1) => acc * number ))