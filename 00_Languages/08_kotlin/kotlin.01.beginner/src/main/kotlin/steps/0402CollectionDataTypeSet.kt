package org.example.steps

fun declareSetDataTypes() {

    // feature
    // 1) unordered
    // 2) unique

    // 1. declare read-only set
    val readonlySet = setOf("One", "Two", "Three")
    // readonlySet.add("Four") // --> 원소 수정 불가
    println(readonlySet)
    println()

    // 2. declare mutable set
    val mutableSet = mutableSetOf("One", "Two", "Three")
    mutableSet.add("Four")
    println(mutableSet)
    println()

    // 3. variety type set
    val varietySet : MutableSet<Any> = mutableSetOf("one", 2, 3.0f)
    println(varietySet)
    println()

    // 4. void set : 데이터 타입만 선언했다면 빈 셋 가능
    val voidSet : MutableSet<Any> = mutableSetOf()

    // 5. unique : 같은 값을 여러 개 넣어도 하나만 유지됨
    val uniqueSet = mutableSetOf("one", "one", "two", "three", "three")
    println(uniqueSet)
}

fun methodsOfSet() {

    // 1. add : 원소 하나 추가
    val set = mutableSetOf<String>()
    set.add("one")
    println(set)
    println()

    // 2. addAll : 여러 개의 원소 추가
    val addingSet = mutableSetOf("two", "three", "one")
    set.addAll(addingSet)
    println(set)
    println()

    // 3. remove : 원소 제거
    addingSet.add("four")
    addingSet.remove("three")
    println(set)
    println()

    // 4. in, not in
    println("one is in set : ${"one" in set}")
    println("three is in set : ${"three" in set}")
    println("one is not in set : ${"one" !in set}")
    println("three is not in set : ${"three" !in set}")
}