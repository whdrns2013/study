import 'package:flutter/material.dart';

class CustomCard extends StatelessWidget {
  final String currencyName;
  final String amountOfMoney;
  final IconData iconSelect;
  final bool isBlackColor; // 색반전 카드이므로 bool만 받아서 색상을 정하기
  final _blackBgColor = const Color(0xFF1F2123); // _를 붙이는 건 "private" 의 의미이다.
  final _whiteBgColr = Colors.white;
  final double offsetX;
  final double offsetY;

  CustomCard(
      {super.key,
      required this.currencyName,
      required this.amountOfMoney,
      required this.iconSelect,
      required this.isBlackColor,
      required this.offsetX,
      required this.offsetY});

  @override
  Widget build(BuildContext context) {
    return Transform.translate(
      offset: Offset(offsetX, offsetY),
      child: Container(
        clipBehavior: // overflow (이 컨테이너를 넘어선 부분)을 어떻게 할지 정함
            Clip.hardEdge, // overflow 를 딱 맞게 잘라버림(숨김)
        // 박스를 만들기 위한 컨테이너 위젯
        decoration: BoxDecoration(
          // 컨테이너 데코레이션
          color: isBlackColor
              ? _blackBgColor
              : _whiteBgColr, // 컨테이너 background color 를 3항연산으로
          borderRadius: BorderRadius.circular(25), // 둥글림 처리
        ),
        child: Padding(
          // 내부 컨텐츠 여백 -> code action으로 쉽게 wrapping 가능
          padding: EdgeInsets.all(30),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start, // 좌측 정렬
                children: [
                  Text(
                    currencyName,
                    style: TextStyle(
                      color: isBlackColor ? _whiteBgColr : _blackBgColor,
                      fontSize: 32,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  const SizedBox(
                    height: 10,
                  ),
                  Row(
                    children: [
                      Text(
                        amountOfMoney,
                        style: TextStyle(
                          color: isBlackColor ? _whiteBgColr : _blackBgColor,
                          fontSize: 20,
                        ),
                      ),
                      const SizedBox(
                        width: 5,
                      ),
                      Text(
                        currencyName,
                        style: TextStyle(
                          color: isBlackColor
                              ? _whiteBgColr.withOpacity(0.7)
                              : _blackBgColor.withOpacity(0.7),
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
                  offset: const Offset(
                    -5,
                    14,
                  ), // 부모 위젯은 가만히 두고 이 위젯 아래의 위젯 위치만 조정
                  child: Icon(
                    // Icon 위젯
                    iconSelect, // 아이콘 종류
                    color:
                        isBlackColor ? _whiteBgColr : _blackBgColor, // 아이콘 색상
                    size: 88, // 아이콘 사이즈
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
