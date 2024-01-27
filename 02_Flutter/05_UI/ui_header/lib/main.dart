import 'package:flutter/material.dart';

void main() {
  runApp(App());
}

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          backgroundColor: Color(0xFF181818),
          body: Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              Padding(
                padding: EdgeInsets.symmetric(horizontal: 30),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    SizedBox(height: 55),
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
                        color: Color.fromRGBO(0, 0, 0, 0.8),
                        fontSize: 16,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          )),
    );
  }
}
