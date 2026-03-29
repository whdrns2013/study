
## 좋아요 아이콘  

이번에 하려는 것은 좋아요 기능이다.  
웹툰 제목 옆에 하트 버튼을 달고, 사용자가 그 버튼을 클릭하면 이것을 기억해서 핸드폰 저장소에 정보를 담게끔 할 것이다.  

사용자가 다시 앱에 접속해도 저장된 정보를 토대로 좋아요를 누른 웹툰에는 좋아요가 그대로 표시되도록 하는 것이다.  

## 폰에 정보를 담기 : shared_preferences  

핸드폰에 정보를 담기 위해서는 Shared_preferences 라는 패키지를 이용한다.  

https://pub.dev/packages/shared_preferences  

이것을 이요하면 핸드폰 저장소에 데이터를 저장할 수 있다.  

### shared_preferences 의 작동 방식  

1. 핸드폰 저장소와 connection을 만든다.  

```dart
// Obtain shared preferences.
final SharedPreferences prefs = await SharedPreferences.getInstance();
```

2. 다양한 자료형을 저장할 수 있다.  

```dart
// Save an integer value to 'counter' key.
await prefs.setInt('counter', 10);
// Save an boolean value to 'repeat' key.
await prefs.setBool('repeat', true);
// Save an double value to 'decimal' key.
await prefs.setDouble('decimal', 1.5);
// Save an String value to 'action' key.
await prefs.setString('action', 'Start');
// Save an list of strings to 'items' key.
await prefs.setStringList('items', <String>['Earth', 'Moon', 'Sun']);
```

3. 가져올 때에는 getInt, getBool .. 과 같이 입력해주면 된다.  

```dart
// Try reading data from the 'counter' key. If it doesn't exist, returns null.
final int? counter = prefs.getInt('counter');
// Try reading data from the 'repeat' key. If it doesn't exist, returns null.
final bool? repeat = prefs.getBool('repeat');
// Try reading data from the 'decimal' key. If it doesn't exist, returns null.
final double? decimal = prefs.getDouble('decimal');
// Try reading data from the 'action' key. If it doesn't exist, returns null.
final String? action = prefs.getString('action');
// Try reading data from the 'items' key. If it doesn't exist, returns null.
final List<String>? items = prefs.getStringList('items');
```

4. 삭제할 때에는 remove 메서드를 이용한다.  

```dart
// Remove data for the 'counter' key.
await prefs.remove('counter');
```


## 좋아요 기능 기획  

1. 좋아요를 누른 웹툰 id를 담은 리스트 자료형을 운영하고 저장할 것이다.  
2. 홈에서 웹툰을 클릭해 webtoon_detail로 이동할 때에 이 자료형을 불러와 좋아요 여부를 표시한다.  
3. 사용자가 좋아요를 누를 경우 값을 더한다.  
4. 사용자가 좋아요를 다시 누를 경우(취소할 경우) 리스트에서 값을 뺀다.  

## 구현  

먼저 이것들이 이뤄질 detail_screen.dart에서 작업을 해준다.  

먼저 shared preferences 클래스를 이용해줘야 하기 때문에, detail screen 에 진입했을 때 Instance 를 만들도록 한다.  

```dart
// detail_screen.dart
class _DetailScreenState extends State<DetailScreen> {
  late Future<WebtoonDetailModel> webtoon;
  late Future<List<WebtoonEpisodeModel>> episodes;
  late SharedPreferences prefs; // 좋아요 저장 property

  Future initPrefs() async { // SharedPreferences 생성 메서드
    prefs = await SharedPreferences.getInstance();  // 인스턴스 생성
  }

  @override
  void initState() {
    super.initState();
    webtoon = ApiService.getToonById(widget.id);
    episodes = ApiService.getLatestEpisodesById(widget.id);
    initPrefs(); // init을 할 때 prefs 를 생성해줌
  }
...
```

이렇게 하면 핸드폰 저장소와의 connection이 생긴 것이다.  

사용자 핸드폰 저장소 내부를 확인해서 좋아요 정보를 담은 StringList가 있는지 확인하고 불러오도록 한다. 좀 더 자세히 말하자면 아래와 같다.  

1. 핸드폰 저장소 내부를 확인해서 좋아요 정보를 담은 StringList가 있는지 확인한다.  
2. 해당 StringList가 있으면 불러오고, 특정 액션을 취한다.  
3. 해당 StringList가 없다면(처음 접속이라면) 리스트를 생성하고 저장한다.  

```dart
// detail_screen.dart
class _DetailScreenState extends State<DetailScreen> {
  late Future<WebtoonDetailModel> webtoon;
  late Future<List<WebtoonEpisodeModel>> episodes;
  late SharedPreferences prefs; // 좋아요 저장

  Future initPrefs() async {
    prefs = await SharedPreferences.getInstance(); // 인스턴스 생성
    final likedTonns = prefs.getStringList('likedToons'); // likedToons 라는 이름의 StringList를 불러옴
    if (likedTonns != null) { // likedToons라는 이름의 StringList가 핸드폰 저장소에 있다면 특정 액션을 취한다 (현재는 비워놓음)
      
    } else { // likedToons라는 이름의 StringList가 핸드폰 저장소에 없다면
      prefs.setStringList("likedToons", []);  // likedToons라는 이름의 StringList를 핸드폰 저장소에 생성한다.  
    }
  }
```

여기까지 이해가 됐다면 이어서 다음 단계를 진행한다.  

큰 틀은 만들었으니, 이제 likedToons 가 저장소에 존재할 경우의 액션을 지정해야 한다. 아래와 같다.  

```dart
// detail_screen.dart
class _DetailScreenState extends State<DetailScreen> {
  late Future<WebtoonDetailModel> webtoon;
  late Future<List<WebtoonEpisodeModel>> episodes;
  late SharedPreferences prefs; // 좋아요 저장
  bool isLiked = false; // 해당 웹툰에 대한 좋아요 여부 상태 state

  Future initPrefs() async {
    prefs = await SharedPreferences.getInstance(); // 인스턴스 생성
    final likedTonns =
        prefs.getStringList('likedToons'); // likedToons 라는 이름의 StringList를 불러옴
    if (likedTonns != null) {
      // likedToons라는 이름의 StringList가 핸드폰 저장소에 있다면
      if (likedTonns.contains(widget.id) == true) {
        // 좋아요 리스트에 현재 웹툰의 아이디가 저장되어있다면
        isLiked = true; // isLiked 상태를 true로 바꾼다.
        setState(() {});  // 상태값을 저장한다.
      }
    } else {
      // likedToons라는 이름의 StringList가 핸드폰 저장소에 없다면
      prefs.setStringList(
          "likedToons", []); // likedToons라는 이름의 StringList를 핸드폰 저장소에 생성한다.
    }
  }
```

그리고 AppBar에 하트 이모티콘을 넣어, isLiked가 true일 경우 채워진 하트, false일 경우 빈 하트가 되도록 해준다.  

```dart
// detail_screen.dart
@override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 1,
        title: Text(
          widget.title,
          style: TextStyle(
            fontSize: 26,
            fontWeight: FontWeight.w600,
          ),
        ),
        actions: [
          IconButton(
            onPressed: () {}, // 좋아요 아이콘을 누를 때의 메서드
            icon: Icon(
                // isLiked 여부에 따라 하트를 채우거나 채우지 않거나
              isLiked ? Icons.favorite_rounded : Icons.favorite_outline_rounded,
            ),
          )
        ],
```

그리고 좋아요 아이콘을 누를 때의 메서드를 지정해주자.  
메서드는 isLiked 가 false일 경우 누르면 likedToons StringList에 해당 웹툰의 id를 넣어주고,  
반대로 isLiked 가 true일 경우 누르면 likedToons StringList에서 해당 웹툰 id를 제거하게끔 해주면 된다.  

```dart
// detail_screen.dart

// 메서드를 추가한다.  
onHeartTap() async {
final likedToons =
    prefs.getStringList('likedToons'); // likedToons 라는 이름의 StringList를 불러옴
if (likedToons != null) {
    // likedToon 가 존재할 경우에 (위에서 Init 했으니 아마 존재할 것이나, 혹시 몰라)
    if (isLiked) {
    // 좋아요가 눌려있다면
    likedToons.remove(widget.id); // 좋아요 리스트에서 제거
    } else {
    // 좋아요가 눌려있지 않다면
    likedToons.add(widget.id); // 좋아요 리스트에 추가
    }
    await prefs.setStringList(
        "likedToons", likedToons); // 핸드폰 저장소에 likedToons를 저장함
    setState(() {
    isLiked = !isLiked;  // 기존의 isLiked와 반대의 상태값을 저장해준다. (탭함 = 현재 상태와 반대가 됨)
    });
}
}

// 아이콘 action에 만든 메서드를 지정해준다.  
@override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 1,
        title: Text(
          widget.title,
          style: TextStyle(
            fontSize: 26,
            fontWeight: FontWeight.w600,
          ),
        ),
        actions: [
          IconButton(
            onPressed: onHeartTap, // 좋아요 아이콘을 누를 때의 메서드
            icon: Icon(
              isLiked ? Icons.favorite_rounded : Icons.favorite_outline_rounded,
            ),
          )
        ],
```


## 다른 방법  

꼭 좋아요를 리스트 형태로 저장할 필요는 없다.  
예를 들어 pref.setBool 즉 bool 형태로 저장하면 아래와 같이 구성할 수도 있다.  

```dart
prefs.setBool('웹툰id', bool);
```