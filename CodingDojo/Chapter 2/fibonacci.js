// Fibonacci
// Create a function to generate Fibonacci numbers.
// In this math sequence, each number is the sum of the previous two.

// function fibonacci(num) {
//     var arr = [0, 1];
//     if (num >= 2) {
//       for (var x = 2; x <= num; x++) {
//         arr.push(arr[x-1]+arr[x-2]);
//       }
//     }
//     return arr[num];
// }

//OR

function fibonacci(num) {
  var a = 1;
  var b = 0;
  var temp;

  while (num > 0) {
    temp = a;
    a = a + b;
    b = temp;
    num--;
  }

  return b;
}

console.log(fibonacci(0));
console.log(fibonacci(1));
console.log(fibonacci(2));
console.log(fibonacci(3));
console.log(fibonacci(4));
console.log(fibonacci(5));
console.log(fibonacci(6));
console.log(fibonacci(7));
