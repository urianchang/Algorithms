// Poor Kenny
// If there is a 10% chance of volcano,
// 15% chance of tsunami, 20% chance of earthquake,
// 25% chance of blizzard, and 30% chance of meteor strike.
// Write function whatHappensToday() to print the outcome.

function what() {
  var rand = Math.floor(Math.random()*100);
  if (rand >= 0 && rand < 10) {
    console.log("Volcano!");
  } else if (rand >= 10 && rand < 25) {
    console.log("Tsunami!");
  } else if (rand >= 25 && rand < 45) {
    console.log("Earthquake!");
  } else if (rand >= 45 && rand < 70) {
    console.log("Blizzard!");
  } else {
    console.log("Meteor Shower!");
  }
}

what();
