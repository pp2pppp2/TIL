// Array helper method
// Helper -> 자주 사용하는 로직을 재활용 할 수 있게 도와주는 친구
// ES5 등장 -> ES6부터 사용도미
// forEach, filter, find, map, every, some, reduce

// 1.forEach
// forEach 주어진 callback을 배열에 있는 각 요소에 대해 오름차순으로 한번씩 실행

// // ES5
// var colors = ['red', 'blue', 'green']

// for (var i = 0; i < colors.length; i++){
//   console.log(colors[i])
// }
// // ES6

// colors.forEach(function(color){
//   console.log(color)
// })

// colors.forEach(color => 
//   console.log(color)
// )

// forEach는 아무것도 리턴하지 않습니다.

// forEach 연습문제

// ES5
// function handlePosts() {
//   const posts = [
//     { id: 23, title: 'Daily Js News ', },
//     { id: 52, title: 'Code Refactor City', },
//     { id: 105, title: 'The Brightest Ruby', },
//   ]
//   for (let i = 0; i < posts.length; i++){
//     console.log(posts[i])
//     console.log(posts[i].id)
//     console.log(posts[i].title)
//   }
// }

// handlePosts()

// ES6

// let handlePosts = _ => {
//   const posts = [
//     { id: 23, title: 'Daily Js News ', },
//     { id: 52, title: 'Code Refactor City', },
//     { id: 105, title: 'The Brightest Ruby', },
//   ]
//   posts.forEach( po => {
//     console.log(po)
//     console.log(po.id)
//     console.log(po.title)
//   })
// }

// handlePosts()

// const images = [
//   { height:10, width:30},
//   { height:20, width:90},
//   { height:54, width:32},
// ]

// const areas = []

// images.forEach( img => areas.push(img.height * img.width))
// console.log(areas)


// 2.filter
// 주어진 함수의 테스트를 통과하는 모든 요소를 모아서 새로운 배열로 반환하는 헬퍼
// 원하는 요소만 필터링 가능

// ES5
// const products = [
//   { name: 'cucumber', type: 'vegetable' },
//   { name: 'banana', type: 'fruit' },
//   { name: 'carrot', type: 'vegetable' },
//   { name: 'apple', type: 'fruit' },
// ]

// var fruitProducts = []



// for(var i = 0; i < products.length; i++){
//   if (products[i].type === 'fruit'){
//     fruitProducts.push(products[i])
//   }
// }

// console.log(products)
// console.log(fruitProducts)

// ES6+

// const PRODUCTS = [
//   { name: 'cucumber', type: 'vegetable' },
//   { name: 'banana', type: 'fruit' },
//   { name: 'carrot', type: 'vegetable' },
//   { name: 'apple', type: 'fruit' },
// ]

// const FRUIT_PRODUCTS = PRODUCTS.filter( product => product.type === 'fruit')

// console.log(FRUIT_PRODUCTS)

//ex1
//filter helper method를 사용하여 numbers 배열 중 50 보다 큰 값만 필터링해서
// filteredNumbers 라는 배열에 담아주세요

// const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]

// const filteredNumbers = numbers.filter( number => number > 50)

// console.log(filteredNumbers)
// //ex2
// // users 배열에서 admin 레벨이 true인 유저 object만 filteredUsers 라는 배열에 담아서
// // filteredUsers 배열의 두번째 유저 이름을 출력해보세요

// const users = [
//   { id :1, admin:false, name: 'justin'},
//   { id :2, admin:false, name: 'harry'},
//   { id :3, admin:true, name: 'tak'},
//   { id :4, admin:false, name: 'jason'},
//   { id :5, admin:true, name: 'juan'},
// ]

// const filteredUsers = users.filter( user => user.admin === true)

// console.log(filteredUsers[1].name)

// 3.find
// 주어진 판별 함수를 만조한느 첫번째 요소 값을 반환 값이 없다면 undefined 반환
// ES5
// var users = [
//   { name: 'Tony stark', age:45 }, 
//   { name: 'steve Rogers', age:32 }, 
//   { name: 'Thor', age:40 }, 
//   { name: 'Tony stark', age:23 }, 
// ]

// for(var i = 0; i < users.length; i++){
//   if (users[i].name === 'Tony stark'){
//     var user = users[i]
//     break
//   }
// }

// ES6
// const user = users.find( function(user){
//   return user.name === 'Tony stark'
// })
// const user = users.find( user => user.name === 'Tony stark')
// console.log(user)

// PEOPLE 중에 admin 권한을 가진 요소를 찾아서 admin 상수에 저장해보자!

// const PEOPLE = [
//   { id:1, admin:false },
//   { id:1, admin:false },
//   { id:1, admin:true },
// ]

// const admin = PEOPLE.find( person => person.admin === true )
// console.log(admin)


// 4.map
// 배열 내의 모든 요소에 대해 각각 주어진 함수를 호출한 결과를 모아 새로운 배열 return
// 일정한 형식의 배열을 다른 형식으로 바꿀 때 사용한다.


// ES5
// var numbers = [1, 2, 3]
// var doublenumbers = []
// for ( var i = 0; i < numbers.length; i++){
//   doublenumbers.push(numbers[i] * 2)
// }

// console.log(numbers)
// console.log(doublenumbers)

// // ES6

// const NUMBERS = [1, 2, 3]
// const DOUBLE_NUMBERS = NUMBERS.map(function(number) {
//   return number * 2
// })

// console.log(NUMBERS)
// console.log(DOUBLE_NUMBERS)

// ex1)
// 숫자가 담긴 배열을 받아 각 숫자의 제곱근이 들어있는 새로운 배열 만들기

// const numbers = [4, 9 , 16]
// const roots = numbers.map(Math.sqrt)

// console.log(roots)

// // ex2)
// // images 배열 내의 object 안에 있는 height 값을 heights 라는 상수에 담아보세요

// const images = [
//   { height: '34px', width: '39px'},
//   { height: '54px', width: '19px'},
//   { height: '83px', width: '75px'},
// ]

// const heights = images.map( img => img.height )
// console.log(heights)
// // ex3
// // distance / time -> 속도를 저장하는 speeds(배열)을 만들어 보세요.

// const trips = [
//   { distance: 30, time: 10 },
//   { distance: 90, time: 50 },
//   { distance: 59, time: 20 },
// ]
// const speeds = trips.map( trip => trip.distance/trip.time )
// console.log(speeds)

// ex 4
// // 다음 두 배열을 객체 형태로 결합한  comics 라는 배열을 만들어 보자
// const brands = ["Marvel", "DC"]
// const movies = ["IronMan", "BatMan"]

// // x = 현재 elem
// // i = 그 elem의 index

// const comics = brands.map( (x, i) => ({ name : x, hero: movies[i]}))

// console.log(comics)

// 5. some & every
// some 과 every는 대상 배열에서 특정 요소를 뽑거나, 배열을 return 하지 않고
// 조건에 대해 boolean을 return

// some
// 배열 내의 "어떤 요소"라도(===하나라도) 주어진 함수를 통과하는지 테스트하고 결과에 따라 boolean return

// every
// 배열 내의 "모든 요소"가 주어진 함수를 통과하는지 테스트하고 결과에 따라 boolean return

// const arr = [1, 2, 3, 4, 5]

// const result = arr.some( elem => elem % 2 === 0 )
// console.log(result)

// const result2 = arr.every( elem => elem % 2 === 0 )
// console.log(result2)

// // some&every 
// const COMPUTERS = [
//   { name: 'macbook', ram:16 },
//   { name: 'gram', ram:8 },
//   { name: 'series9', ram:32 },
// ]

// // 1. some
// const someComputerAvailable = COMPUTERS.some( computer => computer.ram > 16)
// console.log(someComputerAvailable)

// // 2. every
// const everyComputerAvailable = COMPUTERS.every( computer => computer.ram > 16)
// console.log(everyComputerAvailable)



// 6.reduce
// 배열의 각 요소에 주어진 reducer 함수를 실행하고, 하나의 결과값을 return 합니다.
// 배열 내에 숫자, 총합, 평균 계산 등에 활용합니다. (배열의 값을 하나로 줄이는 일)

// const ssafyTests = [90, 90, 80, 77]
// // total = 누적값ssddssds
// // x = 배열의 요소

// const sum = ssafyTests.reduce((total, x) => total += x, 13)
// console.log(sum)

// const avg = ssafyTests.reduce((total, x) => total += x) / ssafyTests.length
// console.log(avg)

// // ex1 
// // 배열 내 요소의 총합 구하기
// const arr = [0, 1, 2, 3]
// const totalSum = arr.reduce( (total, x) => total + x )
// console.log(totalSum)

// // ex2
// // 배열에 담긴 중복된 이름을 { '이름' : 수 }의 object로 반환하세요. (심화)

// const names = ['harry', 'jason', 'tak', 'tak', 'justin']
// const countedNames = names.reduce((allNames, name) => {
//   if (name in allNames){
//     allNames[name]++
//   }
//   else{
//     allNames[name] = 1
//   }
//   return allNames
// }, {})

// console.log(countedNames)