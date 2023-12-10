fn main() {
    let format = String::from("hey");
    let bytes = vec![1,2,3,4];
    let img = structs::Image { format, bytes };
    println!("{:?}", img);
}
