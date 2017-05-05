/*
Greatest Common Factor:

Given two integers, create rGCF(num1, num2) to
recursively determine Greatest Common Factor
(the largest integer dividing evenly into both).
    1) gcf(a, b) == a, if a == b
    2) gcf(a, b) == gcf(a-b, b), if a > b
    3) gcf(a, b) == gcf(a, b-a), if b > a

Second: rework facts #2 and #3 to reduce stack
consumption and expand rGCF's reach. You should
be able to compute rCCF(123456, 987654).
*/

//: Part I
function rGCF(param1, param2) {
    if (param1 == param2) {
        return param1;
    }
    if (param1 > param2) {
        return rGCF(param1-param2, param2);
    }
    if (param1 < param2) {
        return rGCF(param1, param2-param1);
    }
}

console.log(rGCF(3, 7));    // 1
console.log(rGCF(18, 27));  // 9
console.log(rGCF(49, 14));  // 7

//: Part II
function GCF(param1, param2) {
    if (param1 == param2) {
        return param1;
    }
    if (param1 > param2) {
        if ((param1/param2) % 1 === 0) {
            return param2;
        } else {
            return GCF(param1-param2, param2);
        }
    }
    if (param1 < param2) {
        if ((param1/param2) % 1 === 0) {
            return param2;
        } else {
            return GCF(param1, param2-param1);
        }
    }
}
console.log(GCF(123456, 987654));   // 6
