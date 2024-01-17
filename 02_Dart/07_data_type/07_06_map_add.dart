

void main() {
  Map<int, String> someMap = {1:'first', 2:'second', 3:'third'};
  Map<int, String> addMap = {1:'firstChange', 4:'four'};
  print(func01(someMap, addMap));
  func02(someMap, addMap);
}

Map<int, String> func01(var map1, var map2){
  map1.addAll(map2);
  return map1;
}

void func02(var map1, var map2){
  print("== print map ==");
  print(map1);
  
  print(map1);
}