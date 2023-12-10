# Rust

## Read First
* en.wikipedia.org/wiki/Rust_(programming_language)
* the book - doc.rust-lang.org/book
* https://doc.rust-lang.org/rust-by-example/
* create std - doc.rust-lang.org/std
* crates by popularity - https://crates.io/crates?sort=downloads
* crate api guidelines - https://rust-lang.github.io/api-guidelines/

## TODO
* https://doc.rust-lang.org/cargo/
* ide for rust - areweideyet.com
* https://rust-lang.github.io/async-book/
* rust announcements - https://blog.rust-lang.org/
* https://braiins-uni.mag.wiki/async.html
* reference - doc.rust-lang.org/stable/reference/
* formating - https://rust-lang.github.io/rustfmt/
* linting - doc.rust-lang.org/stable/clippy
* https://doc.rust-lang.org/rustdoc/
* https://rust-lang.github.io/rustup/
* rustonomicon (unsafe book) - https://doc.rust-lang.org/nomicon/
* background code checker - https://github.com/Canop/bacon
* https://nnethercote.github.io/perf-book/

## Crates
* https://tokio.rs/
** https://tokio.rs/tokio/tutorial
* https://docs.rs/flume/latest/flume/
* https://lib.rs/
* https://github.com/hyperium/hyper/tree/master/examples
* https://crates.io/crates/futures
* https://github.com/awesome-rust-com/awesome-rust
* https://doc.rust-lang.org/std/marker/struct.PhantomData.html
* mutex, rwlock - https://docs.rs/parking_lot/latest/parking_lot/
* https://github.com/spacejam/sled
* https://github.com/JasonShin/fp-core.rs
* https://crates.io/crates/cargo-audit

## Cargo
```sh
cargo new
cargo check
cargo clean
cargo run
cargo doc --open
cargo clippy
cargo fmt
```

## Comments
* inner doc comments (starting with `//!` or `/*!`) can only appear before [items](https://doc.rust-lang.org/stable/reference/items.html)

    io::stdin()
        .read_line(&mut name)
        .expect("Failed ...");
    let name: &str = name.trim();

    println!("Hello, {}!", name);

## Data Types
* https://doc.rust-lang.org/std/mem/fn.size_of.html
* https://doc.rust-lang.org/std/primitive.str.html
* https://doc.rust-lang.org/rust-by-example/primitives/array.html
* https://doc.rust-lang.org/stable/std/primitive.slice.html
* https://doc.rust-lang.org/book/ch04-03-slices.html
### Enum
* https://en.wikipedia.org/wiki/Tagged_union

## Option
* https://doc.rust-lang.org/std/option/index.html

## Result
* https://doc.rust-lang.org/nightly/core/result/enum.Result.html#method.map

## Ownership
* https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html
* assignment moves
* Copy types

## References
* https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html
### Dereferencing
* *a 
* Automatic dereferencing
* &&T -> &T
* https://doc.rust-lang.org/std/ops/trait.Deref.html

## Function
* https://en.wikipedia.org/wiki/Variadic_function

## Vector Collection
* https://doc.rust-lang.org/std/vec/struct.Vec.html
* https://doc.rust-lang.org/rust-by-example/fn/diverging.html

## String
* https://doc.rust-lang.org/std/string/struct.String.html
* https://doc.rust-lang.org/std/primitive.str.html#method.split
* <https://doc.rust-lang.org/std/primitive.slice.html#method.join>
* https://doc.rust-lang.org/std/primitive.str.html#method.trim_matches

## Format
* https://doc.rust-lang.org/std/fmt/

## Error handling
* https://doc.rust-lang.org/book/ch09-00-error-handling.html
* https://doc.rust-lang.org/std/macro.panic.html
* https://users.rust-lang.org/t/how-to-exit-on-error/64858/2

## Input and Output (IO)
* https://doc.rust-lang.org/std/macro.println.html
* https://doc.rust-lang.org/std/io/struct.Stdin.html#method.read_line
* https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines

## shadowing
    let name: &str = name.trim();

## loops
* https://doc.rust-lang.org/std/ops/struct.Range.html
`let a = 0..9;`

 = 'myloop loop {
    break 'myloop 10
 }

## Modules
    mod greetings {}

## Iterator
* https://doc.rust-lang.org/std/iter/
* https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.map
* https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.flatten
* https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.chain
* https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.min

## Itertools
* https://docs.rs/itertools/latest/itertools/trait.Itertools.html#method.collect_tuple

## Command line arguments
* https://doc.rust-lang.org/std/env/struct.Args.html
* https://doc.rust-lang.org/book/ch12-01-accepting-command-line-arguments.html

## Regex
* https://docs.rs/regex/1.4.2/regex/struct.Regex.html#method.split

## Functional rust
* https://stackoverflow.com/questions/63967743/what-is-the-correct-syntax-to-return-a-function-in-rust

## Operator Overloading
* https://doc.rust-lang.org/rust-by-example/trait/ops.html
* https://doc.rust-lang.org/core/ops/#traits

## Nightly
* https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.intersperse
