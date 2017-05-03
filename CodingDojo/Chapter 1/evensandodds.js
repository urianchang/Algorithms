// Evens and Odds
// Create a function that accepts an array. Every time
// that array has three odd values in a row, print
// "That's odd!" Every time the array has three evens in a row,
// print "Even more so!"

function evensAndOdds(arr) {
  var ecount = 0;
  var ocount = 0;
  for (var x = 0; x < arr.length; x++) {
    if (arr[x]%2 == 0) {
      ocount = 0;
      ecount++;
      if (ecount == 3) {
        ecount = 0;
        console.log("Even more so!");
      }
    } else {
      ecount = 0;
      ocount++;
      if (ocount == 3) {
        ocount = 0;
        console.log("That's odd!");
      }
    }
  }
  return 0;
}

a = [2, 4, 1, 1, 1, 8];
b = [3, 2, 4, 5, 8, 8, 8, 9];

console.log(evensAndOdds(a));
console.log(evensAndOdds(b));
