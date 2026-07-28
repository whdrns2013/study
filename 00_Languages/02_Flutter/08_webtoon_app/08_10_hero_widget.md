

## Hero Widget  

스크린(페이지)을 전환할 때 애니메이션을 넣어주는 위젯이다.  

```dart
Hero(
    tag: id,// 이 위젯의 식별 태그
    child: child,
)
```

webtoon_widget (홈의 웹툰 리스트를 보여주는 곳)의 Column을 Hero로 감싸주고 tag는 id로 준다.  

```dart
child: Column(
    children: [
        Hero(
        tag: id,
        child: Container(
            width: 250,
            ...
```

그리고 detailScreen으로 넘어가서 이곳의 썸네일을 보여주는 컨테이너를 동일하게 Hero 위젯으로 감싸준다.  

```dart
Hero(
    tag: id,
    child: Container(
        width: 250,
        clipBehavior: Clip.hardEdge, // 모서리를 튀어나오는 부분은 깔끔하게(hard) 제거
        decoration: BoxD
    ...
```

그러면 webtoon_widget에 있던 썸네일 이미지를 그대로 가져오는 애니메이션으로 새 스크린을 띄운다. 아래와 같이.  

![](/Feb-18-2024%2013-13-42.gif)

여기서 주목할 점은 바로 두 Hero 위젯 간 같은 Tag(id) 를 공유한다는 점이다.  

이 때 이 tag는 유니크해야 하며, Hero는 동일한 태그를 가진 두 가지를 연결하는 기능을 제공한다고 보면 되겠다.  