## Why Dart?  

![Alt text](01_001.png)

## Portable and fast on adll platforms  

- 다트는 두 개의 컴파일러를 가지고 있음.  
- 다트 웹과 다트 네이티브임  
- 다트 웹 : dart로 작성한 코드를 javascript로 변환하는 컴파일러  
- 다트 네이티브 : dart로 작성한 코드를 여러 CPU의 아키텍처에 맞게 변환하는 컴파일러  
예) ARM32에 맞게, 혹은 대부분 모바일 기기에 맞는 ARM64에 맞게  

=> 즉, 다트만으로 거의 모든 기기에서 작동하는 애플리케이션을 만들 수가 있음  

![Alt text](01_002.png)


## JIT 컴파일과 AOT 컴파일을 모두 지원  

다트는 JIT, AOT 컴파일을 모두 지원한다.  
개발 당시에는 Dart VM을 이용해 JIT 컴파일 방식을 채택하여 디버깅 등 편리한 개발 환경을 제공한다.  
그리고 배포시에는 AOT 컴파일 방식을 사용하여 기계에서 빠른 작동시간이라는 장점을 함께 취한다.  
따라서 Dart는 JIT 와 AOT 컴파일의 장점을 각각 취해 개발환경과 실제 작동환경에서 모두 좋은 경험을 얻을 수 있게 한다.  

(참고) JIT 컴파일과 AOT 컴파일  
https://whdrns2013.github.io/computerscience/20240113_004_jit_aot_compile/  


## Null Safety  

또한 Dart에서는 Null Safety 라는 기능을 지원하는데,  
변수를 생성할 때 값이 null 일 수 있는지 여부를 명시적으로 지정할 수 있는 기능이다.  
이 기능이 있음으로써 코드에서 발생할 수 있는 Null 관련 오류를 사전에 차단할 수 있다.  

```dart
// 값이 Null이 아닌 변수의 선언 (기본)
String nonNullableString = "Hello, Dart";    // -> 정상 처리
String nonBullableString = null;             // -> 비정상 오류

// 값이 Null일 수 있는 변수의 선언 (Null Safety)
String? nullableString = "Hello, Dart";      // -> 정상 처리
String? nullableString = null;               // -> 정상 처리
```

## Flutter 에서 Dart를 선택한 이유  

Dart와 Flutter는 모두 구글에서 개발했다. 이는 Flutter의 성능과 편의성 향상을 위해 Dart의 문법을 수정할 수도 있다는 것이다.  
Flutter는 Dart의 문법적 장점 외로도 이러한 점 때문에 Dart를 개발 언어로 선택했을 것이다.  

예를 들어 Flask 의 성능을 위해 Python의 문법을 변경할 수는 없다. 하지만 Flutter와 Dart는 가능한 것이다.  

실제 예시로, Dart는 처음 개발 당시에는 AOT 컴파일 방식이 불가능했으나, Flutter에서 AOT 컴파일을 필요로 하자 Dart는 해당 기능이 가능하게끔 자신을 개선하였다.  

관련 FAQ 원문  

```plaintext
In addition, we have the opportunity to work closely with the Dart community, which is actively investing resources in improving Dart for use in Flutter. For example, when we adopted Dart, the language didn’t have an ahead-of-time toolchain for producing native binaries, which is instrumental in achieving predictable, high performance, but now the language does because the Dart team built it for Flutter. Similarly, the Dart VM has previously been optimized for throughput but the team is now optimizing the VM for latency, which is more important for Flutter’s workload.
```


## Reference  

노마드코더 why dart : https://nomadcoders.co/dart-for-beginners/lectures/4091  
Dart Docs - overview : https://dart.dev/overview  
Dart Docs - null safety : https://dart.dev/null-safety  
Flutter Docs : https://docs.flutter.dev/resources/faq  