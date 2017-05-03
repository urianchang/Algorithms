// Fahrenheit to Celsius
// Create fahrenheitToCelsius(fDegrees) that accepts a number
// of degrees in Fahrenheit, and returns the equivalent temperature
// as expressed in Celsius degrees.
// For review, Fahrenheit = (9/5 * Celsius) + 32

function ftoc(f) {
  var c;
  c = (f-32)*(5/9);
  return c;
}

console.log(ftoc(100));
