use std::str::FromStr;

#[derive(Debug)]
enum Transformation {
    Lowercase,
    Uppercase,
}

impl Transformation {
    fn transform(&self, i: i32) -> i32 {
        match self {
            Transformation::Lowercase => i-1,
            Transformation::Uppercase => i+1,
        }
    }
}

#[derive(Debug, PartialEq, Eq)]
struct ParseTransformationError; // TODO

impl FromStr for Transformation {
    type Err = ParseTransformationError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "lowercase" => Ok(Transformation::Lowercase),
            "uppercase" => Ok(Transformation::Uppercase),
            _ => Err(ParseTransformationError),
        }
    }
}

fn add_one(n: i32) -> i32 {
    n+1
}

fn main() {
    let v = vec![1,2,3];
    let _tr: Transformation = "lowercase".parse().unwrap();
    println!("{:?}", v);

    println!("{:?}", Transformation::Lowercase.transform(0));
}
