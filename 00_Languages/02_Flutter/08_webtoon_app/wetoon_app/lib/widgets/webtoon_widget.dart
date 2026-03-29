import 'package:flutter/material.dart';
import 'package:wetoon_app/screens/detail_screen.dart';

class Webtoon extends StatelessWidget {
  final String title, thumb, id;

  const Webtoon({
    super.key,
    required this.title,
    required this.thumb,
    required this.id,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        // onTap : 탭했을 때
        Navigator.push(
          // navigator : 스크린을 넘겨준다.
          context,
          MaterialPageRoute(
            // route할 화면을 선택하고 파라미터를 넘겨준다.
            builder: (context) => DetailScreen(
              id: id,
              title: title,
              thumb: thumb,
            ),
            // fullscreenDialog: true,
          ),
        );
      },
      child: Column(
        children: [
          Hero(
            tag: id,
            child: Container(
              width: 250,
              clipBehavior: Clip.hardEdge, // 모서리를 튀어나오는 부분은 깔끔하게(hard) 제거
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
                thumb,
                headers: const {
                  // 헤더를 추가하여 200 통신을 할 수 있도록 함
                  "User-Agent":
                      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                },
              ),
            ),
          ),
          SizedBox(
            height: 13,
          ),
          Text(
            title,
            style: TextStyle(
              fontSize: 22,
            ),
          ),
        ],
      ),
    ); // 아이템을 텍스트로 나타내준다.;
  }
}
