import 'package:flutter/material.dart';

class ScheduleCard extends StatelessWidget {
  Color bgColor;
  List<String> startEndTime;
  String scheduleName;
  List<String> coworker;

  ScheduleCard({
    super.key,
    required Color this.bgColor,
    required List<String> this.startEndTime,
    required String this.scheduleName,
    required List<String> this.coworker,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          decoration: BoxDecoration(
            color: bgColor,
            borderRadius: BorderRadius.circular(30),
          ),
          width: 420,
          height: 225,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(15, 40, 20, 0),
            child: Row(
              children: [
                Container(
                  width: 25,
                  child: Column(
                    children: [
                      Text(
                        "${startEndTime[0]}",
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                      Text(
                        "${startEndTime[1]}",
                        style: TextStyle(
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                      Container(
                        width: 0.5,
                        height: 28,
                        color: Colors.black,
                      ),
                      Text(
                        "${startEndTime[2]}",
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                      Text(
                        "${startEndTime[3]}",
                        style: TextStyle(
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ],
                  ),
                ),
                Column(
                  children: [
                    Padding(
                      padding: const EdgeInsets.fromLTRB(20, 0, 0, 0),
                      child: Container(
                        width: 340,
                        child: Flexible(
                          child: RichText(
                            overflow: TextOverflow.ellipsis,
                            maxLines: 2,
                            textAlign: TextAlign.left,
                            // strutStyle: StrutStyle(fontSize: 3.0),
                            text: TextSpan(
                              text: "$scheduleName",
                              style: TextStyle(
                                fontSize: 64,
                                fontWeight: FontWeight.w500,
                                color: Colors.black,
                                height: 0.9,
                              ),
                            ),
                          ),
                        ),
                      ),
                    ),
                    SizedBox(
                      height: 20,
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(25, 10, 0, 0),
                      child: Container(
                        width: 335,
                        child: Row(
                          children: [
                            for (String worker in coworker)
                              Padding(
                                padding: const EdgeInsets.fromLTRB(0, 0, 25, 0),
                                child: Text(
                                  "${worker}",
                                  style: TextStyle(
                                    color: ((worker == 'ME')
                                        ? Colors.black
                                        : Colors.black45),
                                    fontSize: 16,
                                  ),
                                ),
                              ),
                          ],
                        ),
                      ),
                    ),
                  ],
                )
              ],
            ),
          ),
        )
      ],
    );
  }
}
