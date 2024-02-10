import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

// ======== + 버튼 누르면 숫자 증가 ========= //
// class _MyAppState extends State<MyApp> {
//   int counter = 0;

//   void onClicked() { // click시 일어날 일을 정의
//     setState(() {    // 데이터가 변경되면 state에 알려 새로고침
//       counter += 1;
//     });
//   }

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//         home: Scaffold(
//       backgroundColor: Color(0xFFF4EDDB),
//       body: Center(
//           child: Column(
//         mainAxisAlignment: MainAxisAlignment.center,
//         children: [
//           Text(
//             'Click Count',
//             style: TextStyle(
//               fontSize: 30,
//             ),
//           ),
//           Text(
//             '$counter',
//             style: TextStyle(
//               fontSize: 30,
//               color: Colors.red,
//             ),
//           ),
//           IconButton(    // 누를 아이콘
//             onPressed: onClicked,  // 아이콘을 누르면(onPressed) 일어날 일을 정의
//             icon: Icon(
//               Icons.add_box_rounded,
//               size: 40,
//             ),
//           ),
//         ],
//       )),
//     ));
//   }
// }

// ========== + 버튼 누르면 숫자가 리스트로 증가 ========== //
// class _MyAppState extends State<MyApp> {
//   List<int> numbers = [];

//   void onClicked() {
//     setState(() {
//       numbers.add(numbers.length);
//     });
//   }

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//         home: Scaffold(
//       backgroundColor: Color(0xFFF4EDDB),
//       body: Center(
//           child: Column(
//         mainAxisAlignment: MainAxisAlignment.center,
//         children: [
//           Text(
//             'Click Count',
//             style: TextStyle(
//               fontSize: 30,
//             ),
//           ),
//           for (var n in numbers)
//             Text(
//               '$n',
//               style: TextStyle(
//                 fontSize: 10,
//                 color: Colors.red,
//               ),
//             ),
//           IconButton(
//             onPressed: onClicked,
//             icon: Icon(
//               Icons.add_box_rounded,
//               size: 40,
//             ),
//           ),
//         ],
//       )),
//     ));
//   }
// }

// ============ Context, 스타일시트 사용법 ============ //
// class _MyAppState extends State<MyApp> {
//   int counter = 0;

//   void onClicked() {
//     setState(() {
//       counter += 1;
//     });
//   }

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//         theme: ThemeData(
//           textTheme: TextTheme(
//             titleLarge: TextStyle(
//               color: Colors.red,
//             ),
//           ),
//         ),
//         home: Scaffold(
//           backgroundColor: Color(0xFFF4EDDB),
//           body: Center(
//               child: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: [
//               MyLargeTitle(),
//             ],
//           )),
//         ));
//   }
// }

// class MyLargeTitle extends StatelessWidget {
//   const MyLargeTitle({
//     super.key,
//   });

//   @override
//   Widget build(BuildContext context) {
//     return Text(
//       'My Large Title',
//       style: TextStyle(
//           fontSize: 30, color: Theme.of(context).textTheme.titleLarge?.color),
//     );
//   }
// }

class MyLargeTitle extends StatefulWidget {
  const MyLargeTitle({
    super.key,
  });

  @override
  State<MyLargeTitle> createState() => _MyLargeTitleState();
}

class _MyLargeTitleState extends State<MyLargeTitle> {
  @override
  void initState() {
    // TODO: implement initState
    print('initState');
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
    print('dispose');
  }

  @override
  Widget build(BuildContext context) {
    print('build');
    return Text(
      'My Large Title',
      style: TextStyle(
          fontSize: 30, color: Theme.of(context).textTheme.titleLarge?.color),
    );
  }
}

class _MyAppState extends State<MyApp> {
  int counter = 0;
  bool showTitle = true;

  // @override
  // void initState() {
  //   print("initState");
  //   super.initState();
  // }

  // @override
  // void dispose() {
  //   super.dispose();
  //   print('dispose');
  // }

  void onClicked() {
    setState(() {
      counter += 1;
    });
  }

  void toggleTitle() {
    setState(() {
      showTitle = !showTitle;
      // showTitle == true ? showTitle = false : showTitle = true; // 이것과 같음
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        theme: ThemeData(
          textTheme: TextTheme(
            titleLarge: TextStyle(
              color: Colors.red,
            ),
          ),
        ),
        home: Scaffold(
          backgroundColor: Color(0xFFF4EDDB),
          body: Center(
              child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              showTitle ? MyLargeTitle() : Text('nothing'),
              IconButton(
                onPressed: toggleTitle,
                icon: Icon(
                  Icons.remove_red_eye,
                ),
              )
            ],
          )),
        ));
  }
}
