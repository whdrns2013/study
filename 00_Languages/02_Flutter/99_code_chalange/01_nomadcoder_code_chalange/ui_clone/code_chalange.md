![alt text](image.png)  

## 분석  

구역으로는 크게 세 부분으로 나누어져 있다.  

(1) 상단 - Bar : 프로필사진과 + 아이콘  
(2) 중단 - 날짜 : 수평으로 스크롤할 수 있는 날짜의 나열  
(3) 하단 - 카드 : 수직으로 스크롤할 수 있는, 일정 정보가 적힌 카드  

반복적으로 사용되는 컴포넌트는 하나가 있다.  

(1) 하단 - 카드 : 수직으로 스크롤할 수 있는, 일정 정보가 적힌 카드  


## 시작  

우선 컴포넌트들을 배치할 자리를 만든다.  

### 전체  

전체적으로는 하나의 열(Column)에 행(Row)들이 배열된 형태이므로 Column으로 감싼 뒤 위에서 분석한 것과 같이 상단, 중단, 하단 세 부분으로 나눈다.  

```dart
class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
          body: Column(
        children: [
          Text("상단"),
          Text("중단"),
          Text("하단"),
        ],
      )),
    );
  }
}

```

### 상단  

(1) 가장 위에 스피커 높이만큼의 공백을 넣는다.  
(2) 그리고 프로필과 + 아이콘을 넣을 수 있는 AppBar 정도 크기의 Row 컴포넌트를 잡는다.  
(3) Row 컴포넌트에 Image 위젯으로 프로필사진을 넣고, round 처리를 해준다.  
(4) Row 컴포넌트에 + 아이콘을 넣는다.  
(5) Row 를 정렬해준다.

```dart
Column(
    children: [
        SizedBox(
        height: 55,
        ),
        Padding(
        padding: const EdgeInsets.fromLTRB(25, 0, 20, 0),
        child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
            Container(
                width: 50,
                height: 50,
                child: Image.asset('assets/images/IMG_6872.jpg'),
            ),
            Icon(
                Icons.add,
                size: 35,
                color: Colors.white,
            )
            ],
        ),
        ),],)
```


### 중단  

(1) 전체적으로는 2개의 ROW로 구성된 Column으로 만든다.  
(2) 두 번째 줄은 Text 위젯으로 Today, 구분점, 날짜 세 부분으로 만들어준다.  
(2) 두 번째 줄은 가로로 스크롤이 가능하도록 해준다.  

```dart
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
```


### 하단  

(1) 반복적인 카드 형식이다.(컬럼으로 감싼다.)  
(2) 모서리에 라운드가 있다.  
(3) 일차적으로 두 부분의 컬럼(기간 / 일정과 사람)이 있다.  
(4) 첫 번째 컬럼은 5개의 행으로 구성되어 있다.  
(5) 두 번째 컬럼은 2개의 행으로 구성되어 있다.  
(6) 두 번째 컬럼의 첫 번째 행은 일정 이름이 기재된다.  
(7) 두 번째 컬럼의 두 번째 행은 사람 이름이 기재된다.  

```dart
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
```

```dart
// scheduleCard
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
```

## 참고  

### 컨테이너에 이미지 넣기  

https://security-nanglam.tistory.com/479  

주의할 점은 pubspec.yaml 파일에 assets 를 넣어줄 때 꼭 flutter 아래에 넣어줘야 한다는 점.

### 실선 긋기  

https://yj95.tistory.com/214  

### Text 자동 줄바꿈  

https://d-dual.tistory.com/7  

### Text 행간 조정  

https://yj95.tistory.com/263  

### Column 안에서 scroll 하기  

https://comeng.tistory.com/entry/FlutterColumn-%EC%95%88%EC%97%90%EC%84%9C-scroll%ED%95%98%EA%B8%B0  