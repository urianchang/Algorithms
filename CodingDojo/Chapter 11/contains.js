/*
BST: Contains

Create a contains(val) method on BST that returns
whether the tree contains a given value. Take advantage
of the BST structure to make this a much more rapid operation
than SList.contains() would be.
*/

function BTNode(value) {
    this.val = value;
    this.left = null;
    this.right = null;
    this.count = 1;
}

function BST() {
    this.root = null;
}

BST.prototype.contains = function(value) {

}
