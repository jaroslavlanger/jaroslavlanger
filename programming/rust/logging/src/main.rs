use std::fs;
use tracing;
use tracing_appender;
use tracing_subscriber::{
    filter::LevelFilter,
    Layer,
    prelude::*,
};

fn main() {
    tracing::info!("this will never be seen");

    // TODO
    // Single subscriber
    //let subscriber = tracing_subscriber::FmtSubscriber::new();

    // use that subscriber to process traces emitted after this point
    /*
    let subscriber = tracing_subscriber::FmtSubscriber::new();
    tracing::subscriber::set_global_default(subscriber);
    let file = std::io::stdout();
    */
    let term_layer = tracing_subscriber::fmt::layer()
        .with_filter(LevelFilter::INFO);

    let file = fs::File::create("newtest").unwrap();
    let (non_blocking, _guard) = tracing_appender::non_blocking(file);
    let file_layer = tracing_subscriber::fmt::layer()
        .with_writer(non_blocking)
        .with_filter(LevelFilter::TRACE);

    tracing_subscriber::registry()
        .with(term_layer)
        .with(file_layer)
        .init(); // sets itself as global default subscriber

    /*
    tracing::subscriber::with_default(subscriber.finish(), || {
       tracing::event!(tracing::Level::INFO, "Hello");
    });
    */



    tracing::error!("This is an error message.");
    tracing::warn!("I warned you...");
    tracing::info!("Just to let you know info");
    tracing::debug!("casual debug");
    tracing::trace!("no one cares anyway");

    //warn! {
        //%cause,
        //"failed to parse command from frame"
    //};
}

// fn init_logging() {
    // // Set up the tracing subscriber with a formatted output for the terminal.
    // let terminal_subscriber = tracing_subscriber::FmtSubscriber::builder()
        // .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        // .with_span_events(FmtSpan::CLOSE)
        // .finish();
// 
    // // Set up the tracing subscriber to write to a log file.
    // let file_subscriber = tracing_subscriber::fmt::subscriber()
        // .json()
        // .with_max_level(tracing::Level::INFO)
        // .finish();
// 
    // // Set up a global tracing subscriber that combines both outputs.
    // let subscriber = Registry::default()
        // .with(tracing_subscriber::EnvFilter::from_default_env())
        // .with(terminal_subscriber)
        // .with(file_subscriber);
// 
    // tracing::subscriber::set_global_default(subscriber).unwrap();
// }
