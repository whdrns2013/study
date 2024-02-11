## nicco 가 만든 네이버 웹툰 Unofficial API  

-- `/today` : Returns today's comics
-- `/:id` : returns a comic's information by`:id`  
-- `/:id/episodes`: Returns the latest episodes for a comic by 

```bash
https://webtoon-crawler.nomadcoders.workers.dev/

https://webtoon-crawler.nomadcoders.workers.dev/today
```  

## Unofficial API 살펴보기  

https://webtoon-crawler.nomadcoders.workers.dev/today 에 들어가보면 아래와 같이 오늘자 웹툰의 제목, 썸네일, id값을 볼 수 있다.  

```json
[
{
"id": "758150",
"title": "입학용병",
"thumb": "https://image-comic.pstatic.net/webtoon/758150/thumbnail/thumbnail_IMAG21_4135492154714961716.jpg"
},
{
"id": "809706",
"title": "사랑받는 시집살이",
"thumb": "https://image-comic.pstatic.net/webtoon/809706/thumbnail/thumbnail_IMAG21_de9581cd-9dfc-4500-9c5c-62c4299a5c30.jpg"
},
{
"id": "818806",
"title": "이웃집 연하",
"thumb": "https://image-comic.pstatic.net/webtoon/818806/thumbnail/thumbnail_IMAG21_e1b66355-0263-4fae-938f-ba9f8ff1ec9f.jpg"
},
{
"id": "819910",
"title": "홍끼의 메소포타미아 신화",
"thumb": "https://image-comic.pstatic.net/webtoon/819910/thumbnail/thumbnail_IMAG21_3e1f29a1-2233-4e85-bb2f-3232a1b8ab81.jpg"
},
...
{
"id": "813451",
"title": "내가 만든 이세계",
"thumb": "https://image-comic.pstatic.net/webtoon/813451/thumbnail/thumbnail_IMAG21_63771fb5-bb2b-4ecf-a9d8-1169fa9c73ab.jpeg"
},
{
"id": "814407",
"title": "프린키피아",
"thumb": "https://image-comic.pstatic.net/webtoon/814407/thumbnail/thumbnail_IMAG21_5b80b114-7602-4d9e-93b3-ac7c38b2375f.jpg"
}
]

```

그리고 여기서 알 수 있는 id값을 이용해 API의 두 번째 사용법인 /:id 부분에 id 값을 넣어주면 다음과 같이 해당 웹툰에 대한 정보를 얻을 수 있다.  

```json
{
"title": "입학용병",
"about": "어린 시절 비행기 추락 사고의 유일한 생존자 유이진. 살아남기 위해 용병으로 살아가던 유이진은 10년 후, 가족이 있는 고향으로 돌아왔다.",
"genre": "스토리, 액션",
"age": "12세 이용가",
"thumb": "https://shared-comic.pstatic.net/thumb/webtoon/758150/thumbnail/thumbnail_IMAG06_c355bfb3-959f-43e6-aec6-4314b3193532.jpg"
}
```  

그리고 API의 세 번째 사용법인 /:id/episodes 에 id 값을 넣어주면 최근 n개의 에피소드 정보를 가져와 돌려준다. 대략 30개 정도를 보여주는 것 같다.  

```json
[
{
"thumb": "https://image-comic.pstatic.net/webtoon/758150/171/thumbnail_202x120_a0904963-c095-4947-8e2d-25a76a53724d.jpg",
"id": "171",
"title": "170화",
"rating": "9.94",
"date": "24.02.10"
},
{
"thumb": "https://image-comic.pstatic.net/webtoon/758150/170/thumbnail_202x120_b73f87e6-08bc-45ba-a576-10d1a606e301.jpg",
"id": "170",
"title": "169화",
"rating": "9.94",
"date": "24.02.03"
},
...
{
"thumb": "https://image-comic.pstatic.net/webtoon/758150/143/thumbnail_202x120_69359675-be00-4bb2-ba1d-d2694f69ca5a.jpg",
"id": "143",
"title": "142화",
"rating": "9.93",
"date": "23.07.29"
},
{
"thumb": "https://image-comic.pstatic.net/webtoon/758150/142/thumbnail_202x120_c32a0eea-3748-44ed-bd34-e8428f3b7a70.jpg",
"id": "142",
"title": "141화",
"rating": "9.97",
"date": "23.07.22"
}
]

```

## API 정보 정리  

API 정보를 정리하면 아래와 같다.  

|구분|/today|/:id|/:id/eposodes|
|---|---|---|---|
|설명|오늘자 업로드 웹툰을 리스팅한 정보를 반환|특정 웹툰의 정보를 반환|특정 웹툰의 최신 30개 회차 정보 반환|
|length|flexible|1|30|
|props|id: 해당 웹튼의 id <br>title: 해당 웹툰의 제목<br>thumb: 해당 웹툰의 썸네일|title: 해당 웹툰의 제목<br>about: 해당 웹툰 소개글<br>genre: 해당 웹툰의 장르<br>age: 이용가 등급<br>thub: 해당 웹툰의 썸네일|thumb: 해당 웹툰의 썸네일<br>id: 에피소드 id<br>title: 에피소드의 제목<br>rating: 에피소드 평점<br>date: 업로드 날짜|

