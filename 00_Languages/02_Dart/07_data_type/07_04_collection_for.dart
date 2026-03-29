

void main() {
  print(func01());
  print(func02());
}



List<String> func01() {
  var newMenues = ['Cart', 'HotDeal'];
  // 원래 메뉴에 새로운 메뉴 추가. 별까지!
  var navBar = ['Home', 'Dashboard', 'MyPage', 'Admin Setting', for(var menu in newMenues) '⭐️$menu'];
  return navBar;
}


List<int> func02() {
  // 1 ~ 20 까지 홀수를 구하기 
  var numberRange = Iterable<int>.generate(20, (index) => index +1);
  List<int> oddNumber = [ for(int number in numberRange) if (number % 2 != 0) number ];
  return oddNumber;
}
