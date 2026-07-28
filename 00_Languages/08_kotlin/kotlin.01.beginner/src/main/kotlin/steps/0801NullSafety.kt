package org.example.steps

// null
// 코틀린에서 null 값을 가질 수 있다.
// null은 값을 받지 못했거나 아직 정해지지 않은 경우에 사용된다.
// 코틀린에서는 null이 가져올 프로그램에서의 문제를 방지하고자 null safety 기능을 제공한다.
// 이는 null 값으로 인해 런타임시에 겪을 수 있는 잠재적인 문제를 컴파일시에 포착함으로써 프로그램 안정성에 기여한다.

// nullable type
// 코틀린에서 모든 타입은 기본적으로 null을 허용하지 않는다.
// 따라서 nullable 타입을 선언해 사용해야 하며, 이는 선언시 타입 뒤에 `?` 를 붙임으로써 실현 가능하다.

fun nullable() {

    // 기본 타입 : 널 불가
    var defaultDataType : String = "Hello Kotlin"
    // defaultDataType = null --> 오류

    // 타입 미선언시(자동 추론시) : 널 불가
    var woTypeDeclare : String = "Hello Kotlin"
    // woTypeDeclare = null --> 오류

    // nullable
    var nullableDataType : String? = "Hello Kotlin"
    nullableDataType = null
    println(nullableDataType)
}

fun nullcheck() {

    var defaultDataType : String = "Hello Kotlin"
    var nullableDataType : String? = null

    // 1. null이면 안되는 함수
    fun strLength(text: String): Int {
        return text.length
    }
    println(strLength(defaultDataType))
    // println(strLength(nullableDataType)) // --> 이렇게 하면 컴파일 에러 발

    // 2. null check
    // 위와 같은 경우에 대해서는 null check를 수행하는 게 옳음
    fun describeString(maybeString: String?): Int {
        if (maybeString != null && maybeString.length > 0){
            return maybeString.length
        } else {
            return 0
        }
    }

    describeString(nullableDataType) // -> 컴파일 에러 안남
}

fun safetyCall(){

    // null을 포함할 수도 있는 객체의 속성에 안전하게 접근하려면 safetyCall 연산자인 ?.를 사용하자
    // 이 safety call 연산자는 접근하려는 객체, 속성에 null이 존재하는 경우, null값을 반환한다.
    // 이는 코드에서 null 값이 존재해 오류를 일으키는 경우를 방지하는 데 유용하다.
    fun lengthString(maybeString: String?): Int ? = maybeString?.length

    println(lengthString("Hello Kotlin"))
    println(lengthString(null))

    // 이는 클래스를 통해 만들어진 객체에도 해당이 된다.
    class Address(var country:String)
    class Company(var name:String, var address:Address?)
    class Person(var name:String, var age:Int, var company: Company?)

    val githubCompanyAddress = Address(country="U.S.A")
    val githubCompany = Company(name="Github", address=githubCompanyAddress)
    val john = Person(name="Mike", age=25, company=null)

    println(john)
    println(john.company?.address?.country)
}

fun elvisOperator() {

    // elvis 연산자를 사용하면 null 일 경우 대체할 기본값을 지정할 수 있다.
    // elvis 연산자 : `?:`

    fun lengthString(maybeString: String?): Int? = maybeString?.length

    var targetString :String? = "Hello Kotlin"
    println(lengthString(targetString) ?: 0)

    targetString = null
    println(lengthString(targetString) ?: 0)
}