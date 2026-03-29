// src/main.rs

#[macro_use] extern crate rocket;
mod routes;  // api 모듈을 가져옴

// 메인 함수에서 서버 실행
#[launch]
fn rocket() -> _ {
    rocket::build()
        .mount("/", routes::router::get_routes())  // api의 라우터 등록
}