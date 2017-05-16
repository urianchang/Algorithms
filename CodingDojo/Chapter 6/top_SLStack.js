/*
SLStack: Top

Return (not remove) the stack's top value.
*/
const Node = require('./_NodeSLL');

function SLStack() {
    this.head = null;
}

SLStack.prototype.top = function() {
    if (!this.head) {
        console.log("The stack is empty");
        return null;
    }
    if (this.head.next === null) {
        return this.head;
    }
    var runner = this.head;
    while (runner.next) {
        runner = runner.next;
    }
    return runner;
}

var stack1 = new SLStack();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
stack1.head = node1;
console.log(stack1.top());
