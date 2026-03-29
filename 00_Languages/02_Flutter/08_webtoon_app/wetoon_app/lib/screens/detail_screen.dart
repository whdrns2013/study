import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:url_launcher/url_launcher_string.dart';
import 'package:wetoon_app/models/webtoon_detail_model.dart';
import 'package:wetoon_app/models/webtoon_episode_model.dart';
import 'package:wetoon_app/services/api_service.dart';

import '../widgets/episode.dart';

class DetailScreen extends StatefulWidget {
  final String id, title, thumb;

  const DetailScreen({
    super.key,
    required this.id,
    required this.title,
    required this.thumb,
  });

  @override
  State<DetailScreen> createState() => _DetailScreenState();
}

class _DetailScreenState extends State<DetailScreen> {
  late Future<WebtoonDetailModel> webtoon;
  late Future<List<WebtoonEpisodeModel>> episodes;
  late SharedPreferences prefs; // 좋아요 저장
  bool isLiked = false; // 해당 웹툰에 대한 좋아요 여부 상태 state

  Future initPrefs() async {
    prefs = await SharedPreferences.getInstance(); // 인스턴스 생성
    final likedTonns =
        prefs.getStringList('likedToons'); // likedToons 라는 이름의 StringList를 불러옴
    if (likedTonns != null) {
      // likedToons라는 이름의 StringList가 핸드폰 저장소에 있다면
      if (likedTonns.contains(widget.id) == true) {
        // 좋아요 리스트에 현재 웹툰의 아이디가 저장되어있다면
        isLiked = true; // isLiked 상태를 true로 바꾼다.
        setState(() {}); // 상태값을 저장한다.
      }
    } else {
      // likedToons라는 이름의 StringList가 핸드폰 저장소에 없다면
      prefs.setStringList(
          "likedToons", []); // likedToons라는 이름의 StringList를 핸드폰 저장소에 생성한다.
    }
  }

  @override
  void initState() {
    super.initState();
    webtoon = ApiService.getToonById(widget.id);
    episodes = ApiService.getLatestEpisodesById(widget.id);
    initPrefs();
  }

  onHeartTap() async {
    final likedToons =
        prefs.getStringList('likedToons'); // likedToons 라는 이름의 StringList를 불러옴
    if (likedToons != null) {
      // likedToon 가 존재할 경우에 (위에서 Init 했으니 아마 존재할 것이나, 혹시 몰라)
      if (isLiked) {
        // 좋아요가 눌려있다면
        likedToons.remove(widget.id); // 좋아요 리스트에서 제거
      } else {
        // 좋아요가 눌려있지 않다면
        likedToons.add(widget.id); // 좋아요 리스트에 추가
      }
      await prefs.setStringList(
          "likedToons", likedToons); // 핸드폰 저장소에 likedToons를 저장함
      setState(() {
        isLiked = !isLiked; // 기존의 isLiked와 반대의 상태값을 저장해준다. (탭함 = 현재 상태와 반대가 됨)
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 1, // 음영 색상 (0 : 없음)
        title: Text(
          widget.title,
          style: TextStyle(
            fontSize: 26,
            fontWeight: FontWeight.w600,
          ),
        ),
        actions: [
          IconButton(
            onPressed: onHeartTap, // 좋아요 아이콘을 누를 때의 메서드
            icon: Icon(
              // isLiked 여부에 따라 하트를 채우거나 채우지 않거나
              isLiked ? Icons.favorite_rounded : Icons.favorite_outline_rounded,
            ),
          )
        ],
        backgroundColor: Colors.white, // appBar 의 배경색
        foregroundColor: Colors.green, // appBar 의 전경색 (텍스트, 아이콘 등)
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.symmetric(
            horizontal: 50,
            vertical: 50,
          ),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Hero(
                    tag: widget.id,
                    child: Container(
                      width: 250,
                      clipBehavior:
                          Clip.hardEdge, // 모서리를 튀어나오는 부분은 깔끔하게(hard) 제거
                      decoration: BoxDecoration(
                        // 박스 데코레이션
                        borderRadius: BorderRadius.circular(15), // 모서리 둥글게 처리
                        boxShadow: [
                          // 그림자 설정
                          BoxShadow(
                            blurRadius: 13,
                            offset: Offset(7, 7),
                            color: Colors.black.withOpacity(0.3),
                          )
                        ],
                      ),
                      child: Image.network(
                        // Image.networdk
                        widget.thumb,
                        headers: const {
                          // 헤더를 추가하여 200 통신을 할 수 있도록 함
                          "User-Agent":
                              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                        },
                      ),
                    ),
                  ),
                ],
              ),
              SizedBox(
                height: 20,
              ),
              FutureBuilder(
                future: webtoon,
                builder: (context, snapshot) {
                  if (snapshot.hasData) {
                    // snapshot에 데이터가 있다면
                    return Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          snapshot.data!.about, // snapshot의 about을 텍스트로 노출
                          style: TextStyle(
                            fontSize: 16,
                          ),
                        ),
                        SizedBox(
                          height: 15,
                        ),
                        Text(
                          '${snapshot.data!.genre} / ${snapshot.data!.age}',
                          style: TextStyle(
                            fontSize: 16,
                          ),
                        ),
                      ],
                    );
                  }
                  return Padding(
                    padding: const EdgeInsets.only(top: 50),
                    child: Center(child: CircularProgressIndicator()),
                  );
                },
              ),
              SizedBox(
                height: 20,
              ),
              FutureBuilder(
                future: episodes,
                builder: (context, snapshot) {
                  if (snapshot.hasData) {
                    return Column(
                      children: [
                        for (var episode in snapshot.data!)
                          Episode(episode: episode, webtoonId: widget.id)
                      ],
                    );
                  }
                  return Container();
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
