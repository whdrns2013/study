use ssh2::Session;
use std::net::TcpStream;
use std::io::Read;

// SSH 세션 생성
pub fn create_session(host: &str,
                      port: &str,
                      user: &str,
                      password: &str) -> Result<Session, String>{
    // TCP Connection
    let tcp = TcpStream::connect(format!("{host}:{port}"))
        .map_err(|e| format!("Failed to connect{}", e))?;
    println!("success to connect");

    // start SSH Session
    let mut session: Session = Session::new()
        .map_err(|_| "Could not create SSH session".to_string())?;
    session.set_tcp_stream(tcp);
    session.handshake().map_err(|e| format!("Handshake failed: {}", e))?;
    println!("success to handshake");

    // Cert
    session.userauth_password(user, password)
        .map_err(|e| format!("Authentication failed: {}", e))?;
    println!("success to Authentication");
    
    Ok(session)
}

// SSH 명령어 수행
pub fn run_command(session: &Session, command: &str) -> Result<String, String>{
    // run command
    let mut channel = session.channel_session().map_err(|e| format!("Channel failed: {}", e))?;
    channel.exec(command).map_err(|e| format!("Command failed: {}", e))?;
    println!("running command is {}", command);

    // Read Result
    let mut output = String::new();
    channel.read_to_string(&mut output).map_err(|e| format!("Read failed: {}", e))?;

    println!("{}", output);
    Ok(output)
}

// SSH 세션 종료
pub fn close_session(session: Session) -> Result<String, String>{
    drop(session);
    let mut output = "closing session success".to_string();
    Ok(output)
}