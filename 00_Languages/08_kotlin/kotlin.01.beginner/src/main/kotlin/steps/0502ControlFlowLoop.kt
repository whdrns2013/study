package org.example.steps

 fun controlFlowRanges() {

     // Ranges : 연속되는 값의 범위를 지정하는 방법

     // 1. n..m
     // n 이상 m 이하의 연속된 정수 또는 문자형 iterate??를 반환
     println(1..4)
     println()

     // 2. n..<m
     // n 이상 m 미만의 연속된 정수 또는 문자형 iterate??를 반환
     println(1..<4)
     println()

     // 3. n<..<m
     // 같은 건 없음
     // println(1<..<4)

     // 4. downTo
     // 증가하는 방향이 아닌, 감소하는 방향으로 iterate하고사 할 때
     println(4 downTo 1)
     // 사실 .. 이 downTo 와 같은 듯
     println(1 downTo 4)
     println(1 .. 4)
     println()

     // 5. step
     // .. 또는 downTo를 할 때 한 번에 이동할 거리 즉, interval
     println(1 .. 10 step 2) // -> 1..9 step 2
     println(10 downTo 1 step 2) // -> 10 downTo 2 step 2

     // 6. 문자형
     // 문자형도 interval이 정해져 있기 때문에 가능
     println('a' .. 'd')
     println('d' downTo 'a')
     println('a' .. 'd' step 2)
 }

fun controlFlowLoop() {
    // Loop 는 for 와 While이 있음

    // 1. For
    // 일정 범위를 순회하며 동작을 수행
    // iterate를 입력받아야 한다.
    // iterate 식은 괄호 () 안에 작성한다.
    // 각 스텝마다 행할 동작은 중괄호 {} 안에 작성한다.

    for (number in 1..10 step 2) {
        println(number)
    }
    println()

    // list, set, map과 같이 iterate한 Collection 도 가능
    val mutableMap = mutableMapOf("one" to 1, "two" to 2, "three" to 3, "four" to 4)
    for ((key, value) in mutableMap) {
        println("$key -> $value")
    }
    println()


    // 2. while
    // while 은 특정 조건을 만족하는 경우 계속 반복하는 흐름을 만든다.
    var candidates = 0
    val limit = 10
    while (candidates < limit) {
        println("candidates : ${candidates++} -> limit : $limit")
    }
    println()

    // 최소 1회를 실행하게 하려면 do-while 문을 사용한다.
    var newCandidates = 0
    val newLimit = 10
    while (newCandidates < newLimit) {
        println("candidates : ${newCandidates++} -> limit : $newLimit")
    }
    do {
        println("Panic! Candidates Limit Over : ${++newCandidates} -> limit : $newLimit")
    } while (newCandidates < newLimit*1.5)
    println()
}























