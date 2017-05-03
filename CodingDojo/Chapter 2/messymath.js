// Messy Math
// Create a function messyMath(num) that will return the following sum:
// add all integer from 0 up to the given num, except for the following
// special cases of our count value:
//  1. If current count (not num) is evenly divisible by 3, don't add to sum, skip to next count
//  2. Otherwise, if current count is evenly divisible by 7, include it twice in sum instead of once
//  3. Regardless of the above, if current count is exactly 1/3 of num, return -1 immediately

function messyMath(num) {
  var sum = 0;
  var count = 0;
  while (count <= num) {
    if (count == ((1/3)*num)) {
      return -1;
    } else {
      if (count%3 == 0) {
        count++;
        continue;
      } else {
        if (count%7 == 0) {
          sum += count;
        }
        sum += count;
        count++;
      }
    }
  }
  return sum;
}

console.log(messyMath(4));
console.log(messyMath(8));
console.log(messyMath(15));
