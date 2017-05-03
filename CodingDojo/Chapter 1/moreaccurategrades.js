// More Accurate Grades
// Related to the Letter Grade algorithm.
// Add '-' and '+' signs in top and bottom 2% of A, B, C, and D.
// No A+.

function score(num) {
  console.log("Score: "+num);
  if (num > 92) {
    console.log("Grade: A");
  } else if (num <= 92 && num >= 90) {
    console.log("Grade: A-");
  } else if (num < 90 && num >= 88) {
    console.log("Grade: B+");
  } else if (num < 88 && num > 82) {
    console.log("Grade: B");
  } else if (num <= 82 && num > 80) {
    console.log("Grade: B-");
  } else if (num < 80 && num >= 78) {
    console.log("Grade: C+");
  } else if (num < 78 && num > 72) {
    console.log("Grade: C");
  } else if (num <= 72 && num > 70) {
    console.log("Grade: C-");
  } else if (num < 70 && num >= 68) {
    console.log("Grade: D+");
  } else if (num < 68 && num > 62) {
    console.log("Grade: D");
  } else if (num <= 62 && num > 60) {
    console.log("Grade: D-");
  } else {
    console.log("Grade: F");
  }
}

score(88);
score(61);
