
void main() {
  dynamic result = func01();
  print(result.toString() + ' | ' + result.runtimeType.toString());
}

// late 수식 변수에 null 값 넣어보기
dynamic func01(){
  late final a;
  a = null;
  return a;
}

// late가 아닌 경우 변수에 null 값 넣기
dynamic func02() {
  final a;
  a = null;
  return a;
}

// 초기화 전에는 사용하지 못한다.
String func03(String some) {
  some = 'Hello World!';
  return some;
}
