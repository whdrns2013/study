import 'package:flutter/material.dart';
import 'package:ui_header/widgets/buttons.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: const Color(0xFF181818),
        body: Padding(
          padding: const EdgeInsets.symmetric(
            horizontal: 20,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(
                height: 55,
              ),
              const Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text(
                        "Hi, Selena",
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 28,
                          fontWeight: FontWeight.w800,
                        ),
                      ),
                      Text(
                        "Welcome Back",
                        style: TextStyle(
                          // color: Colors.white.withOpacity(0.8),
                          color: Color.fromRGBO(255, 255, 255, 0.8),
                          fontSize: 16,
                        ),
                      ),
                    ],
                  ),
                ],
              ),
              const SizedBox(
                height: 80,
              ),
              const Text(
                "Total Balance",
                style: TextStyle(
                  color: Color.fromRGBO(255, 255, 255, 0.85),
                  fontSize: 22,
                ),
              ),
              const SizedBox(
                height: 10,
              ),
              const Text(
                "\$7 123 456",
                style: TextStyle(
                  color: Color.fromRGBO(255, 255, 255, 1),
                  fontSize: 48,
                  fontWeight: FontWeight.w700,
                ),
              ),
              const SizedBox(
                height: 20,
              ),
              const Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Button(
                      text: "Transfer",
                      backgroundColor: Color(0xFFF1B33B),
                      textColor: Colors.black),
                  const Button(
                      text: "Request",
                      backgroundColor: Color(0xFF1F2123),
                      textColor: Colors.white),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
