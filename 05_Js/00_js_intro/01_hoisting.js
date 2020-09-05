// Hoisting !
// 나중에 선언된 변수를 참조 할 수 있음
// 함수 or statement 최상단으로 올려지는 것 (hoisting)
// 변수와 함수를 위한 메모리를 확보하는 과정

// console.log(a)
// var a = 10
// console.log(a)
// var가 hoist 되는 과정
//1. 선언이 최상단으로 올라감
//2. 선언이 최상단으로 올라갔기 때문에 에러가 나지 않고 undefined가 출력
// (TMI) Js 에서는 var 변수를 선언할 때 값을 넣어주지 않으면 undefined를 자동으로 넣어줌
//3 할당은 그 뒤에 이루어짐
//4. 최종출력


// let이 hoist 되는 과정
//1. 선언이 최상단으로 올라감
//2. 근데 에러??
//3. 할당
//4. 출력

// console.log(b)
// let b = 10
// console.log(b)

// var 할당 과정
// 1선언 - 초기화 (동시에 진행) --> 처음에는 값이 없기 때문에 Js가 undefined를 할당
// 2값의 할당 진행
// let 할당 과정
// 1선언 - 초기화 x
// 2.TDZ(Temporal Dead Zone) 임시적 사각지대
// 3.초기화 (초기에는 값이 없기 때문에 undefined) 할당
// 4.할당

// let foo
// let bar = undefined

// console.log(foo)
// console.log(bar)

// x

// let x = 1

// y

// var y = 1

// var y // 선언이 끌어 올려진다. 이때 초기화가 같이 이뤄지고 값이 없어서 undefined를 넣어준다
// y = 1 // 값이 할당된다
// console // 출력


if (x !== 1){
  console.log(y)
  var y = 3
  if (y === 3){
    var x = 1
  }
  console.log(y)
}

if (x === 1){
  console.log(y)
}

x = 7
console.log(y)
