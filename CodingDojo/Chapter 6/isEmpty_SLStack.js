/*
SLStack: Is Empty

Return whether the stack is empty.
*/

const Node = require('./_NodeSLL');

function SLStack() {
    this.head = null;
}

SLStack.prototype.isEmpty = function() {
    if (!this.head) {
        return true;
    }
    return false;
}

var stack1 = new SLStack();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
console.log(stack1.isEmpty());
node1.next = node2;
node2.next = node3;
stack1.head = node1;
console.log(stack1.isEmpty());
