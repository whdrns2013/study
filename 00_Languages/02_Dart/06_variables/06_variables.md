

## 변수의 선언  

Dart에서 변수 선언 방법은 두 가지가 있다.  

(1) var 변수명 선언

Dart에서 기본적인 변수 선언 방법은 `var 변수명 = 값;` 이다.  
Dart에서는 값의 데이터 타입을 자동으로 파악해 변수의 데이터 타입을 선언해놓는다.  

```dart
void main() {
  var name = 'some name';
  print(name + " | " + name.runtimeType.toString());
}
--------------------------
// >> some name | String
```

(2) 데이터타입을 명시한 변수명 선언  

데이터타입을 명시하여 변수명을 선언할 수도 있다.  
아래 예시를 참고해보자.  

```dart
void main() {
    String name = 'some name';
    print(name + " | " + name.runtimeType.toString());
}
--------------------------
// >> some name | String
```

(3) 두 가지 변수 선언은 각각 언제 사용될까?  

관습적으로 var를 이용한 변수명 선언은 지역변수(Ex.함수 안쪽)로, 그리고 데이터타입을 명시한 변수명 선언은 전역변수에서 사용한다.  
또한 이 방식은 dart 의 스타일가이드에서도 권장하는 방식이다.  


<br>

## 변수 값 update  

동일한 변수명으로 안에 있는 값을 변경하는 방법을 알아보겠다.  
update 하려는 값이 동일한 데이터타입인 경우에는 문제 없이 변수 안의 값이 변경된다.  

```dart
void main() {
  var name = 'first name';
  name = 'second name';
  print(name + " | " + name.runtimeType.toString());
}
--------------------------
// >> second name | String
```

하지만 변수의 값을 다른 데이터타입으로 update 할 때에는 오류가 생기니 꼭 주의하자.  

```dart
vodi main() {
    var name = 'some name';
    name = 2;
    print(name + " | " + name.runtimeType.toString());
}
--------------------------
// >> Error: A value of type 'String' can't be returned from a function with return type 'int'.
```

<br>

## Dynamic Variables  

변수의 값을 update 할 때에 데이터타입이 변경되어도 이를 허용하는 변수가 있는데, 이를 바로 Dynamic 타입 변수라고 한다.  
`dynamic 변수명;` 혹은 `var 변수명;` 형식으로 선언한 변수인데, 아래 예시로 살펴보도록 하겠다.  

```dart
void main() {
    dynamic name;
    name = 'some name';
    name = 2;
    print(name.toString() + ' | ' + name.runtimeType.toString());
}
--------------------------
// >> 2 | int
```

이번에는 변수 값의 데이터타입이 String에서 int로 변경됨을 볼 수 있다.  
이는 변수 선언시에 `dynamic name;` 으로 변수를 Dynamic Type으로 선언해주었기 때문에 가능한 것이다.  

![Alt text](image.png)

이렇게 Dynamic 타입으로 변수를 선언하는 것은 권장되지는 않는 방법이나, 때에 따라서 불가피하게 사용해야 할 때도 있으므로 유용하게 사용하자.  
하지만 이상적으로는 사용이 권장되지 않으며, 또한 데이터타입을 명시할 때보다 사용할 수 있는 변수의 Attribute가 적으니 되도록이면 피하자!  

|선언 방법|데이터타입|
|---|---|
|dynamic name;<br>name='some name';|dynamic|
|dynamic name='some name';|dynamic|
|var name;<br>name='some name';|dynamic|
|var name='some name';|String|

<br>

## Nullable Variables    

Dart에서는 값이 null 일 수 있는 변수를 선언할 수 있다. 처음부터 있었던 것은 아니고, 몇 개의 버전이 업데이트 되면서 생겨났다.  
기존 코드에서는 변수가 null 값을 참조해버리면 대부분의 경우 null 관련 오류로 프로그램의 흐름이 멈춰버린다.(런타임 에러)  

먼저 일반적인 방식으로 선언한 변수에 null 값을 넣어주는 간단한 코드를 예시로 보자.  

```dart
void main() {
  String name = null;
  print(name.toString() + ' | ' + name.runtimeType.toString());
}
--------------------------
// >> Unhandled exception:
// >> type 'Null' is not a subtype of type 'String'
```

Null 타입은 String 타입의 변수에 할당될 수 없다는 오류가 발생한다.  
변수 자체에 Null 타입이 들어오는 순간 코드의 실행이 멈추게 되는 것이다.  

하지만 프로그래밍에선 모든 경우에서 변수가 null이 아니라고 장담할 수 없는 경우가 많다.  
여기서 착안해 만들어진 것이 바로 nullable variables 즉, "Null 값일 수도 있는 변수" 이다.  

nullable 변수의 선언은 의외로 간단하다.  
변수명 앞에 선언하는 변수 타입에 "?"를 붙여주는 것이다.  

```dart
void main() {
  String? name;
  name = null;
  print(name.toString() + ' | ' + name.runtimeType.toString());
}
--------------------------
// >> null | Null
```

name 변수는 String 타입임에도 null 값이 들어오는 것을 막지 않는다.  
또한 이러한 Null Safety에서는 nullable로 선언된 변수를 사용하는 경우, 에디터에서 해당 변수가 null 일 수도 있으니 주의하라는 문구를 보여준다.  

![Alt text](image-1.png)  

추가로 dynamic 변수는 "?"를 붙이지 않더라도 null 값을 받을 수 있다. 참고하자.  

```dart
void main() {
  dynamic name;
  name = null;
  print(name.toString() + ' | ' + name.runtimeType.toString());
}
--------------------------
// >> null | Null
```

정리해보자면, Dart에서 변수는 기본적으로 non-nullable 이다.  
하지만 모든 경우에 변수의 값이 null이 아닐 것이라는 장담이 어려울 수도 있으므로, Dart에서는 nullable 변수를 지원한다.  
nullable 변수로 선언하기 위해서는 데이터타입의 뒤에 "?"를 붙여주거나, dynamic 변수로 선언하면 된다.  


## Final Variables  

Dart에서 변수는 기본적으로 그 안의 값이 변경될 수 있다.  
하지만 때에 따라서는 변경되면 안되는 값(변수)이 있을 수도 있다.  
이 때 사용하는 것이 Final Variables 즉, 최종 변수이다.  

먼저, 기본적인 방법으로 선언한 변수는 데이터타입이 일치하는 한 그 안의 값을 변경할 수 있다.  

```dart
void main() {
  String name = 'first name';
  name = 'second name';
  print(name.toString() + ' | ' + name.runtimeType.toString());
}
--------------------------
// >> second name | String
```

변수 안의 값을 변경할 수 없도록 하기 위해서는 변수를 final 타입으로 선언하는 것이다.  
이 때에는 값의 데이터타입을 Dart가 자동으로 파악하여 그에 해당하는 데이터타입으로 함께 선언해둔다.  
(일부러 변수명을 명시해둘 수도 있다.)

```dart
void main() {
  final name2 = 'first name';
  // 혹은 final String name2 = 'first name';
  name2 = 'second name';
  print(name.toString() + ' | ' + name.runtimeType.toString());
}
--------------------------
// >> Error: Can't assign to the final variable 'name2'.
```

final 로 선언한 변수의 값은 변경할 수 없으며(같은 데이터타입이라도), 변경하려고 하면 final variable은 변경할 수 없다는 오류 문구를 볼 수 있다.  
이는 javascript나 typescript의 const와 동일한 개념이다.  


## late  

변수 선언시 final 혹은 var 앞에 붙여줄 수 있는 수식어로, 초기 데이터 없이 변수를 선언할 수 있게 해주는 수식어이다.  
간단하게 말하면 "초기화 지연"이다.  
먼저, 사용법 부터 알아보도록 하자.  

```dart
void main() {
  late String a; // 변수를 먼저 선언
  // ~ Do Something ~
  a = 'some text';
}
```

"변수명을 어떠한 타입으로 나중에 사용하겠다" 라는 뜻으로 late 수식어를 더해 변수명을 선언할 수 있다.  
그런데 의문점. 꼭 late를 사용하지 않더라도 아래처럼 초기화 지연은 가능할텐데.. 왜 사용하는 것일까?  

```dart
void main() {
  String a;
  // ~ Do Something ~
  a = 'some text';
}
```

<b>late 수식어를 사용하는 이유</b>

(1) non-nullable 임을 명시해준다 : 가장 주요한 이유이다. late 

(2) 명시적 초기화 지연: late를 사용하면 변수를 선언할 때 초기화하지 않아도 되므로, 일부 변수는 필요한 시점에 초기화할 수 있습니다. 이는 특히 클래스의 생성자에서 초기화 불가능한 값을 필요로 할 때 유용합니다.  

(3) 가독성과 안정성 향상: 코드의 가독성을 높이고 안정성을 향상시키는 데 도움이 됩니다. 코드 리더가 해당 변수가 나중에 초기화될 것이라는 것을 명시적으로 알 수 있습니다.  

즉, "나중에 사용할 변수다" 라는 것을 명시적으로 보여주기 위함이다.  
지금 당장은 와닿지 않으나, 향후 class 를 이용할 경우 유용하다고 하니 일단 알아두자.  


(추가)  
당연하지만 주의할 점이 있다. late 수식어를 사용하든 사용하지 않든, 초기화하지 않은 변수는 다른 함수나 클래스에서 사용할 수 없다는 점.  
초기화 지연을 해준 변수는 반드시 사용 전 초기화를 해줘야 한다.  

```dart
void main() {
  // final a;
  late String a;
  String result = func01(a); // a 변수를 초기화(값 할당)하지 않아 오류가 나는 부분
  print(result.toString() + ' | ' + result.runtimeType.toString());
}

String func01(String some) {
  some = 'Hello World!';
  return some;
}
--------------------------
// >> Error: Late variable 'a' without initializer is definitely unassigned.
```


## Constant Variables  

const 는 상수를 말하는데, javascript 나 typescript의 const와는 다르다.  
(js와 ts에서의 const에 대응하는 개념은 final 이다.)  

Dart에서 const 는 'Compile Time Constant'를 의미하는데,  
이는 "컴파일 될 때에도 그 값을 유지하고 있는 변수" 라고 보면 될 것이다.  
아래 예시를 통해 알아보자.  

```dart
// 컴파일 후 변환되는 값을 보여주는 함수
String returnCompileResult(String text){
  result = // 대충 input 값이 compile 이후에 변경될 값을 보여주는 기능;
  return result
}

void main() {
  final String apiKey = 'SomeText';
  result = returnCompileResult(apiKey);
  print("(1) " + apiKey + " (2) " + result);
}
--------------------------
// >> (1) SomeText (2) [83, 111, 109, 101, 84, 101, 120, 116]
```

먼저, const가 아닌 변수를 이용하면 컴파일시 해당 변수의 값은 기계어에 맞게 번역기 된다.  
그러면 const 로 선언된 변수 값은 어떻게 되는지 살펴보자.

```dart
// 컴파일 후 변환되는 값을 보여주는 함수
String returnCompileResult(String text){
  result = // 대충 input 값이 compile 이후에 변경될 값을 보여주는 기능;
  return result
}

void main() {
  const String apiKey = 'SomeText';
  result = returnCompileResult(apiKey);
  print("(1) " + apiKey + " (2) " + result);
}
--------------------------
// >> (1) SomeText (2) SomeText
```

const로 선언된 값은 컴파일 할 때에도 동일한 값을 가지고 있다.  
즉 컴파일시의 "하드코딩"과 비슷한 느낌으로 이해하면 좋을 것 같다.  

이는 컴파일 후에도 즉, 애플리케이션 상에도 그 값이 그대로 유지되어야 하는 값을 선언하기 위해 사용된다.  


## 복습  

|변수 선언 방법|설명|
|---|---|
|String 변수명|String 타입의 값을 받는 변수 선업 방법.|
|int 변수명|int 타입의 값을 받는 변수 선언 방법.|
|var 변수명|변수타입을 특정하지 않는 변수 선언 방법<br>처음 변수에 할당하는 값의 데이터타입으로 변수의 데이터타입이 고정된다.<br>지역변수에 사용할 때 많이 사용한다.|
|dynamic 변수명|변수타입을 특정하지 않는 변수 선언 방법<br>할당되는 값의 데이터타입에 상관 없이 이후에도 데이터타입을 변경할 수 있다.|
|final 변수명|값을 재할당하지 못하는 '고정값'을 변수에 할당하는 변수 선언 방법|
|데이터타입? 변수명|null 값을 받을 수 있는 변수를 선언하는 방법|
|late 데이터타입 변수명|지연 초기화 변수 선언 방법|


## Reference  

노마드코더 var declaration : https://nomadcoders.co/dart-for-beginners/lectures/4094  
노마드코더 dynamic : https://nomadcoders.co/dart-for-beginners/lectures/4095  
노마드코더 nullable : https://nomadcoders.co/dart-for-beginners/lectures/4096  
노마드코더 final : https://nomadcoders.co/dart-for-beginners/lectures/4097  
노마드코더 late : https://nomadcoders.co/dart-for-beginners/lectures/4098  
노마드코더 const : https://nomadcoders.co/dart-for-beginners/lectures/4099  
late 수식어 사용의 이유 : https://lucky516.tistory.com/185  
late 수식어 사용의 이유 : https://velog.io/@teddyjune/late%EB%8A%94-%EC%99%9C-%EC%93%B0%EB%82%98  