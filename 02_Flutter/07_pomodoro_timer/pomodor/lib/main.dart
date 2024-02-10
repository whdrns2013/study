import 'package:flutter/material.dart';
import 'package:pomodor/screens/home_screen.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        theme: ThemeData(
          backgroundColor: const Color(0xFFE7626C),
          shadowColor: const Color.fromARGB(255, 0, 44, 80),
          textTheme: const TextTheme(
            headline1: TextStyle(
              color: Color(0xFF232B55),
            ),
          ),
          cardColor: const Color(0xFFF4EDDB),
        ),
        home: const Scaffold(
          body: HomeScreen(),
        ));
  }
}
