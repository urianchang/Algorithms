// Factorial
// Write a function factorial(num) that, given a number,
// returns the product (multiplication) of all positive integers
// from 1 up to number (inclusive).
// Ex: factorial(3) = 6; factorial(5) = 120

function factorial(num) {
  var product = 1;
  for (var i = 1; i <= num; i++) {
    product *= i;
  }
  return product;
}

console.log(factorial(3));
console.log(factorial(5));
