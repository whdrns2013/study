class Player2 {

    late String name;
    late int level;
    late String job;

    Player(String name, int level, String job){
        this.name = name;
        this.level = level;
        this.job = job;
    }

    void introduction() {
        print('Hi. my name is $name. level is $level and my job is $job');
    }
}

class Player {

  String name;
  int level;
  String job;

  Player(this.name, this.level, this.job);

  void introduction() {print('Hi. my name is $name. level is $level and my job is $job');}

}


void main() {
    Player player01 = Player('jongya', 10, 'magician');
    print(player01.name);
    player01.introduction();
}