/*
Binary Search Tree: Add

Create an add(val) method on BST object
to add new value to the tree. This entails
creating a BTNode with this value and
connecting it at the appropriate place in
the tree. Unless specified otherwise, BSTs
can contain duplicate values.
*/

function BTNode(value) {
    this.val = value;
    this.left = null;
    this.right = null;
}

function BST() {
    this.root = null;
}
