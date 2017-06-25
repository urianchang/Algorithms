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
    this.count = 1;
}

function BST() {
    this.root = null;
}

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

var tree = new BST();
tree.add(3);    //: Create root node
console.log(tree);
tree.add(4);    //: Add node to right of root
console.log(tree);
tree.add(2);    //: Add node to left of root
console.log(tree);
tree.add(3);    //: Increase count of root node by 1
console.log(tree);
