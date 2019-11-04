// object , array

// Array

const numbers = [1, 2, 3, 4]

console.log(numbers[0])
console.log(numbers[-1])
console.log(numbers.length)


// // 원본을 파괴시키는 친구들

// console.log(numbers.reverse())
// console.log(numbers.push(1))
// console.log(numbers.pop())

// // 배열 끝에 push // 길이를 return 합니다.

// // unshift 배열의 가장 첫번째 요소로 push 후 길이를 return
// console.log(numbers.unshift(6))
// console.log(numbers.shift())
// console.log(numbers)


// // 복사본 or 다른값 return
// console.log(numbers.includes(1)) // 있니?
// console.log(numbers.includes(0))

// console.log(numbers.push('a'))
// console.log(numbers.push('a'))
// console.log(numbers)

// console.log(numbers.indexOf('a')) // 중복시 첫 인덱스 없으면 -1 return
// console.log(numbers.join('-'))


// // 배열의 원본은 변하지 안음

// const me = {
//   name : 'ssafy', // 1개의 단어
//   'phone number': '010123456789', // 여러개의 단어로 이뤄지면 스트링처리
//   appleProducts:{
//     ipad: '2018pr',
//     iphone: '6s+',
//     macbook: '2018pro',
//   }
// }

// console.log(me.name)
// console.log(me['name'])
// console.log(me['phone number']) ///// 무적권 [] 입니다.

// console.log(typeof me.appleProducts)
// console.log(me.appleProducts.ipad)

// Object Literal (추가된 오브젝트 표현법:ES6+)

// const books = ['사서삼경', '천자문']

// const movies = {
//   'Horrer': ['곤지암', '겟아웃'],
//   'SF': ['인셉션', '마션', '인터스텔라', '그레비티'],
// }

// const magazines = null

// const bookshop ={
//   books: books,
//   movies: movies,
//   magazines: magazines,
// }
// // 5
// console.log(bookshop)
// console.log(bookshop.books[1])


// es6
// object 의 key value가 똑같다면 마치 배열처럼 사용가능


// const books = ['사서삼경', '천자문']

// const movies = {
//   'Horrer': ['곤지암', '겟아웃'],
//   'SF': ['인셉션', '마션', '인터스텔라', '그레비티'],
// }

// const magazines = null

// const bookshop ={
//   books,
//   movies,
//   magazines,
// }

// console.log(books[1])


// JSON vs Object

// JSON 은 Object의 형태와 유사한 문자열!
// 실제로 object로 사용하기 위해서는 변환이 필요하다

// ob -> str

// const JsonData = JSON.stringify({
//   coffee:'Americano',
//   iceCream:'Cookie and cream',
// })

// console.log(JsonData)
// console.log(typeof JsonData)

// // str -> ob

// const perseData = JSON.parse(JsonData)
// console.log(perseData)
// console.log(typeof perseData)

// Object - JSON 의 차이
// Object : Js 의 Key - Value 자료구조
// Json : Object 같이 생긴 str