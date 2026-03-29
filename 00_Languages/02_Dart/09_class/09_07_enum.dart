enum Job {warrior, magician, thief}

// class Player {
//   String name;
//   String job;
//   Player({required this.name, required this.job});
// }

class Player {
  String name;
  Job job;
  Player({required this.name, required this.job});
}

void main() {
  // Player player01 = Player(name: 'jongya', job: 'megician');
  Player player02 = Player(name: 'jongya', job: Job.magician);
}