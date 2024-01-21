

// 추상화 클래스인 Car 클래스
abstract class Car{
  late int fuel;
  late String type;

  void start();
  void stop();
}

// Car 를 상속받은 Damas 클래스
class Damas extends Car{
  void start() { print('start this car'); }
  void stop() { print('stop this car'); }
  void somethingNew() { print("it's something new!!");}
}

// Car 를 상속받은 Rambo 클래스
class Rambo extends Car{

  String engine;
  String type;

  Rambo({required this.engine, required this.type});

  void start() { print("It's $type. Boorng Boorng~"); }
  void stop() { print('Kiiiick~'); }
}

void main() {

  Damas damas1 = Damas();
  damas1.start();
  damas1.stop();
  damas1.somethingNew();

  Rambo rambo1 = Rambo(engine: 'Turbo', type: 'Huracán');
  rambo1.start();
  rambo1.stop();
}
