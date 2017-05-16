/*
SLStack: Contains

Return whether given value is within the stack.
*/

const Node = require('./_NodeSLL');

function SLStack() {
    this.head = null;
}

SLStack.prototype.contains = function(val) {
    if (!this.head) {
        return false;
    }
    var runner = this.head;
    while (runner) {
        if (runner.val === val) {
            return true;
        }
        runner = runner.next;
    }
    return false;
}

var stack1 = new SLStack();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
console.log(stack1.contains(1));
node1.next = node2;
node2.next = node3;
stack1.head = node1;
console.log(stack1.contains(3));
