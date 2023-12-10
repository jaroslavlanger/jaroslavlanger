use chrono::{offset::Utc, SecondsFormat};

fn main() {
    let t = Utc::now();
    //let s = t.to_string();
    //let s = t.to_rfc3339();
    let s = t.to_rfc3339_opts(SecondsFormat::Secs, true);
    println!("{s}");
}
