use rocket::{get, routes};

#[get("/")]
pub fn index_default() -> &'static str {
    "Hello from the router!\nIt's default path."
}

#[get("/localhost")]
pub fn index_localhost() -> &'static str {
    "Hello from the router!\nIt's localhost path."
}

// 라우터를 반환하는 함수
pub fn get_routes() -> Vec<rocket::Route> {
    routes![index_default, index_localhost]
}