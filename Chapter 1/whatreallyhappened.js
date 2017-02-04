// What Really Happened?
// Change whatHappensToday() function to create
// whatReallyHappensToday(). In new function, test
// for each disaster independently. With this new function,
// all 5 disasters may happen -- or none at all.

function random(){
  return Math.floor(Math.random()*100);
}

function whatreally() {
  if (random() < 10) {
    console.log("Volcano");
  }
  if (random() < 15) {
    console.log("Tsunami");
  }
  if (random() < 20) {
    console.log("earthquake");
  }
  if (random() < 25) {
    console.log("blizzard");
  }
  if (random() < 30) {
    console.log("meteor strike");
  }
}

whatreally();
