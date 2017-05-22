//: Singly-linked List

const Node = require('./_NodeSLL');

function SLList() {
    this.head = null;
}

//: Add List Node to the back of the list
SLList.prototype.addBack = function(val) {
    var newNode = new ListNode(val);
    var n = this.head;
    while (n.next) {
      n = n.next;
    }
    n.next = newNode;
    return this;
}

//: Return last value
SLList.prototype.lastValue = function() {
    var N = this.head;
    while (N.next) {
      N = N.next
    }
    return N.val;
}

//: Display all nodes in list
SLList.prototype.display = function() {
    var N = this.head;
    var string = "Node values in this list: ";
    while (N.next) {
      string += N.val + ", ";
      N = N.next;
    }
    string += N.val
    console.log(string);
    return this;
}

module.exports = SLList;
