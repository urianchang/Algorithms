/*
Recursive Sigma

Write a recursive function that given a number
returns sum of integers from 1 to that number.
*/

function rsig(num) {
  if (num == 1) {
    return 1;
  }
  return rsig(num-1) + num;
}

console.log(rsig(10));
