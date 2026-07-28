



class Something{
  String name;
  Something({required String this.name});
}

void main(){
  Something a = Something(name: 'something new');
  print(a.name);
}