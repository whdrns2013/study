

void main() {
  String? name;
  name ??= 'jongya';
  print(name);
  
  name = null;
  name ??= 'another name';
  print(name);
}