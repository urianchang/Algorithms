// Sigma
// Implement function sigma(num) that given a number, returns
// the sum of all positive integers up to number (inclusive).
// Ex: sigma(3) = 6

function sigma(num) {
  var sum = 0;
  for (var i = 1; i <= num; i++) {
    sum += i;
  }
  return sum;
}

console.log(sigma(5));
