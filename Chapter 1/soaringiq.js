// Soaring IQ
// Bogdan entered with IQ 101. IQ rose by .01 on first day
// then went up additional .02 on second day, .03 on third, etc.
// On 98th day, increase by 0.98. What is his final IQ?

function soaring(start, days){
  for (var i = 1; i <= days; i++) {
    start += i*0.01;
  }
  return start;
}

console.log("Final IQ: " + soaring(101, 98));
