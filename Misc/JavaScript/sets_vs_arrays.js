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
mySet.add(4);
mySet.add(2); // Value not added. No error thrown.
console.log(mySet.values());

// Removing values
mySet.delete(1);
console.log(mySet.values());
mySet.clear();
console.log(mySet.values());
