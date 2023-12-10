use std::io;
use std::sync::mpsc;
use std::thread;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let (sender, receiver) = mpsc::channel();

    let reader = thread::spawn(move || {
        let mut buffer = String::new();
        let stdin = io::stdin();

        loop {
            buffer.clear();
            match stdin.read_line(&mut buffer) {
                Err(msg) => break Err(msg.to_string()), // wanted to do `e @ Err(_) => return e`
                Ok(0) => break Ok(()), // EOF
                Ok(_) => {
                    if let Err(msg) = sender.send(parse_line(&buffer)) {
                        break Err(msg.to_string())
                    } else {
                        continue
                    };
                },
            }
        }
    });

    let editor = thread::spawn(move || {
        for sth in receiver {
            match sth {
                Err(x) => eprintln!("{}", x),
                Ok((cmd, text)) => println!("Got: '{}', '{}'", cmd, text),
            }
        }
    });

    let (res_read, res_edit) = (reader.join(), editor.join());
    println!("{:?} {:?}", res_read, res_edit);
    Ok(())
}

fn parse_line(raw: &str) -> Result<(String, String), String> {
    let without_newline = if let Some(stripped) = raw.strip_suffix('\n') {
        stripped
    } else {
        raw
    };
    if let Some((cmd, arg)) = without_newline.trim_start().split_once(' ') {
        Ok((cmd.to_string(), arg.to_string()))
    } else {
        Err(format!("Couldn't parse into `<command> <input>`, data={:?}", raw))
    }
}
