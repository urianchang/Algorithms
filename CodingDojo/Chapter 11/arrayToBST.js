/*
Array to BST

Given an array that is sorted in ascending order,
return a BST object that is height-balanced.
*/

//: Require BT Node object
const BTNode = require('./__BSTnode');

//: Require BST object
let BST = require('./__BST');

function array2bst(arr) {
    let tree = new BST();
    let newArr = reorder(arr, []);
    for (var i = 0; i < newArr.length; i++) {
        tree.add(newArr[i]);
    }
    return tree;
}

function reorder(arr, memo) {
    if (arr.length === 0) {
        return;
    }
    let mid = Math.floor(arr.length/2);
    memo.push(arr[mid]);
    //: Recursively add mid points in the bottom half
    reorder(arr.slice(0, mid), memo);
    //: Recursively add mid points in the top half
    reorder(arr.slice(mid+1, arr.length), memo);
    return memo;
}

let arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
let tree1 = array2bst(arr1);
console.log(tree1.isBalanced());    //: true

let arr2 = [2, 4, 6, 8];
let tree2 = array2bst(arr2);
console.log(tree2.isBalanced());    //: true
