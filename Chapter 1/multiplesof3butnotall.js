// Multiples of Three -- but Not All
// Using FOR, print multiples of 3 from -300 to 0.
// Skip -3 and -6.

for (var x = -300; x <= 0; x+=3) {
  if (x === -3) {
    continue;
  } else if (x === -6) {
    continue;
  } else {
    console.log(x);
  }
}
