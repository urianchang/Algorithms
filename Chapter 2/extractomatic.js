// Extract-O-Matic
// Create the extractDigit(num, digitNum) function that given a number and
// a digit number, returns the numeral value of that digit. 0 represents the
// ones digit, 1 represents the tens digit, etc.

function extractDigit(num, digit) {
    var count = 0;
    var value = num%10;
    while (count != digit) {
        num = Math.floor(num/10);
        value = num%10;
        count++;
    }
    return value;
}

// console.log(extractDigit(1824, 7));
// console.log(extractDigit(1824, 0));

// Second: handle negative digitNum values, where -1 represents the tenths digit (0.x),
// -2 represents the hundredths digit (0.0x), etc.

function extractDigitv2(num, digit) {
    var count = 0;
    var value = num%10;
    while (count != digit) {
        if (digit < 0) {
            num = num*10;
            value = Math.trunc(num%10);
            count--;
        } else {
            num = Math.floor(num/10);
            value = num%10;
            count++;
        }
    }
    return value;
}

// console.log(extractDigitv2(1824, 1));
// console.log(extractDigitv2(1824, -1));
// console.log(extractDigitv2(123.45, -1));

// Third: handle negative num values as well, doing what you think is appropriate

// USE MATH.TRUNC() instead of MATH.FLOOR() to account for negative values.
function extractDigitv3(num, digit) {
    var count = 0;
    var value = num%10;
    while (count != digit) {
        if (digit < 0) {
            num = num*10;
            value = Math.trunc(num%10);
            count--;
        } else {
            num = Math.trunc(num/10);
            value = num%10;
            count++;
        }
    }
    return value;
}

console.log(extractDigitv3(-1824, 1));
console.log(extractDigitv3(-1824, -1));
console.log(extractDigitv3(-123.45, -1));
