use std::{
    io::{Cursor, Read, Write},
    fs,
    env,
};

use chrono::{offset::Utc, SecondsFormat};
use image::ImageFormat;

fn main() {
    let mut args = env::args().skip(1);
    let path = args.next().expect("path argument must be given");
    let convert = args.next().is_some();

    let mut bytes = Vec::new();

    // BufReader from file
    /*
    let mut file = fs::File::open(path).expect("File for the given path can not be opened.");
    */

    // Image reader from bytes
    /*
    let reader = image::io::Reader::new(Cursor::new(bytes))
        .with_guessed_format()
        .expect("Cursor io never fails");
    */

    // Image reader from file
    let reader = image::io::Reader::open(path)
        .expect("Image opening failed.")
        .with_guessed_format()
        .expect("The format should be deducible.");

    // Get format from reader.
    let format = reader.format().expect("The image format must be clear!");
    println!("{:?}", format);

    // BufReader from image reader
    let mut file = reader.into_inner();
    println!("{:?}", file);
    file.read_to_end(&mut bytes).expect("Reading the specified file failed.");

    let filename = Utc::now().to_rfc3339_opts(SecondsFormat::Secs, true);

    // Writing to a file
    if convert && format != ImageFormat::Png {
        println!("conversion...");
        // Convert to png
        let img = image::io::Reader::with_format(Cursor::new(bytes), format)
            .decode().expect("Image decoding failed.");

        let format = ImageFormat::Png;
        let ext = format!("{:?}", format).to_lowercase();
        let path = format!("{}.{}", filename, ext);

        img.save_with_format(path, format)
            .expect("Encoding and writing to a file should work.");
    } else {
        println!("just writing to a file...");
        let ext = format!("{:?}", format).to_lowercase();
        let path = format!("{}.{}", filename, ext);
        let mut file_new = fs::File::create(path).expect("File creation failed.");
        file_new.write_all(&bytes).expect("Writing the file failed.");
    }
}
