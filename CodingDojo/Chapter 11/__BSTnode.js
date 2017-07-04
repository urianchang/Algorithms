//: BST Node object

module.exports = function(value) {
    this.val = value;
    this.left = null;
    this.right = null;
    this.count = 1;
    return this;
}
