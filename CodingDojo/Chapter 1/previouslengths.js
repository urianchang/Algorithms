// Previous Lengths
// You are passed an array containing strings.
// Working within that same array, replace each string
// with a number -- the length of the string at the previous
// array index -- and return the array

function prevLength (arr) {
  for (var ind = arr.length-1; ind > 0; ind--) {
    arr[ind] = arr[ind-1].length;
  }
  arr[0] = 0;
  return arr;
}

a = ["bird", "is", "the", "word"];

console.log(prevLength(a));
