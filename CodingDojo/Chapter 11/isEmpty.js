/*
BST: Is Empty

Create a isEmpty() method on the BST class that
returns whether the BST is empty.
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

BST.prototype.isEmpty = function() {
    return this.root === null;
}

var tree = new BST();
console.log(tree.isEmpty());  //: true
tree.add(3);
console.log(tree.isEmpty());  //: false
tree.add(4);
console.log(tree.isEmpty());  //: false
tree.add(2);
console.log(tree.isEmpty());  //: false
tree.add(5);
console.log(tree.isEmpty());  //: false
