// Is Prime
// Return whether or not a given integer is prime.
// Prime numbers are only evenly divisible by themselves and 1.
// For now, just create one that is easy to understand and debug.

function isPrime(num) {
  if (num <= 1) {
    return "A prime number is a natural number greater than 1";
  }
  for (var i = 2; i < num; i++) {
    if (num%i == 0) {
      return "not prime";
    }
  }
  return "prime";
}

var count = 100;
while (count > 1) {
  if (isPrime(count) == "prime") {
    console.log(count);
  }
  count--;
}
