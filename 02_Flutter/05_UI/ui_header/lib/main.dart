import 'package:flutter/material.dart';
import 'package:ui_header/widgets/buttons.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Color(0xFF181818),
        body: Padding(
          padding: const EdgeInsets.symmetric(
            horizontal: 20,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(
                height: 55,
              ),
              const Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text(
                        "Hi, Selena",
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 28,
                          fontWeight: FontWeight.w800,
                        ),
                      ),
                      Text(
                        "Welcome Back",
                        style: TextStyle(
                          // color: Colors.white.withOpacity(0.8),
                          color: Color.fromRGBO(255, 255, 255, 0.8),
                          fontSize: 16,
                        ),
                      ),
                    ],
                  ),
                ],
              ),
              const SizedBox(
                height: 80,
              ),
              const Text(
                "Total Balance",
                style: TextStyle(
                  color: Color.fromRGBO(255, 255, 255, 0.85),
                  fontSize: 22,
                ),
              ),
              const SizedBox(
                height: 10,
              ),
              const Text(
                "\$7 123 456",
                style: TextStyle(
                  color: Color.fromRGBO(255, 255, 255, 1),
                  fontSize: 48,
                  fontWeight: FontWeight.w700,
                ),
              ),
              const SizedBox(
                height: 20,
              ),
              const Row(
                mainAxisAlignment:
                    MainAxisAlignment.spaceBetween, // 두 객체를 가장 멀리 분리
                children: [
                  Button(
                      // 버튼 객체를 외부에서 불러와 사용 (직접 만든 객체)
                      text: "Transfer", // 버튼 안의 문자 초기화
                      backgroundColor: Color(0xFFF1B33B), // 버튼 배경 색상 초기화
                      textColor: Colors.black), // 버튼 안의 문자 색상 초기화
                  Button(
                      text: "Request",
                      backgroundColor: Color(0xFF1F2123),
                      textColor: Colors.white),
                ],
              ),
              const SizedBox(
                // 빈 공간을 만들어낼 때
                height: 100,
              ),
              const Row(
                mainAxisAlignment:
                    MainAxisAlignment.spaceBetween, // 두 객체를 가장 멀리 분리
                crossAxisAlignment: CrossAxisAlignment.end, // 위아래 정렬 (아래 정렬)
                children: [
                  Text(
                    // 텍스트 객체
                    'Wallet', // 폰트 내용
                    style: TextStyle(
                      // 폰트 스타일
                      color: Colors.white, // 폰트 컬러
                      fontSize: 36, // 폰트 사이즈
                      fontWeight: FontWeight.w700, // 폰트 weight(두께)
                    ),
                  ),
                  Text(
                    'View All',
                    style: TextStyle(
                      color: Colors.white60,
                      fontSize: 18,
                    ),
                  ),
                ],
              ),
              const SizedBox(
                height: 20,
              ),
              Container(
                clipBehavior: // overflow (이 컨테이너를 넘어선 부분)을 어떻게 할지 정함
                    Clip.hardEdge, // overflow 를 딱 맞게 잘라버림(숨김)
                // 박스를 만들기 위한 컨테이너 위젯
                decoration: BoxDecoration(
                  // 컨테이너 데코레이션
                  color: const Color(0xFF1F2123), // 컨테이너 background color
                  borderRadius: BorderRadius.circular(25), // 둥글림 처리
                ),
                child: Padding(
                  // 내부 컨텐츠 여백 -> code action으로 쉽게 wrapping 가능
                  padding: EdgeInsets.all(30),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      const Column(
                        crossAxisAlignment: CrossAxisAlignment.start, // 좌측 정렬
                        children: [
                          Text(
                            "Euro",
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 32,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                          SizedBox(
                            height: 10,
                          ),
                          Row(
                            children: [
                              Text(
                                "6 248",
                                style: TextStyle(
                                  color: Colors.white,
                                  fontSize: 20,
                                ),
                              ),
                              SizedBox(
                                width: 5,
                              ),
                              Text(
                                "EUR",
                                style: TextStyle(
                                  color: Colors.white60,
                                  fontSize: 18,
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),
                      Transform.scale(
                        // 부모 위젯은 가만히 두고 이 위젯 아래의 위젯 크기만 조정하기
                        scale: 2.2,
                        child: Transform.translate(
                          offset: Offset(
                            -5,
                            14,
                          ), // 부모 위젯은 가만히 두고 이 위젯 아래의 위젯 위치만 조정
                          child: const Icon(
                            // Icon 위젯
                            Icons.euro_rounded, // 아이콘 종류
                            color: Colors.white, // 아이콘 색상
                            size: 88, // 아이콘 사이즈
                          ),
                        ),
                      )
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
