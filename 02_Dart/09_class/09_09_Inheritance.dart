// enums
enum SuperPower { defenceMaster, infinityMana, pickPocket }

enum Job { Warrior, Magician, Theif, whiteHand }

// Parent Class : Player
class Player {
  String name; Job job; int level;

  Player({required this.name, required this.job, required this.level});

  void introduction() {
    print("i'm $name, the $job. and my level is $level");
  }
}

// Child Class : WhiteHand
class WhiteHand extends Player {
  WhiteHand({required String name, required Job job, required int level})
      : super(name: name, job: job, level: level);
}

// Child Class : Warrior
class Warrior extends Player {
  SuperPower superPower = SuperPower.defenceMaster;

  Warrior({required String name, required int level})
      : super(name: name, job: Job.Warrior, level: level);
  // super Constructor는 초기화의 가장 마지막에만 명시할 수 있다.

  void introduction() {
    super.introduction(); // 부모 클래스의 함수를 그대로 가져와 사용할 수 있다.
  }
}

// Child Class : Magician
class Magician extends Player {

  Magician({required String name, required int level})
      : super(name: name, job: Job.Magician, level: level);

  @override // 부모 쿨래스의 메서드와 동일한 이름의 메서드를 사용할 때에는 @override 어노테이션 사용을 권장한다.
  void introduction() {
    super.introduction();
    print("HaHa, i'm the best ${this.job} in this World!");
    print("my name is ${this.name}, and ${this.level} level");
  }
}

// Child Class : Theif
class Theif extends Player {
  String somethingNew = 'something new';  // 부모 class에는 없던 property도 추가할 수 있다.

  Theif({required String name, required int level})
      : super(name: name, job: Job.Theif, level: level);

  // 하지만 동일한 이름의 메서드를 사용할 때 어노테이션을 사용하지 않아도 컴파일시 자동으로 오버라이드로 인식은 된다.
  void introduction() {
    print("HeHe... what's wrong with you?");
    print("i do not tell you any $somethingNew");
  }
}

// Main
void main() {

  WhiteHand player00 = WhiteHand(name: 'player00', job: Job.whiteHand, level: 1);
  player00.introduction();
  print(player00.name);

  Warrior player01 = Warrior(name: "player01", level: 10);
  player01.introduction();

  Magician player02 = Magician(name: "player02", level: 15);
  player02.introduction();

  Theif player03 = Theif(name: 'player03', level: 50);
  player03.introduction();
}
