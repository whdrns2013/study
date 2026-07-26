package org.example.steps

fun controlFlowIf() {

    // usage
    // 1) conditional expression 조건식은 괄호 () 안에 표현
    // 2) 조건에 따른 액션은 braces 중괄호 {} 안에 표현
    // 3) if 문이 아닌 경우에 대해서는 else 사용
    // 4) 다중 조건인 경우 else if 사용

    val limit : Int = 10
    var candidates: Int = 11

    if (candidates < limit) {
        println("pass")
    } else if (candidates == limit) {
        println("eqqal")
    } else {
        println("panic")
    }



    // 삼항 연산자 ? : 는 코틀린에 없음
    // 대신 if 문을 수식 안에 쓸 수 있음. 파이썬처럼 (순서는 다름)
    val theValue = if (candidates == limit) "pass" else if (candidates == limit) "equal" else "panic"
    println("theValue = $theValue")
}

fun controlFlowWhen() {

    // usage
    // when 은 다중 조건인 경우 사용하기 좋다.
    // 1) condition을 evaluate할 expression 은 괄호 () 안에 표현
    // 2) 조건과 조건일 경우 수행할 내용은 중괄호 {} 안에 표현
    // 3) 조건에 해당하는 경우 수행할 작업은 -> 로 가리킴
    // 4) 모든 조건에 해당하지 않는 경우는 else에 할당

    val score = 40

    when (score) {
        70 -> println("탈락")
        80 -> println("합격")
        90 -> println("합격")
        100 -> println("합격")
        else -> println("탈락")
    }
    println()


    // when 도 expression 이기 때문에 변수 값 할당 등에 사용 가능
    val result = when (score) {
        70 -> "탈락"
        80 -> "합격"
        90 -> "합격"
        100 -> "합격"
        else -> "탈락"
    }
    println(result)
    println()


    // when 을 쓸 때 condition 판단 대상을 미리 지정하지 않을 수도 있음
    val woCondition = when {
        score == 70 -> "탈락"
        score == 80 -> "합격"
        score == 90 -> "합격"
        score == 100 -> "합격"
        else -> "탈락"
    }
    println(woCondition)
    println()

}