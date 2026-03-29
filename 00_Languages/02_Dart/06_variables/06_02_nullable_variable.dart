

void main() {
  dynamic name;
  name = var05();
  print(name.toString() + " | " + name.runtimeType.toString());
}

// non-nullable = null
String var01(){
  var vari = null;
  return vari;
}

// nullable = null
String? var02(){
  var vari = null;
  return vari;
}

// nullable = String
String? var03(){
  var vari = 'some vari';
  return vari;
}

// dynamic = null
dynamic var04() {
  dynamic vari;
  vari = null;
  return vari;
}

// nullable with ?. Attribute
String? var05() {
  String? vari;
  vari = null;
  vari?.isNotEmpty;
  print(vari?.isEmpty);
  return vari?.isNotEmpty.toString();
}