//: https://www.hackerrank.com/challenges/js10-function/problem

function factorial(num) {
  if (num === 1) {
    return num;
  }
  return num * factorial(num-1);
}
