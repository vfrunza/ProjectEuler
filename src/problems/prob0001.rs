/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/
use std::time::Instant;

pub fn problem0001() {
    println!("Problem 1 - Multiples of 3 or 5");

    let iterations = 100000;
    let target = 1000;
    let now = Instant::now();

    for _i in 1..iterations {
        optimized(target);
    }

    let elapsed = now.elapsed();

    let sum = optimized(target);

    println!("Solution: {} | Elapsed: {:.2?}", sum, elapsed / iterations);
}

fn bruteforce(n: i32) -> i32 {
    let mut sum = 0;

    for i in 1..n {
        if i % 3 == 0 || i % 5 == 0 {
            sum = i + sum;
        }
    }
    sum
}

fn optimized(target: i32) -> i32 {
    sum_divisible_by(target, 3) + sum_divisible_by(target, 5) - sum_divisible_by(target, 15)
}

fn sum_divisible_by(target: i32, n: i32) -> i32 {
    let p = target / n;
    n * (p * (p + 1)) / 2
}
