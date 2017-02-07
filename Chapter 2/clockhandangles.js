// Clock Hand Angles
// Create function that given a number of seconds since 12:00:00,
// prints angles (in degrees) of the hour, minute and second hands.
// As review, 360 degrees form a full rotation.

function clock(num) {
  var hours, minutes, seconds, days, weeks;
  hours = num/3600;
  minutes = (num - (3600*Math.trunc(hours)))/60;
  seconds = num - (3600*Math.trunc(hours)) - (60*Math.trunc(minutes));
  days = 0;
  weeks = 0;
  while (hours >= 12) {
    hours -= 12;
    days++;
    if (days == 14) {
      weeks++;
      days = 0;
    }
  }
  hours = hours*30;
  minutes = minutes*6;
  seconds = seconds*6;
  if (weeks > 0) {
    console.log("Week: " + weeks + " Hour hand: " + hours + " degs. Minute hand: " + minutes + " degs. Second hand: " + seconds + " degs.");
  } else {
    console.log("Hour hand: " + hours + " degs. Minute hand: " + minutes + " degs. Second hand: " + seconds + " degs.");
  }
}

// Optimized the clock function: Implemented arrays to hold the values to iterate through. Loops add to the string that is printed at the end.
function clockop(seconds){
    var label = ["Week hand", "Day hand", "Hour hand", "Minute hand", "Seconds hand"];
    var values = [604800, 86400, 3600, 60, 1];
    var deg = [52, 14, 12, 60, 60]
    var time_str = "";
    for (var x = 0; x < values.length; x++) {
        if (seconds >= values[x]) {
            time_str += label[x] + ": " + ((seconds/values[x])*(360/deg[x])) + " degs. ";
            seconds = seconds%values[x];
        }
    }
    console.log(time_str);
}

console.log("For 3600 seconds:");
clock(3600);
console.log();
clockop(3600);
console.log();
console.log("For 119730 seconds:");
clock(119730);
console.log();
clockop(119730);
