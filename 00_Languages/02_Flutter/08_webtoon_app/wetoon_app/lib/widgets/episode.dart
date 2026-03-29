import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:url_launcher/url_launcher_string.dart';

import '../models/webtoon_episode_model.dart';

class Episode extends StatelessWidget {
  final WebtoonEpisodeModel episode;
  final webtoonId;

  const Episode({
    super.key,
    required this.episode,
    required this.webtoonId,
  });

  // 사용 방법 1 : Uri 객체를 만든 뒤 이를 넣어주기
  void onButtonTap() async {
    final url = Uri.parse(
        "https://comic.naver.com/webtoon/detail?titleId=${webtoonId}&no=${episode.id}&week=mon");
    await launchUrl(url);
  }

  // 사용 방법 2 : String으로 URL을 넣기
  // void onButtonTap() async {
  //   await launchUrlString("https://google.copm");
  // }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onButtonTap,
      child: Container(
        margin: EdgeInsets.only(bottom: 7), // container 들끼리 띄우기
        decoration: BoxDecoration(
            color: Colors.green.shade400,
            borderRadius: BorderRadius.circular(20)),
        child: Padding(
          padding: const EdgeInsets.symmetric(
            vertical: 10,
            horizontal: 40,
          ),
          child:
              Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
            Text(
              episode.title,
              style: TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.w500,
                fontSize: 20,
              ),
            ),
            Icon(
              Icons.chevron_right_rounded,
              color: Colors.white,
              size: 30,
            )
          ]),
        ),
      ),
    );
  }
}
