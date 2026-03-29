class ComingSoonModel {
  String imageUrl, title;
  int id;

  ComingSoonModel.fromJson(Map<String, dynamic> json)
      : imageUrl = json['poster_path'],
        id = json['id'],
        title = json['title'];
}
