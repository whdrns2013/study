package org.example.steps

// function
// 1. fun 키워드를 통해 함수임을 가리킬 수 있다.
// 2. 파라미터는 괄호 () 안에 작성한다.
// 3. 각 파라미터는 모두 타입을 가지고 있어야 한다.
// 4. 파라미터가 여러개인 경우 콤마(,)로 구분한다.
// 5. 반환 리턴값의 타입은 함수 뒤 () 뒤에 콜론 : 다음에 작성한다.
// 6. return 키워드는 함수를 종료하며, 특정 값을 함수를 호출한 지점으로 반환한다.
// 7. 함수로부터 반환할 값이 없다면 그냥 `return`만 쓰거나, `return Unit`을 쓰거나, 혹은 return을 아예 쓰지 않으면 된다.

fun sum(a: Int, b: Int): Int {
    return a + b
}

// default parameter
// 함수를 선언할 떄 파라미터의 기본값을 정할 수 있다.
// 기본값이 정해진 파라미터는, 함수가 호출될 때 해당 파라미터가 들어오지 않으면 기본값이 사용된다.

fun sum2(a: Int, b: Int=10): Int {
    return a + b
}

// using function
// 함수를 호출해 사용할 때에는 함수명(파라미터 및 값) 과 같은 형식으로 사용한다.
// 파라미터를 넣는 방법은 두 가지이다.
// 1) positional arguments : 파라미터 순서에 맞춰 값을 넣음 --> 간결
// 2) named arguments : 파라미터와 넣을 값을 매칭함 --> 정확, 권장

fun execFunction(){

    val a1 = 1
    val b1 = 2

    val result1 = sum(a1, b1)
    println(result1)

    val result2 = sum2(a=a1)
    println(result2)

}