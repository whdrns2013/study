

## dart 의 기본적인 데이터타입  

|데이터타입|설명|
|---|---|
|String|문자열 데이터타입을 의미한다.<br>선언시 값은 큰 따옴표 "" 혹은 작은 따옴표 '' 로 묶어준다.|
|bool|true or false 데이터타입을 의미한다.<br>값의 모든 문자를 소문자로 사용해야 한다.|
|int|정수형 데이터타입을 의미한다.|
|double|소수점 이하 자리를 커버할 수 있는 숫자형 데이터타입이다.|
|num|Dart 에는 num 이라는 데이터타입이 있다.<br>그리고 이 num 클래스는 int와 double의 부모 클래스이다.<br>다르게 말하면, num은 int형과 double형을 모두 커버할 수 있는 것이다.|

<br>

## Dart 의 자료형의 특징 : 모두 class 이다.  

여타 언어와 다르게 Dart의 데이터타입은 모두 class 이다.  

예를 들어 Java에서는 정수를 나타내는 데이터타입으로 int와 Integer가 있다.  
int는 데이터타입이고, Integer는 wrapper class인데, 이에 Integer는 필드를 포함하고 있다.  

Dart는 모든 데이터타입이 모두 class 이고, 이러한 특징 때문에 다양한 Attribute와 Method를 가질 수 있다.  

<br>

## List 데이터타입  

List 데이터타입은 동일한 데이터타입 값을 여러 개 배열로 가지고 있는 자료형을 의미한다.  
먼저 List 데이터타입의 변수 선언 방법부터 알아보자.  

```dart
// List 데이터타입 변수 선언 방법

void main() {
    var list1 = [1, 2, 3, 4];
    List<int> list2 = [1, 2, 3, 4];
}
```

List 데이터타입은 여러 가지 Attribute와 Method를 가지고 있다.  
그 중 주요한 몇 가지를 살펴보겠다.  

### List 데이터타입의 주요 Attribute와 Method  

(1) add : 값 추가  

```dart
void main() {
    // add : 리스트에 값을 추가한다.
    var list1 = [1, 2, 3, 4];
    list1.add(5);
    print(list1);

    // addAll: 리스트에 여러 값을 더한다.
    List<int> list2 = [5, 6, 7, 8];
    list2.addAll([7, 8, 9, 10]);
    print(list2);
}
====================
// >> [1, 2, 3, 4, 5]
// >> [5, 6, 7, 8, 7, 8, 9, 10]
```

(2) first, last : 첫 번째와 마지막 값 반환  

```dart
void main() {
    // first : 리스트의 첫 번째 값을 반환한다.  
    List<int> list3 = [9, 10, 11, 12];
    print(list3.first);

    // last : 리스트의 마지막 값을 반환한다.  
    List<int> list4 = [13, 14, 15, 16];
    print(list4.last);
}
====================
// >> 9
// >> 16
```

(3) isEmpty, isNotEmpty : 비어있는지 아닌지  

```dart
void main() {
    // isEmpty, isNotEmpty : 비어있는지 아닌지
    List<int> list5 = [17, 18, 19, 20];
    print(list5.isEmpty);
    print(list5.isNotEmpty);
}
====================
// >> false
// >> true
```

(4) clear : 리스트 안의 값 비우기  

```dart
void main() {
    // clear : 리스트 안을 모두 비운다.
    List<String> list6 = ["안녕", "이건", "리스트야"];
    print(list6);
    list6.clear();
    print(list6);
}
====================
// >> [안녕, 이건, 리스트야]
// >> []
```

(5) contains : 특정 값이 포함되어있는지  

```dart
void main() {
  // contains : 특정 값이 포함되어있는지 여부를 체크한다.  
    List<String> list7 = ["이", "값이", "포함되어 있나?"];
    print(list7.contains("이"));
    print(list7.contains("없는값"));
}
====================
// >> true
// >> false
```

(6) 리스트 인덱싱  

```dart
void main() {
    // 인덱싱 : list 에서 특정 순서에 있는 값을 반환받을 때
    List<String> list8 = ['첫 번째', '두 번째', '세 번째'];
    print(list8[1]);
    print(list8[list8.length -2]);
}
====================
// >> 두 번째
// >> 두 번째
```

(7) 리스트 슬라이싱  

```dart
void main() {
    // slicing
    List<int> list9 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    print(list9.sublist(2, 6));
}
====================
// >> [3, 4, 5, 6]
```

### Collection If  

collection if 는 "존재 할 수도, 안할 수도 있는 값" 을 리스트의 원소로 할당해두는 것을 의미한다.  
글로는 이해가 어려울 수 있으니, 예시로 이해해보도록 하자.  

```dart
void main() {
    bool giveMeFive = false;
    bool giveMeSix = true;

    List<int> list10 = [
        1,
        2,
        3,
        4,
        if(giveMeFive) 5,
        if(giveMeSix) 6,
        ];

    print(list10);
}
====================
// >> [1, 2, 3, 4, 6]
```

list10 변수 리스트에 할당되는 값들을 살펴보면 1, 2, 3, 4 와 같은 일반적인 정수형 값도 있지만,  
if로 시작하는 조건문을 원소값으로도 가지고 있는 것을 볼 수 있다.  

위에서부터 해석하면,  
(1) if(giveMeFive) 5: giveMeFive가 참이면 5를 원소로 갖는다.  
(2) if(giveMeSix) 6: giveMeSix가 참이면 6을 원소로 갖는다.  

그러므로 giveMeFive 가 false 이므로 5는 리스트에 추가되지 못하였고,  
조건문이 true인 6은 리스트의 값으로 추가될 수 있었다.  

이를 풀어 쓰자면 아래와 같다.  

```dart
void main() {
    bool giveMeFive = false;
    bool giveMeSix = true;
    List<int> list11 = [1, 2, 3, 4];
    if (giveMeFive == true) {list11.add(5);}
    if (giveMeSix == true) {list11.add(6);}
    print(list11);
}
====================
// >> [1, 2, 3, 4, 6]
```


## Collection For

collection for 는 list 자료형에 for 문을 추가해 원소를 추가하는 방법을 의미한다.  

아래 예시를 보자.  
(String Interpolation은 다음 챕터를 미리 보자)  

```dart
void main() {
  var newMenues = ['Cart', 'HotDeal'];
  // 원래 메뉴에 새로운 메뉴 추가. 별까지!
  var navBar = ['Home', 'Dashboard', 'MyPage', 'Admin Setting', for(menu in newMenuews) '⭐️$menu'];
  print(navBar);
}
==================
// >> [Home, Dashboard, MyPage, Admin Setting, ⭐️Cart, ⭐️HotDeal]
```

언제 쓰면 좋을까? 메뉴를 예로 들어 collection for, collection if 와 함께 써보자.

아래 예시는 회원의 권한별로 접근할 수 있는 메뉴를 출력하는 방법이다.  

```dart
void main() {
  // 1 ~ 20 까지 홀수를 구하기 
  var numberRange = Iterable<int>.generate(20, (index) => index +1);
  List<int> oddNumber = [ for(int number in numberRange) if (number % 2 != 0) number ];
  print(oddNumber);
}
==================
// >> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```


## String Interpolation  

String Interpolation  
문자열 보간  

![](./07_001.png)


String Interpolation 은 String 문자열에 변수를 넣어 유동적으로 사용하는 방법이다.  

방법은 간단한데, String 문자열의 표현법인 따옴표 안쪽에 달러($)표시를 쓰고, 그 다음에 비로 변수명을 적어주면 된다.  

아래 예시를 보자.  

```dart
void main(){
  String name = "Jongya";
  String introduction = "Hi, my name is $name. nice to meet you.";
  print(introduction);
}
// ====================
// >> Hi, my name is Jongya. nice to meet you.
```

수식 계산이 필요한 경우엔 달러($) 표시 다음 중괄호{}로 묶어주면 된다.  

```dart
void main(){
  String name = "Jongya";
  int age = 10;
  String introduction = "Hi, my name is $name. im ${age + 5} years old. nice to meet you.";
  print(introduction);
}
// ====================
// >> Hi, my name is Jongya. im 15 years old. nice to meet you.
```


## Reference  

노마드코더 - basic datatype : https://nomadcoders.co/dart-for-beginners/lectures/4101  
노마드코더 - lists : https://nomadcoders.co/dart-for-beginners/lectures/4102  
노마드코더 - String Interpolation : https://nomadcoders.co/dart-for-beginners/lectures/4103  
