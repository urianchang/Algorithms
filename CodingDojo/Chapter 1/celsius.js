// Celsius to Fahrenheit
// Create celsiusToFahrenheit(cDegrees) that accepts number of
// degrees Celsius, and returns the equivalent temperature
// expressed in Fahrenheit degrees.
// (Optional) Do Fah. and Cel. values equate at a certain number? For
// challenge, try series of Celsius values starting at 200 and descending.

function ctof(c) {
  var f;
  f = ((9/5)*c)+32;
  return f;
}

console.log(ctof(100));
console.log("...OPTIONAL...");
for (var x = 200; x >= -200; x--) {
  if (ctof(x) == x) {
    console.log("Fah and Cel are the same at: " + x);
  } else {
    continue;
  }
}
console.log("Check complete.");
