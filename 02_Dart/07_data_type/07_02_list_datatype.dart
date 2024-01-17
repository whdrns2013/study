void main() {
  // add : 리스트에 값을 추가한다.
  var list1 = [1, 2, 3, 4];
  list1.add(5);
  print(list1);

  // addAll: 리스트에 여러 값을 더한다.
  List<int> list2 = [5, 6, 7, 8];
  list2.addAll([7, 8, 9, 10]);
  print(list2);

  // first : 리스트의 첫 번째 값을 반환한다.
  List<int> list3 = [9, 10, 11, 12];
  print(list3.first);

  // last : 리스트의 마지막 값을 반환한다.
  List<int> list4 = [13, 14, 15, 16];
  print(list4.last);

  // isEmpty, isNotEmpty : 비어있는지 아닌지
  List<int> list5 = [17, 18, 19, 20];
  print(list5.isEmpty);
  print(list5.isNotEmpty);

  // clear : 리스트 안을 모두 비운다.
  List<String> list6 = ["안녕", "이건", "리스트야"];
  print(list6);
  list6.clear();
  print(list6);

  // contains : 특정 값이 포함되어있는지 여부를 체크한다.
  List<String> list7 = ["이", "값이", "포함되어 있나?"];
  print(list7.contains("이"));

  // list 에서 특정 순서에 있는 값을 반환받을 때
  List<String> list8 = ['첫 번째', '두 번째', '세 번째'];
  print(list8[1]);
  print(list8[list8.length - 2]);

  // slicing
  List<int> list9 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  print(list9.sublist(2, 6));

  // collection if
  bool giveMeFive = false;
  bool giveMeSix = true;
  List<int> list10 = [
    1,
    2,
    3,
    4,
    if(giveMeFive) 5,
    if(giveMeSix) 6,
  ];
  print(list10);

  // collection if 2
  List<int> list11 = [1, 2, 3, 4];
  if (giveMeFive == true) {list11.add(5);}
  if (giveMeSix == true) {list11.add(6);}
  print(list11);





}

