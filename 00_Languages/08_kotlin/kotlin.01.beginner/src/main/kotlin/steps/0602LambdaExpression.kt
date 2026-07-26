package org.example.steps

// Lambda Expression
// 익명함수
// 1. 어떤 동작을 함수의 인자로 전달하거나,
// 2. 변수에 동작을 담아서 재사용하기 위한 목적
// 사용법은 아래와 같다.
// (1) 람다함수는 중괄호 {} 안에 작성한다.
// (2) 입력받는 변수와 그 타입을 선언한 뒤, -> 로 동작을 가리킨다.
// (3) -> 뒤에는 실행할 동작이 담기며, return 된다.

fun lambdaExample() {

    // 일반적으로 함수를 선언해 사용할 때
    fun customSum(a: Int, b: Int): Int {
        return a + b
    }

    val sumResult = customSum(a=1, b=2)
    println(sumResult)


    // lambda 함수
    val lambdaSumResult = { a : Int, b : Int -> a + b }
    println(lambdaSumResult(1, 2))
}

// Iterate에 대한 filter 에 유용함

fun passToAnotherFunction() {
    // Iterate 에 대해 filter를 수행할 때 유용함

    val numbers = listOf(1, -2, 3, -4, 5, -6)

    // lambda로 한줄에
    val positives = numbers.filter({ x -> x > 0 })

    // lambda를 쓰나 이렇게 써도 됨
    // 설명이 좀 필요한데, negativeFilter는 조건함수가 됨
    // numbers.filter는 컬렉션 안의 원소를 순회하므로 각각의 원소에 대해 negativeFilter 익명함수를 수행
    val negativeFilter = {x:Int -> x < 0}
    val negatives = numbers.filter(negativeFilter)

    // 결과 확인
    println(positives)
    println(negatives)
    println(negativeFilter)
}

// Lambda 함수의 타입 선언
// Lambda 함수에 대해서도 : 로 타입 선언이 가능하며, 동시에 반환값 타입 지정도 가능
// 변수 : (입력타입) -> 반환타입 = { 익명함수 식 }

fun typedLambda() {

    val isLowerLambda : (String) -> Boolean = {
        s -> s.lowercase() == s
    }

    println(isLowerLambda("Hello"))
    println(isLowerLambda("hello"))

}

// fun 과 lambda를 결합해 사용하기

fun discount(level: String): (Int) -> Int =
    when (level) {
        "VIP" -> {price -> price * 90/100}
        "GOLD" -> {price -> price * 95/100}
        else -> {price -> price}
}

// 람다함수를 변수에 할당하지 않고 바로 사용하기
// Invoke seperately
fun invokeSeperately(){
    println({a:Int, b:Int -> a + b}(10, 20))
}