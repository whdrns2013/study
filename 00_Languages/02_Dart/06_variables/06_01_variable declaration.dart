
void main() {
  var result = var06();
  print(result.toString() + " | " + result.runtimeType.toString());
}


// 01 변수 선언
String var01() {
  var name = 'some name';
  return name;
}


// 02 변수 값 update (동일 데이터 타입)
String var02() {
  var name = 'first name';
  name = 'second name';
  return name;
}


// 03 변수 값 update (다른 데이터 타입)
int var03() {
  var name = 'first name';
  // int name = 2;
  int number = 2;
  return number;
}

int var04() {
  dynamic name;
  name = 'some name';
  name = 2;
  return name;
}

int var05() {
  dynamic name = 'some name';
  name = 2;
  return name;
}

int var06() {
  var name;
  name = 'some name';
  name = 2;
  return name;
}
