class PopularMovieModel {
  final String imageUrl;
  final int id;

  PopularMovieModel.fromJson(Map<String, dynamic> json)
      : imageUrl = json['poster_path'],
        id = json['id'];
}
