// Sum to One Digit
// Implement sumToOne(num) that sums a given integer's digits repeatedly
// until the sum is only one digit. Return that one-digit result.
// Ex: sumToOne(928) returns 1, because 9+2+8=19, then 1+9=10, then 1+0=1.


// function sumToOne(num) {
//   var sum = num;
//   while (num > 9) {
//     sum = Math.floor(num/100);
//     sum += Math.floor((num%100)/10);
//     sum += num%10;
//     num = sum;
//   }
//   return sum;
// }

// OR

function sumToOne(num) {
  var sum = num;
  while (sum > 9) {
    sum = 0;
    while (num > 0) {
      sum += Math.floor(num%10);
      num = num/10;
    }
    num = sum;
  }
  return sum;
}

console.log(sumToOne(928));
console.log(sumToOne(2568));
