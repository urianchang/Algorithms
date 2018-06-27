// Convert a decimal (base-10) number to a binary (base-2) number

function decToBin1(num) {
  return num.toString(2);
}

function decToBin2(num) {
  let output = [];
  let n = num;
  //: Divide by 2 until 0, keeping track of the remainder (i.e. 0 or 1)
  while (n) {
    output.push(n%2);
    n = Math.floor(n/2);
  }
  //: Reverse remainder array and join
  return output.reverse().join('');
}

console.log(decToBin1(2) === decToBin2(2));
console.log(decToBin1(4) === decToBin2(4));
console.log(decToBin1(10) === decToBin2(10));

// Convert a binary number string to decimal
function binToDec1(numStr) {
  return parseInt(numStr, 2);
}

function binToDec2(numStr) {
  let numArr = numStr.split('').reverse();
  //: Add all decimal values with "1"
  let sum = 0;
  for (let idx = 0; idx < numArr.length; idx++) {
    if (numArr[idx] === "1") {
      sum += Math.pow(2, idx);
    }
  }
  return sum;
}

console.log(binToDec1('1010') === binToDec2('1010'));
console.log(binToDec1('100') === binToDec2('100'));
console.log(binToDec1('10')  === binToDec2('10'));
