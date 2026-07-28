



// void : 반환할 값이 없음
void func01(String input) {
  String someText = "Hello $input";
  print(someText);
}

// String : 반환할 값이 문자열
String func02(String input) {
  return "Hello $input";
}

// int : 반환할 값이 정수형임
int plus(int a, int b){
  int result = a + b;
  return result;
}

// main - void
// void main() {
//   func01("jongya");
//   print(func02("jongya"));
//   print(plus(1, 3));
// }

var name = "jongya";

// main - declaration return type
String main(){
  // String result = func02(name);
  return func02(name);
}
