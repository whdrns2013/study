import 'dart:async';

import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<HomeScreen> {
  static int defaultTime = 1500; // static을 붙여야 다른 변수가 이 변수에 접근이 가능함
  int seconds = defaultTime;
  bool isRunning = false;
  late Timer timer;
  int roundCount = 0;
  int goalCount = 0;
  bool isSelected15 = false;
  bool isSelected20 = false;
  bool isSelected25 = true;
  bool isSelected30 = false;
  bool isSelected35 = false;

  void onTick(Timer timer) {
    if (seconds == 0) {
      setState(() {
        roundCount += 1;
        goalCount += 1;
        seconds = defaultTime;
        isRunning = false;
        timer.cancel();
      });
    } else {
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
    seconds = defaultTime;
    isRunning = false;
    setState(() {});
  }

  void selectTime15() {
    resetTimer();
    seconds = 15 * 60;
    defaultTime = seconds;
    isSelected15 = true;
    isSelected20 = false;
    isSelected25 = false;
    isSelected30 = false;
    isSelected35 = false;
    setState(() {});
  }

  void selectTime20() {
    resetTimer();
    seconds = 20 * 60;
    defaultTime = seconds;
    isSelected15 = false;
    isSelected20 = true;
    isSelected25 = false;
    isSelected30 = false;
    isSelected35 = false;
    setState(() {});
  }

  void selectTime25() {
    resetTimer();
    seconds = 25 * 60;
    defaultTime = seconds;
    isSelected15 = false;
    isSelected20 = false;
    isSelected25 = true;
    isSelected30 = false;
    isSelected35 = false;
    setState(() {});
  }

  void selectTime30() {
    resetTimer();
    seconds = 30 * 60;
    defaultTime = seconds;
    isSelected15 = false;
    isSelected20 = false;
    isSelected25 = false;
    isSelected30 = true;
    isSelected35 = false;
    setState(() {});
  }

  void selectTime35() {
    resetTimer();
    seconds = 35 * 60;
    defaultTime = seconds;
    isSelected15 = false;
    isSelected20 = false;
    isSelected25 = false;
    isSelected30 = false;
    isSelected35 = true;
    setState(() {});
  }

  String format(int seconds, int start, int end) {
    var duration = Duration(seconds: seconds);
    return duration.toString().split(".").first.substring(start, end);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        // color: Theme.of(context).backgroundColor,
        decoration: BoxDecoration(
            gradient: LinearGradient(
                // 그라디언트
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
              Theme.of(context).backgroundColor,
              Theme.of(context).backgroundColor,
              Theme.of(context).backgroundColor,
              Theme.of(context).backgroundColor,
              Theme.of(context).backgroundColor,
              Color.fromARGB(228, 255, 114, 6)
            ])),
        child: Column(
          children: [
            SizedBox(
              height: 55,
            ),
            HeadLine(),
            SizedBox(
              height: 100,
            ),
            Padding(
              padding: EdgeInsets.fromLTRB(20, 0, 20, 0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  TimeCard(
                    time: format(seconds, 2, 4),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(20),
                    child: Text(
                      ":",
                      style: TextStyle(fontSize: 75, color: Colors.white60),
                    ),
                  ),
                  TimeCard(
                    time: format(seconds, 5, 7),
                  )
                ],
              ),
            ),
            SizedBox(
              height: 30,
            ),
            Padding(
              padding: EdgeInsets.all(20),
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Container(
                  child: Row(
                    children: [
                      GestureDetector(
                        onTap: selectTime15,
                        child: SelectTime(time: 15, isSelected: isSelected15),
                      ),
                      SizedBox(
                        width: 20,
                      ),
                      GestureDetector(
                        onTap: selectTime20,
                        child: SelectTime(time: 20, isSelected: isSelected20),
                      ),
                      SizedBox(
                        width: 20,
                      ),
                      GestureDetector(
                        onTap: selectTime25,
                        child: SelectTime(time: 25, isSelected: isSelected25),
                      ),
                      SizedBox(
                        width: 20,
                      ),
                      GestureDetector(
                        onTap: selectTime30,
                        child: SelectTime(time: 30, isSelected: isSelected30),
                      ),
                      SizedBox(
                        width: 20,
                      ),
                      GestureDetector(
                        onTap: selectTime35,
                        child: SelectTime(time: 35, isSelected: isSelected35),
                      ),
                    ],
                  ),
                ),
              ),
            ),
            SizedBox(
              height: 80,
            ),
            IconButton(
              onPressed: isRunning ? pauseTimer : startTimer,
              icon: Icon(
                isRunning
                    ? Icons.pause_circle_filled_outlined
                    : Icons.play_circle,
                color: Colors.white,
                size: 100,
              ),
            ),
            isRunning
                ? SizedBox(
                    height: 66,
                  )
                : IconButton(
                    onPressed: resetTimer,
                    icon: Icon(Icons.restore, color: Colors.white, size: 50),
                  ),
            SizedBox(
              height: 30,
            ),
            Padding(
              padding: EdgeInsets.fromLTRB(80, 0, 80, 0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  RoundGoal(chil: 0, parnt: 4, txt: "ROUND"),
                  SizedBox(
                    width: 110,
                  ),
                  RoundGoal(chil: 0, parnt: 12, txt: "GOAL"),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }
}

// RoundGoal
class RoundGoal extends StatelessWidget {
  int chil;
  int parnt;
  String txt;

  RoundGoal({
    super.key,
    required this.chil,
    required this.parnt,
    required this.txt,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          "${chil.toString()}/${parnt.toString()}",
          style: TextStyle(
            fontSize: 20,
            color: Colors.white60,
            fontWeight: FontWeight.w500,
          ),
        ),
        Text(
          "${txt}",
          style: TextStyle(
              fontSize: 20, color: Colors.white, fontWeight: FontWeight.w600),
        ),
      ],
    );
  }
}

// SelectTime
class SelectTime extends StatelessWidget {
  int time;
  bool isSelected;

  SelectTime({
    super.key,
    required this.time,
    required this.isSelected,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 50,
      width: 70,
      decoration: BoxDecoration(
          border: Border.all(color: Colors.white, width: 1),
          color: isSelected ? Colors.white : Theme.of(context).backgroundColor,
          borderRadius: BorderRadius.circular(10)),
      child: Center(
        child: Text(
          time.toString(),
          style: TextStyle(
              fontSize: 35,
              color: isSelected
                  ? Theme.of(context).backgroundColor
                  : Colors.white),
        ),
      ),
    );
  }

  void timeSelect(int time) {}
}

// TimeCard
class TimeCard extends StatelessWidget {
  String time;

  TimeCard({super.key, required this.time});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 200,
      width: 150,
      decoration: BoxDecoration(
          color: Colors.white, borderRadius: BorderRadius.circular(5)),
      child: Center(
        child: Text(
          time,
          style:
              TextStyle(color: Theme.of(context).backgroundColor, fontSize: 90),
        ),
      ),
    );
  }
}

// HeadLine
class HeadLine extends StatelessWidget {
  const HeadLine({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 10, 0, 0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Text(
            "POMOTIMER",
            style: TextStyle(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }
}
