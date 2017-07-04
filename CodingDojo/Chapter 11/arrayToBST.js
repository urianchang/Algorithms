/*
Array to BST

Given an array that is sorted in ascending order,
return a BST object that is height-balanced.
*/

//: Require BT Node object
const BTNode = require('./__BSTnode');

//: Require BST object
let BST = require('./__BST');

var tree = new BST();
console.log(tree.isBalanced()); //: true
tree.add(3);
tree.add(2);
tree.add(1);
console.log(tree.isBalanced()); //: false
tree.add(4);
console.log(tree.isBalanced()); //: true
tree.add(5);
tree.add(6);
tree.add(7);
console.log(tree.isBalanced()); //: false
