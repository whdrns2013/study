void main() {
  // Map<Srting, Object>
  // declaration with var
  var player = {
    'name': 'player01',
    'level': 20,
    'job': 'magician',
    'superUser': false,
  };

  // declaration 'Map'
  Map<String, String> keyValue = {'key': 'value', 'name': 'some name'};

  // can input any object in key or value
  Map<List<String>, String> auth = {
    ['Home', 'DashBoard']: 'guest',
    ['Home', 'AdminPage']: 'admin'
  };

  Map<String, List<int>> nums = {
    'underFive': [1, 2, 3, 4],
    'underTen': [5, 6, 7, 8, 9]
  };

  // Map<String, Object>
  var dragon = {
    'first': 'dragon',
    'second': 100,
    'third': [10, 20, 30],
    'real': true,
  };

  // Methods
  Map<int, String> someMap = {1: 'first', 2: 'second', 3: 'third'};

  // is it Empty?
  print(someMap.isNotEmpty);
  print(someMap.isEmpty);

  // contains
  print(someMap.containsKey(2));
  print(someMap.containsValue('fifth'));

  // get keys or values
  print(someMap.keys);
  print(someMap.values);

  // addAll :
  someMap.addAll({1: "change first", 4: "four"});
  print(someMap);
  // addEntries
  // someMap.addEntries({1 : "changed?? first", 4 : "four"}.entries);
  // print(someMap);

  // remove and clear
  someMap.remove(2);
  print(someMap);
  someMap.clear();
  print(someMap);

  Map<String, String> map1 = {"key1": "value1", "key2": "value2"};
  map1['key1'] = 'changed value';
  print(map1);
}
