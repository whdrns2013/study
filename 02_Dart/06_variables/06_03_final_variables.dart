

void main() {

  String name = 'first name';
  name = 'second name';
  print(name.toString() + ' | ' + name.runtimeType.toString());

  final name2 = 'first name';
  // name2 = 'second name'; // final 변수를 다른 값으로 변경하려고 시도
  print(name.toString() + ' | ' + name.runtimeType.toString());
}