use std::sync::mpsc::channel;

fn main(){
    let (tx, rx) = channel();
    (0..5).map(|x| x * 2 + 1)
          .for_each(move |x| tx.send(x).unwrap());

    let v: Vec<_> = rx.iter().collect();
    assert_eq!(v, vec![1, 3, 5, 7, 9]);
}
