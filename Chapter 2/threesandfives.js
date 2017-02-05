// Threes and Fives
// Create threesFives() that adds values from 100 and 4000000 (inclusive)
// if that value is evenly divisible by 3 or 5 but not both.
// Display the final sum in the console.
// Bonus: Create a better function that allows you to enter #'s for ranges.

function threesFives(start, end) {
  var sum = 0;
  for (var x = start; x <= end; x++) {
    if (x%3 == 0 || x%5 == 0) {
      if (x%3 == 0 && x%5 == 0) {
        continue;
      } else {
        sum += x;
      }
    }
  }
  return sum;
}

console.log(threesFives(100, 4000000));
console.log(threesFives(3, 16));
