
## Webtoon detail ui  

우선 페이지에 FutureBuilder를 넣어줄 것이다.  
퓨처빌더는 Future 형태의 자료형을 받아 UI를 빌드하는 위젯이다.  

```dart
FutureBuilder(
    future: ,// 퓨처빌더에서 사용할 자료. Future<> 형태의 자료이다.
    builder: (context,snapshot){ // context : 부모 위젯의 내용을 불러옴 snapshot : 퓨처형태의 snapshot
        //내용 작성
    }
)
```

이를 이용해서 웹툰의 소개글(about)과 장르(genre), 이용연령(age)를 넣어주면!  

```dart
body: Column(
        children: [
          SizedBox(
            height: 50,
          ),
          Row(...),
          SizedBox(
            height: 20,
          ),
          FutureBuilder(
            future: webtoon,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                // snapshot에 데이터가 있다면
                return Padding(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 50,
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        snapshot.data!.about,
                        style: TextStyle(
                          fontSize: 16,
                        ),
                      ),
                      SizedBox(
                        height: 15,
                      ),
                      Text(
                        '${snapshot.data!.genre} / ${snapshot.data!.age}',
                        style: TextStyle(
                          fontSize: 16,
                        ),
                      ),
                    ],
                  ),
                );
              }
              return Text(",,,");
            },
          )
        ],
      ),
```

![alt text](image-20.png)  



## episodes UI  

FutureBuilder 를 통해 유동성 있는 자료형을 UI빌드에 이용하고,  
Collection For 를 통해 여러 객체들을 리스팅해주며,  
Container를 이용해 버튼을 만들어준다.  

```dart
FutureBuilder(
    future: episodes,
    builder: (context, snapshot) {
        if (snapshot.hasData) {
        return Column(
            children: [
            for (var episode in snapshot.data!)
                Container(
                margin:
                    EdgeInsets.only(bottom: 7), // container 들끼리 띄우기
                decoration: BoxDecoration(
                    color: Colors.green.shade400,
                    borderRadius: BorderRadius.circular(10)),
                child: Padding(
                    padding: const EdgeInsets.symmetric(
                    vertical: 10,
                    horizontal: 40,
                    ),
                    child: Row(
                        mainAxisAlignment:
                            MainAxisAlignment.spaceBetween,
                        children: [
                        Text(
                            episode.title,
                            style: TextStyle(
                            color: Colors.white,
                            fontWeight: FontWeight.w500,
                            fontSize: 20,
                            ),
                        ),
                        Icon(
                            Icons.chevron_right_rounded,
                            color: Colors.white,
                            size: 30,
                        )
                        ]),
                ),
                )
            ],
        );
        }
        return Container();
    },
    ),
```

![alt text](image-21.png)  

