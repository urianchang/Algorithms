// Star Art
// Assume that you have a text field that is exactly 75 characters long.
// You want to fill it with spaces and asterisks. Print the given number
// of asterisks consecutively. Depending on which function is called,
// those stars should be left-justified or right-justified or centered.

function drawLeftStars(num) {
  if (num <= 75) {
    var str = "";
    for (var y = 1; y <= num; y++) {
      str += "*";
    }
    console.log(str);
  } else {
    console.log("Please use a number that is less than or equal to 75");
  }
}

drawLeftStars(7);

function drawRightStars(num) {
  if (num <= 75) {
    var str = "";
    var num_spaces = 75 - num;
    for (var i = 1; i <= num_spaces; i++) {
      str += " ";
    }
    for (var y = 1; y <= num; y++) {
      str += "*";
    }
    console.log(str);
  } else {
    console.log("Please use a number that is less than or equal to 75");
  }
}

drawRightStars(70);

function drawCenteredStars(num) {
  if (num <= 75) {
    var str = "";
    var num_spaces = 75 - num;
    for (var i = 1; i <= Math.floor(num_spaces/2); i++) {
      str += " ";
    }
    for (var x = 1; x <= num; x++) {
      str += "*";
    }
    for (var y = 1; y <= Math.ceil(num_spaces/2); y++) {
      str += " ";
    }
    console.log(str);
  } else {
    console.log("Please use a number that is less than or equal to 75");
  }
}

drawCenteredStars(40);
