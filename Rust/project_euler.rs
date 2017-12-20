extern crate test;
use test::Bencher;

#[bench]
fn bench_xor_1000_ints(b: &mut Bencher) {
    b.iter(|| {
        // use `test::black_box` to prevent compiler optimizations from disregarding
        // unused values
        test::black_box(main());
    });
}

fn main(){
    println!("Hello, world!");
}