/*
BST: Max

Create a max() method on the BST class that
returns the largest value found in the BST.
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

//: Helper Add function to create tree
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

var tree = new BST();
console.log(tree.maximum());  //: null
tree.add(3);
console.log(tree.maximum());  //: 3
tree.add(4);
console.log(tree.maximum());  //: 4
tree.add(2);
console.log(tree.maximum());  //: 4
tree.add(5);
console.log(tree.maximum());  //: 5
