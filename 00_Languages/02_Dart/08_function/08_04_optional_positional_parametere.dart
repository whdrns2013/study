


String introduction01(
  String name,
  int level,
  String job) {
  return "Hi $name. your level is $level, and you are $job";
  }

String introduction02(
  String job,
  [String? name='default name', int? level = 20]) {
  return "Hi $name. your level is $level, and you are $job";
  }

void main() => print(introduction02('thief'));