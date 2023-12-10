use std::collections::HashMap;

fn main() {

    let strings = vec![String::from("first"), 
                       String::from("second"),
                       String::from("third")];
    println!("{:?}", strings);
    let mut map: HashMap<usize, String> = HashMap::new();
    for (i, s) in strings.into_iter().enumerate() {
        map.insert(i, s);
    }
    let s = map.get_mut(&(0 as usize)).unwrap();
    println!("{:?}", map);
    println!("{:?}", s);
}
