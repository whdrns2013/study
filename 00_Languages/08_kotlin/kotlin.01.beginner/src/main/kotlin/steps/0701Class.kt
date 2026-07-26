package org.example.steps

// kotlin 은 객체지향 프로그래밍을 지원함

// 1. 클래스는 class 키워드를 이용해 선언한다.
// 2. 클래스에 대한 속성을 선언할 때에는 클래스명 뒤에 괄호 () 를 두고, 그 안에 속성 이름과 데이터타입을 명시해둔다. -> 이 부분의 내용을 클래스 헤더라고 함
// 3. 클래스 본문은 중괄호 {} 안에 선언한다.
// 4. 주의할점은 속성의 mutable이다. 속성의 값이 나중에 바뀌어야 하면 var, 바뀌지 않아도 된다면 val을 사용한다. val이나 var를 없이 선언할 수도 있는데, 이 경우 인스턴스가 생성된 후로는 접근할 수 없다?
// 5. 속성은 기본값을 가질 수 있다.
// 6. 클래스의 멤버 함는 클래스 본문{} 내에 선언할 수 있다.

class Food(val name: String, var price: Int = 0) {
    var category: String = ""

    fun introduce() {
        println("$name is one of $category food. price is $price")
    }
}

// class 를 사용할 때, 생성자를 이용해 인스턴스를 선언할 수 있다.
// 코틀린은 기본적으로 클래스 헤에 선언왼 매개변수를 사용해 생성자를 자동으로 생성한다.

fun usingClass() {

    // 클래스 인스턴스 선언
    val kimbob:Food = Food("Kimbob", 3000)

    // 클래스 인스턴스 속성에 접근
    // . 을 이용해 속성에 접근할 수 있다.
    println(if (kimbob.category != "") kimbob.category else "None")
    println(kimbob.name)
    println(kimbob.price)
    println()

    // 클래스 인스턴스 속성 값 업데이트
    kimbob.category = "Korean"
    kimbob.price = 3500
    println(kimbob.category)
    println(kimbob.name)
    println(kimbob.price)
    println()

    // val 속성은 업데이트 하지 못함
    // kimbob.name = "bibimbob"

    // 클래스의 멤버 함수 또한 . 을 가지고 사용할 수 있다.
    kimbob.introduce()
}

// 데이터 클래스
// 코틀린에는 데이터를 저장하는 데 유용한 데이터 클래스라는 게 있다.
// 파이썬에서 @dataclass 로 사용하는 그거 같은데.
// 이는 일반적인 클래스와 비슷하지만, 추가적인 멤버함수가 포함되어있음
// 1. data class 키워드를 사용해 선언한다.
// 2. toString() 멤버 함수 : 클래스 인스턴와 해당 속성을 읽기 쉬운 문자열로 출력한다. 별도 선언하지 않아도 사용할 수 있다.
// 3. equals() 또는 == : 클래스의 인스턴스를 비교한다. 이 또한 별도 선언하지 않아도 사용할 수 있다.
// 4. copy() : 다른 클래스의 인스턴스를 복사해 생성하며, 이때 일부 속성은 다를 수 있음. 또한 별도 선언하지 않아도 사용할 수 있다.

data class User(var name: String, var age: Int)

fun usingDataClass() {

    val tintin = User(name="tintin", age=20)
    val mushroom = User(name="mushromm", age=30)
    val tintinCopy = User(name="tintin", age=20)

    // toString :: println을 하면 자동적으로 적용되기도 하고, 명시적으로 써도 됨
    println(tintin)
    println(tintin.toString())
    println()

    // equals(), == :: 인스턴스 간 동일한지 체크
    println(tintin == tintinCopy)
    println(tintin.equals(mushroom))
    println()

    // copy() :: 인스턴스를 복사. copy를 할 때 대체 속성값을 부여할 수도 있다.
    val tomato = tintin.copy(name="tomato")
    println(tomato)

}