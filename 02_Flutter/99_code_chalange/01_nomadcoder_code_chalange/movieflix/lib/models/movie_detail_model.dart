class MovieDetailModel {
  String imageUrl, title, overview;
  double voteAverage;
  int voteCount, runtime;
  List<Map<String, dynamic>> genres;

  MovieDetailModel.fromJson(Map<String, dynamic> json)
      : imageUrl = json['poster_path'],
        title = json['title'],
        overview = json['overview'],
        voteAverage = json['vote_average'],
        voteCount = json['vode_count'],
        runtime = json['runtime'],
        genres = json['genres'];
}
