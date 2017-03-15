/*
Recursive Fibonacci

Write rFib(num). Recursively compute and return numth Fibonacci value.
As earlier, treat first two Fibonacci vals as 0 and 1.
*/

function rFib(num) {
  if (num == 0) {
    return 0;
  }
  if (num == 1) {
    return 1;
  }
  return rFib(num-1) + rFib(num-2);
}

console.log(rFib(3));
