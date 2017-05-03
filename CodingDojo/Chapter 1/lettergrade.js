// Letter Grade
// Write a function that assigns and prints a letter grade.
// 90+ = A, 80-89 = B, 70-79 = C, 60-69 = D, lower than 60 = F

function score(num) {
  console.log("Score: "+num);
  if (num >= 90) {
    console.log("Grade: A");
  } else if (num < 90 && num >= 80) {
    console.log("Grade: B");
  } else if (num < 80 && num >= 70) {
    console.log("Grade: C");
  } else if (num < 70 && num >= 60) {
    console.log("Grade: D");
  } else {
    console.log("Grade: F");
  }
}

score(88);
score(61);
