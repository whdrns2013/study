

void main() {
  print(func01());
  print(func02());
}



String func01(){
  String name = "Jongya";
  String introduction = "Hi, my name is $name. nice to meet you.";
  return introduction;
}


String func02(){
  String name = "Jongya";
  int age = 10;
  String introduction = "Hi, my name is $name. im ${age + 5} years old. nice to meet you.";
  return introduction;
}