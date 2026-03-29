import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:ui_clone/widgets/scheduleCard.dart';

import 'widgets/profileImage.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Color.fromRGBO(31, 31, 31, 1),
        body: Column(
          children: [
            const SizedBox(
              height: 55,
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(25, 0, 20, 0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  ProfileImage(),
                  const Icon(
                    Icons.add,
                    size: 35,
                    color: Colors.white,
                  )
                ],
              ),
            ),
            const SizedBox(
              height: 20,
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(
                20,
                0,
                0,
                0,
              ),
              child: Column(
                children: [
                  const Row(
                    children: [
                      Text(
                        "MONDAY 16",
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ],
                  ),
                  SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                      children: [
                        Text(
                          "TODAY",
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 41,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                        Text(
                          "•",
                          style: TextStyle(
                            color: Colors.pink.shade400,
                            fontSize: 41,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                        Text(
                          "17  18  19  20  21  22  23  24  25  26  27  28  29  30  31",
                          style: TextStyle(
                            color: Colors.white.withOpacity(0.6),
                            fontSize: 41,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(
              height: 50,
            ),
            Container(
              height: 675,
              child: SingleChildScrollView(
                scrollDirection: Axis.vertical,
                clipBehavior: Clip.hardEdge,
                child: Column(
                  children: [
                    ScheduleCard(
                      bgColor: Color.fromRGBO(254, 245, 98, 1),
                      startEndTime: ["11", "30", "12", "20"],
                      scheduleName: "DESIGN MEETING",
                      coworker: ["ALEX", "HELENA", "NANA"],
                    ),
                    SizedBox(
                      height: 7,
                    ),
                    ScheduleCard(
                      bgColor: Color.fromRGBO(156, 110, 204, 1),
                      startEndTime: ["12", "35", "14", "10"],
                      scheduleName: "DAILY PROJECT",
                      coworker: ["ME", "RICHARD", "CIRY", "+4"],
                    ),
                    SizedBox(
                      height: 7,
                    ),
                    ScheduleCard(
                      bgColor: Color.fromRGBO(189, 237, 88, 1),
                      startEndTime: ["15", "00", "16", "30"],
                      scheduleName: "WEEKLY PLANNING",
                      coworker: ["DEN", "NANA", "MARK"],
                    ),
                    SizedBox(
                      height: 7,
                    ),
                    ScheduleCard(
                      bgColor: Color.fromRGBO(255, 255, 255, 1),
                      startEndTime: ["17", "00", "18", "30"],
                      scheduleName: "DAILY REPORT",
                      coworker: ["ME", "DONALD", "JACOB"],
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
