// Leap Year
// Write a function that determines whether a given year is a leap year.
// If a year is divisible by four, it is a leap year, unless it is divisible
// by 100. However, if it is divisible by 400, then it is.

var year = prompt("Enter a year: ");
var leap;

if (year%4 == 0) {
  if (year%400 == 0) {
    leap = true;
  } else if (year%100 == 0) {
    leap = false;
  } else {
    leap = true;
  }
} else {
  leap = false;
}

if (leap) {
  console.log("It is a leap year!");
} else {
  console.log("It is not a leap year");
}
