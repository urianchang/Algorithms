//: https://www.hackerrank.com/challenges/js10-arrays/problem
/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
  let numSet = Array.from(new Set(nums));
  switch (numSet.size) {
    case 1:
      return numSet[0];
    case 2:
      return (numSet[0] > numSet[1]) ? numSet[1] : numSet[0];
    default:
      let largest, secondLargest;
      if (numSet[0] > numSet[1]) {
        largest = numSet[0];
        secondLargest = numSet[1];
      } else {
        largest = numSet[1];
        secondLargest = numSet[0];
      }
      for (let i = 2; i < numSet.length; i++) {
        if (numSet[i] > largest) {
          secondLargest = largest;
          largest = numSet[i];
        } else if (numSet[i] > secondLargest) {
          secondLargest = numSet[i];
        } else {
          continue;
        }
      }
      return secondLargest;
  }
}

console.log(getSecondLargest([9, 1, 2, 3, 4, 4, 4, 5]));
