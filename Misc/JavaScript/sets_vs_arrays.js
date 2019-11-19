/* Sets vs Arrays
 * Arrays can have duplicate values, but sets cannot. Data in an array is
 * ordered by index; sets use keys and elements are iterable in order of
 * insertion.
 */

const myArr = [1, 1, 2, 2, 3, 3];
const mySet = new Set(myArr);
// console.log(mySet);

// Accessing elements
console.log(mySet.values());

// Adding values
console.log("\n*** Adding values ***")
mySet.add(4);
mySet.add(2); // Value not added. No error thrown.
console.log(mySet.values());

// Removing values
console.log("\n*** Removing values ***")
mySet.delete(1);
console.log(mySet.values());
mySet.clear();
console.log(mySet.values());

// Sets use strict equality (===) to determine if value is unique. JavaScript
// compares objects by reference (not contents).
console.log("\n*** Uniqueness ***")
console.log(new Set([1, 2, 3, "3"]).values());
console.log(new Set([[1], [1]]).values());
console.log(new Set([{a: 1}, {a: 1}]).values());
