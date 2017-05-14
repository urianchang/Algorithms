/*
SLStack: Push

Create push(val) that adds val to our stack.
*/

const Node = require('./_NodeSLL');

function SLStack() {
    this.head = null;
}

SLStack.prototype.push = function(val) {
    var node = new Node(val);
    if (!this.head) {
        this.head = node;
        console.log(`${val} has been added to the stack`);
        return this;
    }
    var runner = this.head;
    while (runner.next) {
        runner = runner.next;
    }
    runner.next = node;
    console.log(`${val} has been added to the stack`);
    return this;
}

var stack1 = new SLStack();
var node1 = new Node(1);
var node2 = new Node(2);
node1.next = node2;
stack1.head = node1;
stack1.push(3);
console.log(stack1);
