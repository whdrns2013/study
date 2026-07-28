mod test_ssh2;
    use dotenv::dotenv;
    use std::env;

fn main() {

    // load env file
    dotenv().ok();

    // read env varis
    let host = env::var("HOST_IP").expect("HOST_IP is not set");
    let port = env::var("HOST_PORT").expect("HOST_PORT is not set");
    let username = env::var("USERNAME").expect("USERNAME is not set");
    let password = env::var("PASSWORD").expect("PASSWORD is not set");

    // do ssh
    test_ssh2::do_ssh(&host, &port, &username, &password, "ls -al");
}
