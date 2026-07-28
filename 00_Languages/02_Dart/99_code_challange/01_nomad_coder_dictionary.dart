// Challenge goals:
// Using everything we learned, make a Dictionary class with the following methods:

// add: 단어를 추가함.
// get: 단어의 정의를 리턴함.
// delete: 단어를 삭제함.
// update: 단어를 업데이트 함.
// showAll: 사전 단어를 모두 보여줌.
// count: 사전 단어들의 총 갯수를 리턴함.
// upsert 단어를 업데이트 함. 존재하지 않을시. 이를 추가함. (update + insert = upsert)
// exists: 해당 단어가 사전에 존재하는지 여부를 알려줌.
// bulkAdd: 다음과 같은 방식으로. 여러개의 단어를 한번에 추가할 수 있게 해줌. [{"term":"김치", "definition":"대박이네~"}, {"term":"아파트", "definition":"비싸네~"}]
// bulkDelete: 다음과 같은 방식으로. 여러개의 단어를 한번에 삭제할 수 있게 해줌. ["김치", "아파트"]

// Requirements:
// Use class
// Use typedefs
// Use List
// Use Map

typedef DictTemplate = Map<String, String>;
typedef BulkAddTemplate = List<DictTemplate>;

class Dictionary {
  DictTemplate dictionary = {};

  // add 단어 추가
  void add(DictTemplate input) => dictionary.addAll(input);

  // get 단어 정의 리턴
  String? get(String input) => dictionary[input];

  // delete 삭제
  void delete(String input) => dictionary.remove(input);

  // update 단어 업데이트
  void update(DictTemplate input) =>
      dictionary[input.keys.first] = input.values.first;

  // showAll 사전 단어를 모두 보여줌
  Iterable<String> showAll() {
    print(dictionary.keys);
    return dictionary.keys;
  }

  // count 사전 단어들 총 갯수를 리턴
  int count() => dictionary.length;

  // upsert 단어를 업데이트하고, 존재하지 않는다면 추가함
  void upsert(DictTemplate input) =>
      dictionary[input.keys.first] = input.values.first;

  // exists 해당 단어가 사전에 존재하는지 여부 알려줌
  bool exists(String input) {
    print(dictionary.containsKey(input));
    return dictionary.containsKey(input);
  }

  // bulkAdd 여러 개의 단어를 한 번에 추가
  void bulkAdd(BulkAddTemplate input) {
    for (DictTemplate dic in input) {
      dictionary.addAll(dic);
    }
  }

  // bulkDelete 여러 개의 단어를 한 번에 삭제
  void builkDelete(List<String> input) {
    for (String word in input) {
      dictionary.remove(word);
    }
  }

  // 추가 : 테스트 편하려고 추가함
  DictTemplate showAllPlus() {
    print(dictionary);
    return dictionary;
  }
}

void main() {
  Dictionary dictionary = Dictionary();

  dictionary.add({"first word": "definition of first word"});
  dictionary.add({"test word": "the definition of test word is me"});
  dictionary.showAllPlus();

  print(dictionary.get("test word"));

  dictionary.delete("test word");
  dictionary.showAllPlus();

  dictionary.update({"first word": "changed definition"});
  dictionary.showAllPlus();

  dictionary.showAll();

  print(dictionary.count());

  dictionary.upsert({"first word": "change definition twice"});
  dictionary.upsert({"new word": "the definition of new word"});
  dictionary.showAllPlus();

  dictionary.exists("first word");
  dictionary.exists("second word");

  dictionary.bulkAdd([
    {"head": "we can think because"},
    {"hand": "we can type because"}
  ]);
  dictionary.showAllPlus();

  dictionary.builkDelete(["first word", "new word"]);
  dictionary.showAllPlus();
}
