// Whoa, That Sucker's Huge
// Add odd integers from -300,000 to 300,000,
// and console.log the final sum. Is there a shortcut?

var sum = 0;
for (var x = -300000; x <= 300000; x++) {
  sum += x;
}
console.log(sum);
