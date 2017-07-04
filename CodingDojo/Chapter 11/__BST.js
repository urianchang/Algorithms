//: Binary Search Tree object

//: Require BST node object
const BTNode = require('./__BSTnode');

function BST() {
    this.root = null;
}

//: Add nodes to BST
BST.prototype.add = function(value) {
    //: Check if root node exists
    if (this.root === null) {
        this.root = new BTNode(value);
    } else {
        //: Compare value at each node and move accordingly
        var runner = this.root;
        while (runner) {
            //: If value is equal...
            if (value === runner.val) {
                runner.count++;
                break;
            //: If value is less than...
            } else if (value < runner.val) {
                if (!runner.left) {
                    runner.left = new BTNode(value);
                    break;
                } else {
                    runner = runner.left;
                }
            //: If value is greater than...
            } else {
                if (!runner.right) {
                    runner.right = new BTNode(value);
                    break;
                } else {
                    runner = runner.right;
                }
            }
        }
    }
}

//: Finding height from root
BST.prototype.height = function() {
    if (this.root === null) {
        return 0;
    }
    return getHeight(this.root);
}

//: Recursive helper function to find height from a node
function getHeight(node) {
    if (node === null) {
        return 0;
    }
    return 1 + Math.max(getHeight(node.left), getHeight(node.right));
}

//: Check if BST is balanced
BST.prototype.isBalanced = function() {
    if (this.root === null) {
        return true;
    }
    return Math.abs(getHeight(this.root.left) - getHeight(this.root.right)) <= 1;
}

//: Return size of BST
BST.prototype.size = function() {
    if (this.root === null) {
        return 0;
    }
    //: Helper function to recursively count leaf nodes
    function flood(leaf) {
        if (leaf === null) {
            return 0;
        }
        return 1 + flood(leaf.left) + flood(leaf.right);
    }
    return flood(this.root);
}

//: Return minimum value of BST
BST.prototype.minimum = function() {
    //: Check if root node exists
    if (this.root === null) {
        return null;
    }
    var runner = this.root;
    while (runner.left) {
        runner = runner.left;
    }
    return runner.val;
}

//: Return maximum value of BST
BST.prototype.maximum = function() {
    //: Check if root node exists
    if (this.root === null) {
        return null;
    }
    var runner = this.root;
    while (runner.right) {
        runner = runner.right;
    }
    return runner.val;
}

//: Check if BST is empty
BST.prototype.isEmpty = function() {
    return this.root === null;
}

//: Check if value is in BST
BST.prototype.contains = function(value) {
    //: Check if root node exists
    if (this.root === null) {
        return false;
    }
    var runner = this.root;
    while (runner) {
        //: If value is found...
        if (value === runner.val) {
            return true;
        }
        //: If value is less than...
        if (value < runner.val) {
            if (!runner.left) {
                return false;
            }
            runner = runner.left;
        //: If value is greater than...
        } else {
            if (!runner.right) {
                return false;
            }
            runner = runner.right;
        }
    }
    return false;
}

module.exports = BST;
