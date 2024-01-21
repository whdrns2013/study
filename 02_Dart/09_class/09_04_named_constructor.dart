class Player {
  String name, job, skill;
  int level, str, inteli;

  Player(
      {this.name = 'default name',
      this.level = 0,
      this.job = 'non',
      this.str = 5,
      this.inteli = 5,
      this.skill = 'non'});

  Player.creatWarrior({required String name, required String skill})
      : this.name = name,
        this.level = 10,
        this.job = 'warrior',
        this.str = 25,
        this.inteli = 5,
        this.skill = skill;

  Player.createMagician({required String name, required String skill})
      : this.name = name,
        this.level = 10,
        this.job = 'magician',
        this.str = 5,
        this.inteli = 25,
        this.skill = skill;

  Player.createThief({required String name, required String skill})
      : this.name = name,
        this.level = 10,
        this.job = 'thief',
        this.str = 10,
        this.inteli = 10,
        this.skill = skill;

  void introduction() {
    print(this.name + "/" + this.job);
    print("level : " + this.level.toString() + "/ skill : " + this.skill);
  }
}

void main() {}
