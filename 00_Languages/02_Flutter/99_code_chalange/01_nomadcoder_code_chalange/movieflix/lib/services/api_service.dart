import 'dart:convert';

import 'package:movieflix/models/coming_soon_model.dart';
import 'package:movieflix/models/movie_detail_model.dart';
import 'package:movieflix/models/now_in_cinema_model.dart';
import 'package:movieflix/models/popular_movie_model.dart';
import 'package:http/http.dart' as http;

class ApiService {
  static String baseUrl = "https://movies-api.nomadcoders.workers.dev/";
  static String popular = "popular";
  static String nowInCinema = "now-playing";
  static String comingSoon = "coming-soon";
  static String detail = "movie?id=";
  static String imageBaseUrl = "https://image.tmdb.org/t/p/w500";

  static Future<List<PopularMovieModel>> getPopularMovies() async {
    List<PopularMovieModel> MoviesInstance = [];
    final url = Uri.parse(baseUrl + popular);
    final response = await http.get(url);
    if (response.statusCode == 200) {
      final List<dynamic> Movies = jsonDecode(response.body)['results'];
      for (var movie in Movies) {
        MoviesInstance.add(PopularMovieModel.fromJson(movie));
      }
    }
    return MoviesInstance;
  }

  static Future<List<NowInCinemaModel>> getNowInCinemaMovies() async {
    List<NowInCinemaModel> MoviesInstance = [];
    final url = Uri.parse(baseUrl + nowInCinema);
    final response = await http.get(url);
    if (response.statusCode == 200) {
      final List<dynamic> Movies = jsonDecode(response.body)['results'];
      for (var movie in Movies) {
        MoviesInstance.add(NowInCinemaModel.fromJson(movie));
      }
    }
    return MoviesInstance;
  }

  static Future<List<ComingSoonModel>> getComingSoonMovies() async {
    List<ComingSoonModel> MoviesInstance = [];
    final url = Uri.parse(baseUrl + comingSoon);
    final response = await http.get(url);
    if (response.statusCode == 200) {
      final List<dynamic> Movies = jsonDecode(response.body)['results'];
      for (var movie in Movies) {
        MoviesInstance.add(ComingSoonModel.fromJson(movie));
      }
    }
    return MoviesInstance;
  }

  static Future<MovieDetailModel> getMovieDetail(String id) async {
    final url = Uri.parse(baseUrl + "/" + detail + id);
    final response = await http.get(url); // 요청에 대한 응답을 받아옴
    if (response.statusCode == 200) {
      final Map<String, dynamic> movieInfo = jsonDecode(response.body);
      return MovieDetailModel.fromJson(movieInfo);
    }
    throw Error();
  }
}
