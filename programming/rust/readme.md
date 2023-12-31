# Rust

## Read First
* en.wikipedia.org/wiki/Rust_(programming_language)
* the book - doc.rust-lang.org/book
* https://doc.rust-lang.org/rust-by-example/
* crate api guidelines - https://rust-lang.github.io/api-guidelines/
* https://rust-unofficial.github.io/patterns/

## TODO
* https://github.com/pretzelhammer/rust-blog/blob/master/posts/common-rust-lifetime-misconceptions.md
* https://rust-lang.github.io/async-book/
* https://google.github.io/comprehensive-rust/
    * https://google.github.io/comprehensive-rust/exercises/concurrency/solutions-afternoon.html#broadcast-chat-application
* ide for rust - areweideyet.com
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
* https://github.com/rust-lang/rustlings

## Rust Language
* https://doc.rust-lang.org/core/
* Enum - https://en.wikipedia.org/wiki/Tagged_union
* Does not have variadic functions -> macros.

### Comments
* inner doc comments (starting with `//!` or `/*!`) can only appear before [items](https://doc.rust-lang.org/stable/reference/items.html)

### Data Types
* https://doc.rust-lang.org/std/mem/fn.size_of.html
* https://doc.rust-lang.org/std/primitive.str.html
* https://doc.rust-lang.org/rust-by-example/primitives/array.html
* https://doc.rust-lang.org/stable/std/primitive.slice.html
* https://doc.rust-lang.org/book/ch04-03-slices.html

### Ownership
* https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html
* assignment moves
* Copy types

### References
* https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html
* Automatic dereferencing
* `&&T -> &T`
* https://doc.rust-lang.org/std/ops/trait.Deref.html

### shadowing
* `let name: &str = name.trim();`

### loops
```
 = 'myloop loop {
    break 'myloop 10
 }
 ```

### Modules
* `mod greetings {}`

### Operator Overloading
* https://doc.rust-lang.org/rust-by-example/trait/ops.html
* https://doc.rust-lang.org/core/ops/#traits

## [Standard Library](https://doc.rust-lang.org/std/)

### Option
* https://doc.rust-lang.org/std/option/index.html

### Result
* https://doc.rust-lang.org/nightly/core/result/enum.Result.html#method.map

### Vector Collection
* https://doc.rust-lang.org/std/vec/struct.Vec.html
* https://doc.rust-lang.org/rust-by-example/fn/diverging.html

### String
* https://doc.rust-lang.org/std/string/struct.String.html
* https://doc.rust-lang.org/std/primitive.str.html#method.split
* https://doc.rust-lang.org/std/primitive.slice.html#method.join
* https://doc.rust-lang.org/std/primitive.str.html#method.trim_matches

### Format
* https://doc.rust-lang.org/std/fmt/

### Iterator
* https://doc.rust-lang.org/std/iter/
* https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.map
* https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.flatten
* https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.chain
* https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.min
* https://doc.rust-lang.org/std/ops/struct.Range.html

### Default
* https://doc.rust-lang.org/std/default/trait.Default.html

## Practices

### Error handling
* https://doc.rust-lang.org/book/ch09-00-error-handling.html
* https://doc.rust-lang.org/std/macro.panic.html
* https://users.rust-lang.org/t/how-to-exit-on-error/64858/2
* https://docs.rs/anyhow/latest/anyhow/
* https://docs.rs/thiserror/latest/thiserror/

### Input and Output (IO)
* https://doc.rust-lang.org/std/macro.println.html
* https://doc.rust-lang.org/std/io/struct.Stdin.html#method.read_line
* https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines

### Command line arguments
* https://doc.rust-lang.org/std/env/struct.Args.html
* https://doc.rust-lang.org/book/ch12-01-accepting-command-line-arguments.html

## Crates
* crates by popularity - https://crates.io/crates?sort=downloads
* https://lib.rs/
* https://github.com/awesome-rust-com/awesome-rust
* https://docs.rs/dashmap/latest/dashmap/struct.DashMap.html
* https://docs.rs/async-trait/latest/async_trait/
* https://crates.io/crates/futures
* https://docs.rs/argon2/latest/argon2/
* https://docs.rs/flume/latest/flume/
* https://github.com/hyperium/hyper/tree/master/examples
* https://doc.rust-lang.org/std/marker/struct.PhantomData.html
* mutex, rwlock - https://docs.rs/parking_lot/latest/parking_lot/
* https://github.com/spacejam/sled
* https://github.com/JasonShin/fp-core.rs
* https://crates.io/crates/cargo-audit

### Regex
* https://docs.rs/regex/1.4.2/regex/struct.Regex.html#method.split

### [Tokio](https://tokio.rs/)
* Asynchrony - IO bound then message passing (oneshot::channel) otherwise sharded mutex.
* Always bound everything with reasonable numbers.
* https://tokio.rs/tokio/tutorial
* https://github.com/tokio-rs/mini-redis/blob/master/src/lib.rs
* https://github.com/tokio-rs/mini-redis/blob/master/src/db.rs
* https://github.com/tokio-rs/tokio/blob/master/examples/chat.rs
* https://www.youtube.com/watch?v=fTXuGRP1ee4[Actors with Tokio – a lesson in ownership - Alice Ryhl]
* https://ryhl.io/blog/actors-with-tokio/
* https://docs.rs/tokio-util/latest/tokio_util/index.html

### sqlx
* https://docs.rs/sqlx/latest/sqlx/
* https://github.com/launchbadge/sqlx/blob/main/README.md
* https://github.com/launchbadge/sqlx/blob/main/examples/postgres/chat/src/main.rs
* [Rust to PostgreSQL with SQLX | Rust By Example](https://gist.github.com/jeremychone/34d1e3daffc38eb602b1a9ab21298d10)

### Itertools
* https://docs.rs/itertools/latest/itertools/trait.Itertools.html#method.collect_tuple

## [Cargo](https://doc.rust-lang.org/cargo/)
```sh
cargo new
cargo check
cargo clean
cargo run
cargo doc --open
cargo clippy
cargo fmt
```

## Functional rust
* https://stackoverflow.com/questions/63967743/what-is-the-correct-syntax-to-return-a-function-in-rust

## Nightly
* https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.intersperse
