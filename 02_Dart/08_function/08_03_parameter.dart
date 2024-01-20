String introduction01(
  String name,
  int level,
  String job) {
  return "Hi $name. your level is $level, and you are $job";
}

String introduction02(
    {String name = 'default name',
    int level = 1,
    String job = 'unemployed'}) {
  return "Hi $name. your level is $level, and you are $job";
}

String introduction03(
    {required name,
    required level,
    required job}) {
  return "Hi $name. your level is $level, and you are $job";
}

String introduction04(
    {String name = 'default name',
    required level,
    required job}) {
  return "Hi $name. your level is $level, and you are $job";
}

// void main() => print(introduction01('jongya', 10, 'magician'));
// void main() => print(introduction02(name: 'jongya', level: 10, job: 'magician'));
// void main() => print(introduction03(name: 'jongya', level: 10, job: 'magician'));
// void main() => print(introduction02(level: 10, job: 'magician', name: 'jongya'));
// void main() => print(introduction02(level: 10));
void main() => print(introduction04(level: 10, job: 'magician'));