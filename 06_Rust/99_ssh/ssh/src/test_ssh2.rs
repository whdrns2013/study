use ssh2::Session;
use std::net::TcpStream;
use std::io::Read;


pub fn do_ssh(host: &str,
              port: &str,
              user: &str,
              password: &str,
              command: &str) -> Result<String, String>{
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