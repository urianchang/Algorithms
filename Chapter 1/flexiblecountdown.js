// Flexible Countdown
// Based on earlier "Countdown by Fours", given lowNum, highNum,
// mult, print multiples of mult from highNum down to lowNum, using
// a FOR. For (2,9,3), print 9 6 3 (on successive lines).

function countdown(lowNum, highNum, mult) {
  for (var x = highNum; x >= lowNum; x -= mult) {
    console.log(x);
  }
}

countdown(2, 9, 3);
