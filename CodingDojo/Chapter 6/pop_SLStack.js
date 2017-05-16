/*
SLStack: Pop

Create pop() to remove and return the top val.
*/

const Node = require('./_NodeSLL');

function SLStack() {
    this.head = null;
}

SLStack.prototype.pop = function() {
    if (!this.head) {
        console.log("The stack is empty");
        return null;
    }
    if (this.head.next === null) {
        var removedNode = this.head;
        this.head = null;
        return removedNode;
    }
    var runner = this.head;
    while (runner.next.next) {
        runner = runner.next;
    }
    var removedNode = runner.next;
    runner.next = null;
    return removedNode;
}

var stack1 = new SLStack();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
stack1.head = node1;
console.log(stack1.pop());
console.log(stack1);
