


String makeUpperName01(String? name) {
  if (name != null) {
    return name.toUpperCase();
  }
  return 'Null';
}

String makeUpperName02(String? name) =>
    name != null ? name.toUpperCase() : 'null';


// QQ Operator  ::  Question Question Operator
String makeUpperName03(String? name) => name?.toUpperCase() ?? 'Null';

// String makeUpperName04(String? name) => name.toUpperCase() ?? 'Null';

// QQ assignment
// Strring


void main() {
  print(makeUpperName01('jongya'));
  print(makeUpperName02('jongya'));
  print(makeUpperName03('jongya'));
}
