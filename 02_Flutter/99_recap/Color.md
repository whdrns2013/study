

## Colors

```dart

Colors.yellowAccent.shade700,

// Colors : 색상 family에 대한 클래스
// yellowAccent : 데이터타입. 색상 family이다. yellow color family
// shade : 음영의 강도.
```

```dart
class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.yellowAccent.shade700,
        appBar: AppBar(
          title: Text("Hi!"),
        ),),);}
}
```