// Fit the First Value
// Your function should accept an array. If value at [0] is
// greater than array's length, print "Too big!";
// if value at [0] is less than array's length, print "Too small!";
// otherwise print "Just right!".

function yourmom(arr) {
  if (arr.length <= 1) {
    console.log("ERROR: Array is not long enough");
  } else {
    if (arr[0] > arr.length) {
      console.log("Too big!");
    } else if (arr[0] < arr.length) {
      console.log("Too small!");
    } else {
      console.log("Just right!");
    }
  }
}

a = [9];
b = [100, 2];
c = [1, 2, 3];
d = [2, 2];

yourmom(a);
yourmom(b);
yourmom(c);
yourmom(d);
