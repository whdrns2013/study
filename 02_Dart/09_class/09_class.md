

## 클래스 작성법

클래스의 기본적인 작성법은 Java 등 다른 객체지향 언어들과 동일합니다.  
class 라는 말을 쓰고, 대문자로 시작하는 클래스명을 적어주고, 중괄호 안에 클래스의 내용을 적어주죠.  
그리고 property와 method들을 가질 수 있습니다. 하지만 class 안에 또 다른 class는 선언할 수 없습니다.  

```dart
class Player {
    String name = 'default name';
    int level = 0;
    final job = 'magician';
}
```

### class 인스턴스(객체) 생성  

클래스를 작성한 뒤, 함수에서 사용할 때에는 `var 인스턴스명 = 클래스명();` 혹은 `클래스명 인스턴스명 = 클래스명();` 과 같이 작성해주면 됩니다.  

```dart
class Player {
    String name = 'default name';
    int level = 0;
    final job = 'magician';
}

void main() {
    var player01 = Player();
    Player player02 = Player();
    print(player01.name);
    print(player02.name);
}
// ==============================
// >> default name
// >> default name
```


### class의 property  

클래스의 property는 클래스 안의 변수를 의미합니다. property를 선언할 때에는 데이터타입을 명시해주는 것이 권장됩니다. var나 dynamic과 같은 데이터타입은 권장되지 않습니다. 이는 자신 혹은 다른 사람이 코드를 봤을 때 명확한 자료형을 추론할 수 있도록 하기 위함과 함께, 데이터타입을 명시해줌으로써 프로그래밍 상의 오류가 없도록 하기 위함도 있습니다.  

클래스를 생성하여 사용할 경우 생성된 인스턴스의 property는 기본적으로 수정할 수 있습니다. final로 선언된 변수가 아니라면요. 만약 어떤 property를 수정할 수 없게 하고 싶다면 final 변수로 선언해주면 됩니다.  

```dart
class Player {
    String name = 'default name';  // 데이터타입을 명시해주는 것이 권장됨
    int level = 0;                 // 데이터타입을 명시해주는 것이 권장됨
    final job = 'magician';        // 값을 변경할 수 없게 final로 선언
}

void main() {
    var player01 = Player();
    print(player01.name);     // >> default name
    player01.name = 'jongya';
    print(player01.name);     // >> jongya
    player01.job = 'warrior'; // >> 오류 발생
}
```


### 같은 클래스의 서로 다른 인스턴스

동일한 클래스의 서로 다른 두 개 이상의 인스턴스가 있을 경우를 생각해보겠습니다. 둘은 서로 영향을 미칠 수 있을까요?  

그렇지 않습니다. 동일한 클래스로 생성된 인스턴스들이라도 각각은 서로 독립된 객체입니다. 예시를 들어보겠습니다.  

```dart
class Player {
    String name = 'default name';  // 데이터타입을 명시해주는 것이 권장됨
    int level = 0;                 // 데이터타입을 명시해주는 것이 권장됨
    final job = 'magician';        // 값을 변경할 수 없게 final로 선언
}

void main() {
    var player01 = Player();
    print(player01.name);     // >> default name
    player01.name = 'jongya';
    print(player01.name);     // >> jongya

    Player player02 = Player();
    print(player02.name);     // >> default name
}
```


### 클래스 안의 method  

클래스는 method 즉 함수를 가질 수 있습니다. 그리고 이를 인스턴스를 통해 활용할 수도 있습니다. 앞서 살펴 본 property의 사용법과 동일하죠.  

```dart
class Player {
    String name = 'default name';  // 데이터타입을 명시해주는 것이 권장됨
    int level = 0;                 // 데이터타입을 명시해주는 것이 권장됨
    final job = 'magician';        // 값을 변경할 수 없게 final로 선언

    void introduction() {
        print('Hi. my name is $name');
    }
}

void main() {
    Player player01 = Player();
    player01.introduction();
    player01.name = 'jongya';
    player01.introduction();
}
// ==============================
// >> Hi. my name is default name
// >> Hi. my name is jongya
```

만약 클래스 안의 property 명과 클래스의 함수 안의 지역변수 명이 동일하다면 어떻게 될까요? 물론 이러한 상황이 이상적이지는 않지만, 피할 수 없는 상황이라면 `this.property명`과 `지역변수명`으로 구분지어 사용할 수 있습니다.  
*겹치지 method 내에 겹치는 변수명이 없다면 $name 만 사용해도 class property를 가리킵니다.*  


|구분|설명|
|---|---|
|$변수명|함수 안의 변수를 가리킴|
|${this.변수명}|클래스의 property 를 가리킴|


```dart
class Player {
    String name = 'default name';  // 데이터타입을 명시해주는 것이 권장됨
    int level = 0;                 // 데이터타입을 명시해주는 것이 권장됨
    final job = 'magician';        // 값을 변경할 수 없게 final로 선언

    void introduction() {
        var name = 'name in method';
        print('Hi. my name is $name');
        print('Hi. my name is ${this.name}');
    }
}

void main() {
    Player player01 = Player();
    player01.introduction();
    player01.name = 'jongya';
    player01.introduction();
}
// ==============================
// >> Hi. my name is name in method
// >> Hi. my name is default name
// >> Hi. my name is name in method
// >> Hi. my name is jongya
```

## Constructor Method  

Constructor Method 는 클래스 인스턴스를 생성할 때 property를 함께 설정해줄 수 있는 함수를 의미합니다. 클래스 안에 선언되는데, 아래 예시를 살펴보겠습니다.  

```dart
class Player {

    late String name;
    late int level;
    late final String job;

    Player(String name, int level, String job){
        this.name = name;
        this.level = level;
        this.job = job;
    }

    void introduction() {
        print('Hi. my name is $name. level is $level and my job is $job');
    }
}

void main() {
    Player player01 = Player('jongya', 10, 'magician');
    print(player01.name);
    player01.introduction();
}
```

가장 먼저 눈여겨 볼 것은 Player calss 안의 Player 라는 method 입니다. 이것이 바로 Constructor Method로, 인스턴스를 만들 때 인스턴스의 특성을 함께 부여하는 역할을 하죠.  

그리고 두 번째로는 아래 main 함수에서 사용된 인스턴스 생성 부분입니다. 앞서 살펴본 것들과는 다르게 인스턴스 생성시 Player() 안에 파라미터들이 있는 것을 볼 수 있습니다. 이러한 작성 방식이 바로 Constructor Method 를 통해 인스턴스를 만드는 방식입니다.  

세 번째로는 late 수식어입니다. 지난 변수 선언 관련 포스트에서 late 수식어는 나중에 살펴보기로 했었는데요, 그게 바로 지금입니다. late는 변수의 초기화를 지연시키는 수식어로, 위 코드에서 late가 없다면 class 안의 Player(...) Constructor Method는 초기화되지 않은 변수를 받게 되고, 이는 오류로 이어지게 됩니다. 즉 컴파일 자체가 불가능해지는 것이죠. 이 late 변수를 사용함으로 인해서 "이 변수(property) 들은 나중에 초기화될 것이니 안심하고 써" 가 되는 것입니다.  



## Reference

https://nomadcoders.co/dart-for-beginners/lectures/4113  
https://nomadcoders.co/dart-for-beginners/lectures/4114  
https://nomadcoders.co/dart-for-beginners/lectures/4115  
https://nomadcoders.co/dart-for-beginners/lectures/4116  
https://nomadcoders.co/dart-for-beginners/lectures/4117  
https://nomadcoders.co/dart-for-beginners/lectures/4118  
https://nomadcoders.co/dart-for-beginners/lectures/4119  
https://nomadcoders.co/dart-for-beginners/lectures/4120  
https://nomadcoders.co/dart-for-beginners/lectures/4121  
https://nomadcoders.co/dart-for-beginners/lectures/4122  
https://nomadcoders.co/dart-for-beginners/lectures/4123  