// Twelve Bar Blues
// Write a function that console.logs the number 1, then "chick",
// then "boom", then "chick", then 2, etc. until (including) 12.

function bomb(num) {
  var start = 1;
  while (start <= num) {
    console.log(start);
    console.log("chick");
    console.log("boom");
    console.log("chick");
    start++;
  }
}

bomb(12);
