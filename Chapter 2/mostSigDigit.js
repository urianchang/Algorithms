// Most Significant Digit
// Given number of any size, return the most significant
// digit. If you already know what strings are, don't use them here.
// Hint: use WHILE to bring the most significant digit into range
// where you can use the friendly modulus operator.
// Most significant digit is the leftmost non-zero digit of a number.

function sigDigit(num) {
    if (Math.abs(num) >= 1) {
        var digit = num%10;
        while (Math.abs(num) > 9) {
            num = Math.trunc(num/10);
            digit = num%10;
        }
    } else if (Math.abs(num) < 1 && Math.abs(num) > 0) {
        while (Math.abs(num) < 1 && Math.abs(num) > 0) {
            var digit = Math.trunc((num*10)%10);
            if (Math.abs(digit) >= 1) {
                break;
            }
            num = (num*10)%1;
        }
    }
    return digit;
}

// Added Math.abs() for negative values.
console.log(sigDigit(-12345));
console.log(sigDigit(-67.89));
console.log(sigDigit(-0.00987));
