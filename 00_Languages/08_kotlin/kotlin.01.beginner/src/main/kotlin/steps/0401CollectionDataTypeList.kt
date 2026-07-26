package org.example.steps

// https://kotlinlang.org/docs/kotlin-tour-collections.html#list

fun listDataTypeDeclare() {

    // feature
    // 1) ordered
    // 2) allow duplicate items

    // 1. to create read-only list : listOf()
    // (1) read-only list with val
    val readOnlyList = listOf("one", "two", "three")
    println(readOnlyList)

    // readOnlyList.add() // -> 불가

    // (2) read-only list with var
    var readOnlyListWithVar = listOf("one", "two", "three")
    println(readOnlyListWithVar)

    readOnlyListWithVar = listOf("one", "two", "three", "four")
    println(readOnlyListWithVar)

    // readOnlyListWithVar.add("five") // --> 이게 안됨


    // 2. to create mutable list : mutableListOf()
    // (1) mutable list with val
    // 리스트 안의 원소를 수정하느 ㄴ것 가능, 변수 자체에 할당되는 값은 변경 불가(val)
    val mutableListVal = mutableListOf("one", "two", "three")
    println(mutableListVal)

    mutableListVal.add("four")
    println(mutableListVal)

    // mutableListVal = mutableListOf(...) // -> 이건 불가

    // (2) mutable list with var
    // 변수 자체에 할당되는 값 변경 가능, 리스트 안의 원소를 수정하는 것도 가능
    var mutableList = mutableListOf("one", "two", "three")
    println(mutableList)

    mutableList = mutableListOf("one", "two", "three", "four")
    println(mutableList)

    mutableList.add("five")
    println(mutableList)


    // 3. 리스트 안에 다양한 데이터타입 가능
    val varietyTypeList = mutableListOf("one", 2, 3.0f, 4L)
    println(varietyTypeList)



    // 4. <> : 안에 들어갈 데이터 타입을 선언하기
    val declaredTypeList: MutableList<String> = mutableListOf("one", "two", "three")
    println(declaredTypeList)

    val voidList: MutableList<String> = mutableListOf() // 타입을 선언하면 빈 리스트 생성 가능 -> 타입을 알 수 있으므로 괜찮음
    println(voidList)

    val voidList2 = mutableListOf<String>() // 타입 선언은 이렇게 도 가능
    println(voidList2)

    // declaredTypeList.add(5) // --> 불가능

}

fun listDataTypeMethods() {

    val listDataType = mutableListOf<Any>()

    // add : 원소를 추가
    listDataType.add("one")
    listDataType.add(1, "two") // 넣을 인덱스 지정 가능
    listDataType.add(0, "three") // 원소가 있는 인덱스 순서에 원소를 넣으면 원래 원소부터 뒤로 밀림
    listDataType.add("four") // 인덱스를 지정하지 않고 add하면 가장 마지막으로 들어감
    println(listDataType) // -> [three, one, two, "four"]
    println()

    // remove : 원소를 제거
    listDataType.add("four")
    listDataType.remove("four") // --> 가장 첫 번째 four만 제거함
    println(listDataType)
    println()

    // [index] : 원소 번호(인덱스)로 원소에 접근
    println("the second value of list : ${listDataType[1]}")
    println()

    // .first() : 첫 원소, .last() : 마지막 원소
    println("the first value of list : ${listDataType.first()}")
    println("the last value of list : ${listDataType.last()}")
    println()

    // get number of item
    println("the number of elements : ${listDataType.count()}")
    println()

    // in, !in
    println("\"one\" is in the list : ${"one" in listDataType}")
    println("\"four\" is in the list : ${"four" in listDataType}")
    println("\"one\" is not in the list : ${"one" !in listDataType}")
    println("\"four\" is not in the list : ${"four" !in listDataType}")
    println()

    // addAll : 한 번에 여러 원소를 추가. 리스트를 넣는다면 python 의 extend 효과
    val addingList = mutableListOf("ten", "eleven", "twelve")
    listDataType.addAll(addingList)
    println(listDataType)
    println()
}
