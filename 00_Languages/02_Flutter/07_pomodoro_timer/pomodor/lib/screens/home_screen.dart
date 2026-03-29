import 'dart:async';

import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<HomeScreen> {
  // basic props
  static const int twentyFiveMinutes = 10; // 여기엔 왜 static을 붙여야 하는가?
  int seconds = twentyFiveMinutes;
  bool isRunning = false;
  int count = 0;
  late Timer timer;
  bool isDayColor = true;

  void onTick(Timer timer) {
    if (seconds == 0) {
      // 0초가 되면 count +1, 시간 초기화, 타이머 중지
      setState(() {
        count = count + 1;
        seconds = twentyFiveMinutes;
        isRunning = false;
        timer.cancel();
      });
    } else {
      // 총 time 에서 1을 뺌
      setState(() {
        seconds = seconds - 1;
      });
    }
  }

  void startTimer() {
    timer = Timer.periodic(
      Duration(seconds: 1),
      onTick,
    );
    setState(() {
      isRunning = true;
    });
  }

  void pauseTimer() {
    timer.cancel();
    setState(() {
      isRunning = false;
    });
  }

  void resetTimer() {
    timer.cancel();
    setState(() {
      seconds = twentyFiveMinutes;
      isRunning = false;
    });
  }

  void changeDayAndNight() {
    setState(() {
      isDayColor = !isDayColor;
    });
  }

  String format(int seconds) {
    var duration = Duration(seconds: seconds);
    return duration.toString().split(".").first.substring(2, 7);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: (isDayColor
          ? Theme.of(context).backgroundColor
          : Theme.of(context).shadowColor),
      body: Column(
        children: [
          Flexible(
            flex: 9,
            child: Container(
              alignment: Alignment.bottomRight,
              child: IconButton(
                icon: Icon(
                  Icons.brightness_medium_sharp,
                  color: Theme.of(context).cardColor,
                ),
                iconSize: 40,
                onPressed: changeDayAndNight,
              ),
            ),
          ),
          Flexible(
            flex: 20,
            child: Container(
              alignment: Alignment.center, // 하단 중앙에 정렬
              child: Text(
                format(seconds),
                style: TextStyle(
                  color: Theme.of(context).cardColor,
                  fontSize: 89,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ),
          Flexible(
            flex: 30,
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  IconButton(
                    icon: Icon(
                      isRunning
                          ? Icons.pause_circle_outline
                          : Icons.play_circle_outline_outlined,
                      color: Theme.of(context).cardColor,
                    ),
                    iconSize: 120,
                    onPressed: isRunning ? pauseTimer : startTimer,
                  ),
                  IconButton(
                    icon: Icon(
                        isRunning
                            ? Icons.restore
                            : Icons.check_box_outline_blank,
                        color: (isRunning
                            ? Theme.of(context).cardColor
                            // : Theme.of(context).backgroundColor),
                            : (isDayColor
                                ? Theme.of(context).backgroundColor
                                : Theme.of(context).shadowColor))),
                    onPressed: resetTimer,
                    iconSize: 80,
                  ),
                ],
              ),
            ),
          ),
          Flexible(
            flex: 20,
            child: Row(
              children: [
                Expanded(
                  child: Container(
                    decoration: BoxDecoration(
                        color: Theme.of(context).cardColor,
                        borderRadius: BorderRadius.circular(50)),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          'Pomodors',
                          style: TextStyle(
                            fontSize: 20,
                            color: Theme.of(context).textTheme.headline1!.color,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                        Text(
                          '$count',
                          style: TextStyle(
                            fontSize: 58,
                            color: Theme.of(context).textTheme.headline1!.color,
                            fontWeight: FontWeight.w600,
                          ),
                        )
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
