// First Plus Length
// Given an array, return the sum of the first value in the array,
// plus the array's length. What happens if the array's given value
// is not a number, but a string like ("what?") or a boolean (like false)?

function firstlength(arr) {
  return arr[0]+arr.length;
}

a = [2, 4, 6];
b = ["what", "is", "it", 8];
c = [true, true, true, true, false];
console.log(firstlength(a));
console.log(firstlength(b));
console.log(firstlength(c));
