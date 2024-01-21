


class Player{
  String name, job;
  int level;

  Player({required this.name, required this.job, required this.level});
  void introduction(){print('my name is $name, $level level, and $job');}
}

void main() {

  Player player01 = Player(name:'jongya', level:10, job:'magician');
  player01.name = 'changed name';
  player01.level = 15;
  player01.job = 'thief';
  player01.introduction();

  Player player02 = Player(name:'jongya', level:10, job:'magician')
  ..name = 'changed name'
  ..level = 15
  ..job = 'thief';
  player02.introduction();

  Player player = Player(name: 'default', job: 'non', level: 1);

  Player potato = player
  ..name = 'potato'
  ..level = 0
  ..job = 'potato'
  ..introduction();
}