// Always Hungry
// Create a function that accepts an array,
// and prints "yummy" each time one of the values
// is equal to "food". If no array elements are
// "food", then print "I'm hungry" once.

function hunger(arr) {
  var hungry = true;
  for (var x = 0; x < arr.length; x++) {
    if (arr[x] == "food") {
      console.log("yummy");
      hungry = false;
    }
  }
  if (hungry == true)  {
    console.log("I'm hungry");
  }
  return 0;
}

me = [1, 2, 3, 4];
you = ["food", "food"];
console.log(hunger(me));
console.log(hunger(you));
