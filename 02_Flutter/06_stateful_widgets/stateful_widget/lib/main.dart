import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

// + 버튼 누르면 숫자 증가
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

class _MyAppState extends State<MyApp> {
  List<int> numbers = [];

  void onClicked() {
    setState(() {
      numbers.add(numbers.length);
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
      backgroundColor: Color(0xFFF4EDDB),
      body: Center(
          child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            'Click Count',
            style: TextStyle(
              fontSize: 30,
            ),
          ),
          for (var n in numbers)
            Text(
              '$n',
              style: TextStyle(
                fontSize: 10,
                color: Colors.red,
              ),
            ),
          IconButton(
            onPressed: onClicked,
            icon: Icon(
              Icons.add_box_rounded,
              size: 40,
            ),
          ),
        ],
      )),
    ));
  }
}
