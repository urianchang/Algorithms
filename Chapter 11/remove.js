/*
BST: Remove

Remove a given val. Return false if not found.
*/

function BSTree() {
    this.root = null;
}
function BSNode(value) {
    this.value = value;
    this.left = null;
    this.right = null;
}

//: Remove node from tree
BSTree.prototype.remove = function(val) {
    var runner = this.root;
    if (runner.value == val) {
        if (runner.left == null && runner.right == null) {
            this.root = null;
            return this;
        } else if (runner.left == null && runner.right != null) {
            this.root = runner.right;
            return this;
        } else if (runner.left != null && runner.right == null) {
            this.root = runner.left;
            return this;
        } else {
            var temp = runner.left;
            var attach = runner.right.minNode();
            attach.left = temp;
            this.root = runner.right;
            return this;
        }
    } else {
        runner.pop(val);
        return this;
    }
}

//: Pop function for node
BSNode.prototype.pop = function(val) {
    if (this.value > val) {
        if (this.left == null) {
            console.log("value not found");
            return this;
        }
        var runner = this.left;
        if (runner.value == val) {
            if (runner.left == null && runner.right == null) {
                this.left = null;
                return this;
            } else if (runner.left == null && runner.right != null) {
                this.left = runner.right;
                return this;
            } else if (runner.left != null && runner.right == null) {
                this.left = runner.left;
                return this;
            } else {
                var temp = runner.left;
                var attach = runner.right.minNode();
                attach.left = temp;
                this.left = runner.right;
                return this;
            }
        } else {
            return runner.pop(val);
        }
    } else {
        if (this.right == null) {
            console.log("value not found");
            return this;
        }
        var runner = this.right;
        if (runner.value == val) {
            if (runner.left == null && runner.right == null) {
                this.right = null;
                return this;
            } else if (runner.left == null && runner.right != null) {
                this.right = runner.right;
                return this;
            } else if (runner.left != null && runner.right == null) {
                this.right = runner.left;
                return this;
            } else {
                var temp = runner.left;
                var attach = runner.right.minNode();
                attach.left = temp;
                this.right = runner.right;
                return this;
            }
        } else {
            return runner.pop(val);
        }
    }
}

//: Helper function to find Node of minimum value and return it
BSNode.prototype.minNode = function() {
    var runner = this;
    if (runner.left === null) {
        return runner;
    }
    var runner = runner.left;
    return runner.minNode();
}

//: Top
var a = new BSNode(5);
//: Left side of tree
var b = new BSNode(4);
var c = new BSNode(3);
var d = new BSNode(2);
var e = new BSNode(1);
a.left = c;
c.left = e;
c.right = b;
e.right = d;
//: Right side of tree
var f = new BSNode(8);
var g = new BSNode(7);
var h = new BSNode(6);
var i = new BSNode(10);
var j = new BSNode(9);
var k = new BSNode(11);
a.right = f;
f.left = g;
f.right = i;
g.left = h;
i.left = j;
i.right = k;

//: Initialize tree
var tree = new BSTree();
tree.root = a;

tree.remove(8);
console.log(tree.root.right);
