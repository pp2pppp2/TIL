// primitive(원시) 타입
// const a = 13
// const b = -5
// const c = 3.14
// const d = 2.99e8 // 10^8
// const e = Infinity
// const f = -Infinity
// const g = NaN // Not a Number
// console.log(a,b,c,d,e,f,g)

// string

// const sentence1 = 'Ask and go to the blue'
// const sentence2 = "Ask and go to the blue"
// const sentence3 = `Ask and go to the blue`
// console.log(sentence1,sentence2,sentence3)

// 따옴표를 사용하면 줄바꿈 불가 -> 백틱 이용!

// const word = "안녕\n하세요"
// console.log(word)

// const word = `안녕
// 하세요`
// console.log(word)

// backtick -> 줄바꿈 + 문자열 사이에 변수도 넣을 수 있다?!?!! 단, 이스케이프 문자는 사용이 불가능 하오니 이부분 주의해주시길 바랍니다.

// const word2 = `안녕
// 하에여`
// console.log(word2)

// const age = 10
// const message = `홍길동은 ${age}세 
// 입니다`
// console.log(message)

// 문자열 이어 붙이기

// const happy = 'Will you join us?'
// const hacking = 'Happy' + 'Hacking' + '!'
// console.log(happy,hacking)

// Boolean

// const truthy = true
// const falsy = false

// console.log(truthy, falsy)
// console.log(typeof truthy)
// console.log(typeof falsy)


// Empty value
// Js -> null, undefined

// let first_name // Js 가 넣어줌
// console.log(first_name)

// let last_name = null // 의도적으로 값이 없음을 명시함
// console.log(last_name)

// console.log(typeof null)
// console.log(typeof undefined)

// console.log(null == undefined ) // 동등 비교 연산자
// console.log(null === undefined ) // 일치 연산자

// console.log(!null)
// console.log(!undefined)

// 연산자

// 할당 연산자
// let c = 0

// c += 10
// console.log(c)

// c -= 3
// console.log(c)

// c += 10
// console.log(c)

// c++
// console.log(c)

// c--
// console.log(c)

// 비교
// 변수앞에 let const var 를 붙여주지 않으면 Js 가 자동으로 var를 붙여줍니다.

// console.log(3 > 2)

// console.log('A' < 'B')
// console.log('가' < '나')

// 동등 비교 연산자 ( == ) 아예 안씀
// 느슨한 평가

// const a = 1
// const b = '1'

// console.log(a == b)
// console.log(a != b)
// console.log(a == Number(b))

// // 자동형 변환 예시

// console.log(8 * null) // 0
// console.log("5" - 1) // 4
// console.log("5" + 1) // 51
// console.log("five" * 2) // NaN

// 일치 연산자 (===)
// 엄격한 평가

// const a = 1
// const b = "1"

// console.log(a === b)
// console.log(a === Number(b))


// // 논리 연산자
// // and
// console.log( true && false )

// console.log( 1 && 0 )
// console.log( 0 && 1 )
// console.log( 4 && 7 )

// // or
// console.log( true || false)

// console.log( 1 || 0 )
// console.log( 0 || 1 )
// console.log( 4 || 7 )

// // not
// console.log(!true)
// console.log(!false)

// 삼항 연산자
// 가장 앞이 Boolean 값이 참이면 앞의 값이 반환되고 반대일 경우 뒤의 값이 반환

// console.log(true ? 1 : 2)
// console.log(false ? 1 : 2)
// console.log('nyapy' ? 'nice' : 'awesome')

// // 삼항 연산의 결과를 변수에 할당 할 수 있다.!

// const result = Math.PI > 4 ? "Yep" : "Nope"
// console.log(result)