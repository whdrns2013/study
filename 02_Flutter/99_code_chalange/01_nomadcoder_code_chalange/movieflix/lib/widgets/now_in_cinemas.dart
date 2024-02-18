import 'package:flutter/material.dart';

class NowInCinemas extends StatelessWidget {
  final String imageUrl, title;
  final int id;

  const NowInCinemas(
      {super.key,
      required this.imageUrl,
      required this.title,
      required this.id});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              clipBehavior: Clip.hardEdge,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
              ),
              height: 160,
              child: Image.network(
                "https://image.tmdb.org/t/p/w500" + imageUrl,
                fit: BoxFit.cover,
                width: 150,
              ),
            ),
            SizedBox(
              height: 10,
            ),
            Text(title,
                style: TextStyle(
                  fontWeight: FontWeight.w500,
                  fontSize: 15,
                ))
          ],
        ),
      ],
    );
  }
}
