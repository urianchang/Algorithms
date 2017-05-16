/*
SLStack: Size

Return the number of stacked values.
*/

const Node = require('./_NodeSLL');

function SLStack() {
    this.head = null;
}

SLStack.prototype.size = function() {
    if (!this.head) {
        return 0;
    }
    var count = 0;
    var runner = this.head;
    while (runner) {
        count++;
        runner = runner.next;
    }
    return count;
}

var stack1 = new SLStack();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
// console.log(stack1.size());
node1.next = node2;
node2.next = node3;
stack1.head = node1;
console.log(stack1.size());
