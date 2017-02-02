// This Length, That Value
// Given two numbers, return array of length num1 with each value num2.
// Print "Jinx!" if they are same.

function makearray(num1, num2) {
  if (num1 === num2) {
    console.log("Jinx!");
    return 0;
  } else {
    var arr = [];
    for (var x = 0; x < num1; x++) {
      arr.push(num2);
    }
    return arr;
  }
}

a = 8;
b = 10;
c = 8;

console.log(makearray(a, b));
console.log(makearray(a, c));
