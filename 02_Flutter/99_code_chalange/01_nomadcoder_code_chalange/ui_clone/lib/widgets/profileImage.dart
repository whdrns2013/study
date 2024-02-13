import 'package:flutter/material.dart';

class ProfileImage extends StatelessWidget {
  const ProfileImage({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(25),
        color: Colors.white,
      ),
      child: Image(
        image: AssetImage('assets/images/IMG_6872.jpg'),
        width: 50,
        height: 50,
      ),
      clipBehavior: Clip.hardEdge,
    );
  }
}
