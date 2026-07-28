import 'package:flutter/material.dart';
import 'package:ui_header/widgets/buttons.dart';
import 'package:ui_header/widgets/CustomCard.dart';

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
        body: SingleChildScrollView(
          // 스크롤이 가능하게 함
          child: Padding(
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
                  height: 50,
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
                  height: 15,
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
                  height: 70,
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
                  height: 15,
                ),
                CustomCard(
                    currencyName: "Euro",
                    amountOfMoney: "6 248",
                    iconSelect: Icons.euro_rounded,
                    isBlackColor: true,
                    offsetX: 0,
                    offsetY: 0),
                CustomCard(
                  currencyName: "Bitcoin",
                  amountOfMoney: "55 622",
                  iconSelect: Icons.currency_bitcoin_rounded,
                  isBlackColor: false,
                  offsetX: 0,
                  offsetY: -25,
                ),
                CustomCard(
                  currencyName: "Dollar",
                  amountOfMoney: "28 981",
                  iconSelect: Icons.attach_money_outlined,
                  isBlackColor: true,
                  offsetX: 0,
                  offsetY: -50,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
