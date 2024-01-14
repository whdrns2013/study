import 'dart:convert';


void main() {
  final String a;
  a = "SomeText";

  List<int> utf8Bytes = utf8.encode(a);
  print(utf8Bytes);
}