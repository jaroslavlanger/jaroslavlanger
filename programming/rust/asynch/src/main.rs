use tokio::io;
use std::thread::sleep;
use std::time::Duration;

/// IO bound then message passing (oneshot::channel)
/// otherwise sharded mutex, dashmap
/// Always bound everything with reasonable numbers...
#[tokio::main]
async fn main() -> io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:11111").await?;

    let a = async {
        println!("this is crazy async");
        5
    };

    //let streams: Vec<> = Vec::new();

    // loop {
    //     let (socket, _) = listener.accept().await?;
    //     process_socket(socket).await;
    // }
    // println!("{:?}", a.await);
    let b = a;
    sleep(Duration::from_secs(5));
    let c = b.await;

    loop {

        // break Ok(())
    }
}
