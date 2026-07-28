package org.example.steps

fun declareMapDataTypes() {

    // feature
    // 1) key-value pair
    // 2) not using index, using "key"
    // 3) key is unique
    // 4) value can duplicate

    // 1. read-only map
    val readOnlyMap = mapOf("one" to 1, 2 to "two", 3.0f to "three")
    println(readOnlyMap)
    println()

    // 2. mutable map
    val mutableMap = mutableMapOf("one" to 1, "two" to 2, "three" to 3.0f)
    mutableMap["four"] = 4
    println(mutableMap)
    println()

    // 3. unique key : 동일한 키에 값을 다시 할당하면 덮어씌워짐
    mutableMap["one"] = 1.00f
    println(mutableMap)
    println()

    // 4. type : 타입 지정
    val typedMap : MutableMap<String, Int> = mutableMapOf("one" to 1, "two" to 2, "three" to 3)
}

fun methodsOfMapDataTypes() {

    val map = mutableMapOf<String, Any>("one" to 1, "two" to 2, "three" to 3.0f)

    // 1. add - []
    map["four"] = 4
    println(map)
    println()

    // 2. remove : 원소 제거 - 키로 접근
    map.remove("two")
    println(map)
    println()

    // 3. count : 원소 개수 (쌍 개수)
    println("len of map : ${map.size}")
    println("len of map : ${map.count()}")
    println()

    // 4. containsKey : 특정 키를 포함하는지 확인
    println("key one is in map : ${map.containsKey("one")}")
    println("key one is not in map : ${!map.containsKey("one")}")
    println()

    // 5. containsValue : 특정 값을 포함하는지 확인
    println("value 1 is in map : ${map.containsValue(1)}")
    println("value 2 is in map : ${map.containsValue(2)}")
    println()

    // 6. keys : 키 목록 (속성 - 배열 형태로 출력됨)
    println(map.keys)
    println()

    // 7. values : 값 목록 (속성 - 배열 형태로 출력됨)
    println(map.values)
    println()

    // 8. 따라서 containseKey, containseValue를 사용하지 않고 동일한 작동을 하게 하려면
    println("key one is in map : ${"one" in map.keys}")
    println("value 1 is in map : ${2 in map.values}")
}