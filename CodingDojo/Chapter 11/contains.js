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

var tree = new BST();
console.log(tree.contains(4));  //: false
tree.add(3);
console.log(tree.contains(4));  //: false
tree.add(4);
console.log(tree.contains(4));  //: true
tree.add(2);
console.log(tree.contains(1));  //: false
tree.add(1);
console.log(tree.contains(1));  //: true
