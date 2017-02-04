// Math Help
// Cartman doesn't really like math class
// and needs help. You are given two numbers:
// coefficients M and B in the equation Y = MX + B.
// Build a function that returns the X-intercept.

function xint(m, b) {
  return (-b/m);
}

var M = 10;
var B = 9;
console.log("X-intercept is: " + xint(M, B));
