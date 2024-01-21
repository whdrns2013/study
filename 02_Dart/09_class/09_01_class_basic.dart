

class Player{
  String name = 'jongya';
  int xp = 1500;
  final String job = 'magician';

  void sayHello() {
    var name = 'name in method';
    print('Hello, my name is ${this.name}');
    print('Hello, my name is $name');
  }

  void sayHello2() {
    print('Hello, my name is ${this.name}');
    print('Hello, my name is $name');
  }

  // class ClassInClass{
  //   var name = 'I want make new one in existed class';
  // }
}


class newPlayer {
    String name = 'default name';  // 데이터타입을 명시해주는 것이 권장됨
    int level = 0;                 // 데이터타입을 명시해주는 것이 권장됨
    final job = 'magician';        // 값을 변경할 수 없게 final로 선언

    void introduction() {
        var name = 'name in method';
        print('Hi. my name is $name');
        print('Hi, my name is ${this.name}');
    }
}


void main() {
  
  // class 객체를 생성하는 방법
  var player = Player();

  // property 를 출력할 수 있고
  print(player.name);

  // class 객체 안의 property를 수정할 수도 있다.
  player.name = 'changed name';
  print(player.name);

  // 다른 변수명으로 새롭게 만들어진 class 객체는 기존과 서로 다름
  Player player2 = Player();
  print(player2.name);

  // final로 선언된 property는 수정할 수 없다.
  // player.job = 'changed job';

  // this.name 은 class 안의 변수를 가리킨다.
  player.sayHello();

  // class 안에 겹치는 변수가 없다면 $name은 ${this.name} 과 같다.
  player.sayHello2();

  newPlayer player03 = newPlayer();
  player03.introduction();
  player03.name = 'jongya';
  player03.introduction();
}