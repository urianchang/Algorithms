/*
SLQueue: Size

Create SLQueue method size() that returns the
number of values in our queue.
*/

const Node = require('./_NodeSLL');

function SLQueue() {
    var head = null;
    var tail = null;
}

SLQueue.prototype.size = function() {
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

var q = new SLQueue();
var node1 = new Node(1);
var node2 = new Node(2);
console.log(`Size of queue: ${q.size()}`);
q.head = node1;
console.log(`Size of queue: ${q.size()}`);
node1.next = node2;
console.log(`Size of queue: ${q.size()}`);
