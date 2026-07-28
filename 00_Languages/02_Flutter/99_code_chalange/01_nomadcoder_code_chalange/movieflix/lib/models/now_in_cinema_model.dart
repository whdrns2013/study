class NowInCinemaModel {
  String imageUrl, title;
  int id;

  NowInCinemaModel.fromJson(Map<String, dynamic> json)
      : imageUrl = json['poster_path'],
        id = json['id'],
        title = json['title'];
}
