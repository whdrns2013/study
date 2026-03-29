

## Main Function  

Dart 로 작성한 프로그램의 EntryPoint 가 되는 코드파일.  
그 외로 작성한 Class나 Dart, 그 외의 파일들은 이 main Function을 시작점으로 호출될 것이다.  

다른 말로 하면, main Function이 없다면 Dart로 작성한 프로그램은 실행되지 않는다는 것이다.  
아래 예시를 통해 알아보자.  

먼저, main Function을 제대로 선언한 뒤 실행을 해보자.  

```dart
void main() {
    print('Hello World!');
}

// 실행시
>>> Hello WorLd!
>>> Exited.
```

그리고 main Function의 이름을 something으로 바꿔보면, 실행버튼이 사라져서 실행할 수 없는 것을 볼 수 있다.  

![Alt text](image.png)




