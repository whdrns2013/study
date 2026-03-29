// class Player {
//   String name;
//   int level;
//   String job;

//   Player({this.name = 'default name',
//           this.level = 0,
//           this.job = 'non'});
          
//   void introduction() {
//     print('Hi. my name is $name. level is $level and my job is $job');
//     }
// }

class Player {
  String name;
  int level;
  String job;

  Player({required this.name,
          required this.level,
          required this.job});
          
  void introduction() {
    print('Hi. my name is $name. level is $level and my job is $job');
    }
}

void main() {
  // Player player01 = Player(level: 50);
  Player player01 = Player(name:'jongya', level:10, job:'magician');
  player01.introduction();
}
