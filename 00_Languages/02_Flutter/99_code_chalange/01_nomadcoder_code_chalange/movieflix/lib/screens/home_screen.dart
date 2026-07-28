import 'package:flutter/material.dart';
import 'package:movieflix/models/coming_soon_model.dart';
import 'package:movieflix/models/now_in_cinema_model.dart';
import 'package:movieflix/models/popular_movie_model.dart';
import 'package:movieflix/services/api_service.dart';

import '../widgets/coming_soon.dart';
import '../widgets/now_in_cinemas.dart';
import '../widgets/popular_movies.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});

  Future<List<PopularMovieModel>> popularMovies = ApiService.getPopularMovies();
  Future<List<NowInCinemaModel>> nowInCinemaMovies =
      ApiService.getNowInCinemaMovies();
  Future<List<ComingSoonModel>> comingSoonMovies =
      ApiService.getComingSoonMovies();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Padding(
            padding: EdgeInsets.fromLTRB(30, 120, 0, 0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                TitleComp(text: "Popular Movies"),
                SizedBox(
                  height: 15,
                ),
                FutureBuilder(
                  future: popularMovies,
                  builder: (context, snapshot) {
                    if (snapshot.hasData) {
                      return SizedBox(
                        height: 220,
                        child: makePopularList(snapshot),
                      );
                    } else {
                      return Center(child: CircularProgressIndicator());
                    }
                  },
                ),
                SizedBox(
                  height: 30,
                ),
                TitleComp(text: "Now in Cinemas"),
                SizedBox(
                  height: 15,
                ),
                FutureBuilder(
                  future: nowInCinemaMovies,
                  builder: (context, snapshot) {
                    if (snapshot.hasData) {
                      return SizedBox(
                        height: 191,
                        child: makeNowInCinemaList(snapshot),
                      );
                    } else {
                      return Center(child: CircularProgressIndicator());
                    }
                  },
                ),
                SizedBox(
                  height: 30,
                ),
                TitleComp(text: "Coming soon"),
                SizedBox(
                  height: 15,
                ),
                FutureBuilder(
                  future: comingSoonMovies,
                  builder: (context, snapshot) {
                    if (snapshot.hasData) {
                      return SizedBox(
                        height: 191,
                        child: makeComingSoonList(snapshot),
                      );
                    } else {
                      return Center(child: CircularProgressIndicator());
                    }
                  },
                ),
              ],
            )),
      ),
    );
  }
}

class TitleComp extends StatelessWidget {
  final String text;

  const TitleComp({
    super.key,
    required this.text,
  });

  @override
  Widget build(BuildContext context) {
    return Text(
      "$text",
      style: TextStyle(
        fontSize: 20,
        fontWeight: FontWeight.w700,
      ),
    );
  }
}

ListView makePopularList(AsyncSnapshot<List<PopularMovieModel>> snapshot) {
  return ListView.separated(
    scrollDirection: Axis.horizontal,
    itemCount: snapshot.data!.length,
    itemBuilder: (context, index) {
      var movie = snapshot.data![index];
      return PopularMovie(
        imageUrl: movie.imageUrl,
        id: movie.id,
      );
    },
    separatorBuilder: (context, index) => SizedBox(
      width: 20,
    ),
  );
}

ListView makeNowInCinemaList(AsyncSnapshot<List<NowInCinemaModel>> snapshot) {
  return ListView.separated(
    scrollDirection: Axis.horizontal,
    itemCount: snapshot.data!.length,
    itemBuilder: (context, index) {
      var movie = snapshot.data![index];
      return NowInCinemas(
        imageUrl: movie.imageUrl,
        id: movie.id,
        title: movie.title,
      );
    },
    separatorBuilder: (context, index) => SizedBox(
      width: 20,
    ),
  );
}

ListView makeComingSoonList(AsyncSnapshot<List<ComingSoonModel>> snapshot) {
  return ListView.separated(
    scrollDirection: Axis.horizontal,
    itemCount: snapshot.data!.length,
    itemBuilder: (context, index) {
      var movie = snapshot.data![index];
      return ComingSoon(
        imageUrl: movie.imageUrl,
        id: movie.id,
        title: movie.title,
      );
    },
    separatorBuilder: (context, index) => SizedBox(
      width: 20,
    ),
  );
}
