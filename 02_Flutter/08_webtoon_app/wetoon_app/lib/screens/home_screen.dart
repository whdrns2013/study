import 'package:flutter/material.dart';
import 'package:wetoon_app/models/webtoon_model.dart';
import 'package:wetoon_app/services/api_service.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});
  // const HomeScreen({super.key}); // const 를 지워줘야 한다.
  // const는 컴파일 전에 값을 알고 있다는 뜻이기 때문에 컴파일 전에 값을 알 수 없는 Future값이 클래스 내에 있으면 const는 사용할 수 없다.

  // Future 변수를 API Service로부터 바로 받는다.
  Future<List<WebtoonModel>> webtoons = ApiService.getTodaysToons();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 1, // 음영 색상 (0 : 없음)
        title: Text(
          "Today's 툰s",
          style: TextStyle(
            fontSize: 26,
            fontWeight: FontWeight.w600,
          ),
        ),
        backgroundColor: Colors.white, // appBar 의 배경색
        foregroundColor: Colors.green, // appBar 의 전경색 (텍스트, 아이콘 등)
      ),
      body: FutureBuilder(
        future: webtoons,
        builder: (context, snapshot) {
          // future builder
          if (snapshot.hasData) {
            // snapshot에 데이터가 있으면
            return Column(
              children: [
                SizedBox(
                  height: 100,
                ),
                Expanded(child: makeList(snapshot)), // Expanded
              ],
            );
          } else {
            // snapshot에 데이터가 없으면
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
    );
  }

  ListView makeList(AsyncSnapshot<List<WebtoonModel>> snapshot) {
    return ListView.separated(
      // 리스트뷰 빌더 / 세퍼레이터
      scrollDirection: Axis.horizontal, // 스크롤
      itemCount: snapshot.data!.length, // 아이템카운트
      padding: EdgeInsets.symmetric(vertical: 10, horizontal: 20),
      itemBuilder: (context, index) {
        // 아이템빌더
        var webtoon = snapshot.data![index]; // 빌드할 아이템 선택
        return Column(
          children: [
            Container(
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
                webtoon.thumb,
                headers: const {
                  // 헤더를 추가하여 200 통신을 할 수 있도록 함
                  "User-Agent":
                      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                },
              ),
            ),
            SizedBox(
              height: 13,
            ),
            Text(
              webtoon.title,
              style: TextStyle(
                fontSize: 22,
              ),
            ),
          ],
        ); // 아이템을 텍스트로 나타내준다.
      },
      separatorBuilder: (context, index) => SizedBox(
        width: 40,
      ),
    );
  }
}

// 첫 번째 방법 (data fetch 후 state에 넣어주기)
// class _HomeScreenState extends State<HomeScreen> {
//   List<WebtoonModel> webtoons = []; // 웹툰 정보들을 담아둘 리스트
//   bool isLoading = true; // ?

//   void waitForWebToons() async {
//     // 웹툰 정보를 가져오는 함수. getTodaysToons 서비스가 비동기이기 때문에 이 함수도 비동기로 선언해줘야 한다. ★★★★★
//     webtoons = await ApiService.getTodaysToons(); // API로 받아오는 웹툰 정보
//     isLoading = false; // isLoading flag
//     setState(() {}); // 변경된 데이터를 적용해 새로고침
//   }

//   @override
//   void initState() {
//     super.initState();
//     waitForWebToons();
//   }

//   @override
//   Widget build(BuildContext context) {
//     print(webtoons); // initState 테스트
//     print(isLoading); // initState 테스트
//     return Scaffold(
//       backgroundColor: Colors.white,
//       appBar: AppBar(
//         elevation: 1, // 음영 색상 (0 : 없음)
//         title: Text(
//           "Today's 툰s",
//           style: TextStyle(
//             fontSize: 26,
//             fontWeight: FontWeight.w600,
//           ),
//         ),
//         backgroundColor: Colors.white, // appBar 의 배경색
//         foregroundColor: Colors.green, // appBar 의 전경색 (텍스트, 아이콘 등)
//       ),
//     );
//   }
// }

