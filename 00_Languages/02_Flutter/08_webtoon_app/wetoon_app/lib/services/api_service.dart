import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:wetoon_app/models/webtoon_detail_model.dart';
import 'package:wetoon_app/models/webtoon_episode_model.dart';
import 'package:wetoon_app/models/webtoon_model.dart';

class ApiService {
  static const String baseUrl =
      "https://webtoon-crawler.nomadcoders.workers.dev";
  static const String today = "today";

  static Future<List<WebtoonModel>> getTodaysToons() async {
    // async(비동기) 이기 때문에 반환값을 Future로 감싸줘야 함
    List<WebtoonModel> webtoonsInstances = [];
    final url = Uri.parse(baseUrl + "/" + today);
    final response = await http.get(url); // 요청에 대한 응답을 받아옴
    if (response.statusCode == 200) {
      // 요청 처리가 정상(200) 일 경우
      final List<dynamic> webtoons = jsonDecode(response.body);
      for (var webtoon in webtoons) {
        webtoonsInstances.add(
            WebtoonModel.fromJson(webtoon)); // WetoonModel 클래스로 정보를 받아 리스트에 넣어줌
      }
      return webtoonsInstances;
    }
    throw Error(); // 요청 처리가 정상이 아닐 경우 Error를 발생시킨다.
  }

  static Future<WebtoonDetailModel> getToonById(String id) async {
    final url = Uri.parse(baseUrl + "/" + id);
    final response = await http.get(url); // 요청에 대한 응답을 받아옴
    if (response.statusCode == 200) {
      final webtoon = jsonDecode(response.body);
      return WebtoonDetailModel.fromJson(webtoon);
    }
    throw Error();
  }

  static Future<List<WebtoonEpisodeModel>> getLatestEpisodesById(
      String id) async {
    List<WebtoonEpisodeModel> episodesInstance = [];
    final url = Uri.parse(baseUrl + "/" + id + "/episodes");
    final response = await http.get(url); // 요청에 대한 응답을 받아옴
    if (response.statusCode == 200) {
      final episodes = jsonDecode(response.body);
      for (var episode in episodes) {
        episodesInstance.add(WebtoonEpisodeModel.fromJson(episode));
      }
      return episodesInstance;
    }
    throw Error();
  }
}
