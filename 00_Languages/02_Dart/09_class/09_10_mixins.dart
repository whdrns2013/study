mixin class Strong {
  final double strength = 10000;
}

mixin Speed {
  final double speed = 10000;
  void skillRunQuick() {
    print('run fast!');
  }
}

class Player with Strong, Speed {
  String name, job;
  Player({required String name, required String job})
      : this.name = name,
        this.job = job;
}

void main() {
  Player player01 = Player(name: 'jongya', job: 'magician');
  player01.skillRunQuick();
  print(player01.strength);
  print(player01.name);
}
