
## Scaffold  

scaffold는 원래 공사장에서 쓰이는 "비계" 를 의미한다.  
비계는 건설현장에서 쓰이는 가시설물 등으로, 아래와 같이 생겼다.  

![Alt text](image-2.png)

즉 애플리케이션을 하나의 건축물이라고 예를 들었을 때, 이 scaffold 를 통해 애플리케이션 UI 의 틀을 쉽게 잡아줄 수 있다.  


## home

```dart
      home: Scaffold(
        backgroundColor: Colors.black,  // 앱의 배경 색상
        appBar: AppBar(                 // AppBar : 네비게이션 바
          title: Text("Hi!"),
        ),
```





## body  

### Column  

화면에서 "열"을 의미하는 것으로, children 이라는 List 형태의 property를 가진다.  

이 list 안에는 Row 라는 것을 넣을 수도 있고, Column 처럼 children 이라는 List 형태의 property를 가질 수 있다.  




### Row  

화면에서 "행"을 의미하는 것으로, children 이라는 List 형태의 property를 가진다.  

- MainAxisAlignment : 수평 방향 정렬  
- CrossAxisAlignment : 수직 방향 정렬  


### Padding  

children 을 감싸고 있는 내부 여백을 가지고 있는 큰 상자라고 보면 된다. 내용물을 여백을 주고 화면의 가장자리로부터 띄우는 역할을 한다.  

```dart

Padding(padding: EdgeInsetx.all(40),
child: 내용물)

```

padding: 에는 EdgeInsets 가 값으로 들어갈 수 있으며 EdgeInsets 는 아래와 같이 사용한다.  


-- EdgeInsets.all : 상하좌우에 모두 동일한 여백을 줌  
-- EdgeInsets.only : 상하좌우 중 한 군데에 여백을 줌  
--- EdgeInsets.only(t,값) : 위쪽에 여백을 줌  
--- EdgeInsets.only(b,값) : 아래쪽에 여백을 줌  
--- EdgeInsets.only(l,값) : 왼쪽에 여백을 줌  
--- EdgeInsets.only(r,값) : 오른쪽에 여백을 줌  
-- EdgeInsets.symmetric() : 수직과 수평 padding  
--- EdgeInsets.symmetric(horizontal : 수평 padding 값, vertical : 수직 padding 값)  