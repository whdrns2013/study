import 'package:flutter/material.dart';
import 'package:movieflix/screens/detail_screen.dart';

class PopularMovie extends StatelessWidget {
  final String imageUrl;
  final int id;

  const PopularMovie({
    super.key,
    required this.imageUrl,
    required this.id,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        String idString = id.toString();
        Navigator.push(
            context,
            MaterialPageRoute(
                builder: (context) => DetailScreen(id: idString)));
        // print(idString.runtimeType);
      },
      child: Container(
        // 눈여겨 볼 것 : clip 하는 방식 : fit
        height: 220,
        clipBehavior: Clip.hardEdge,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(10),
        ),
        child: Image.network(
          "https://image.tmdb.org/t/p/w500" + imageUrl,
          width: 300,
          fit: BoxFit.cover,
        ),
      ),
    );
  }
}
