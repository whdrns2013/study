import 'package:flutter/material.dart';
import 'package:wetoon_app/screens/home_screen.dart';
import 'package:wetoon_app/services/api_service.dart';

void main() {
  runApp(const MainApp());
  ApiService().getTodaysToons();
}

class MainApp extends StatelessWidget {
  const MainApp({super.key}); // 이 위젯의 key를 stateless widget이라는 슈퍼클래스에 보내는 것
  // 즉 위젯은 ID 같은 식별자 역할을 하는 key가 있다는 것.

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: HomeScreen(),
    );
  }
}
