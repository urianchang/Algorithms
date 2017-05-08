/*
SLQueue: Front

Create SLQueue method front() to return
the value at front of queue, without
removing it.
*/

function Node(val) {
    this.val = val;
    this.next = null;
}

function SLQueue() {
    var head = null;
    var tail = null;
}

SLQueue.prototype.front = function() {
    if (!this.head) {
        return "Queue is empty";
    }
    return `Value at front of queue: ${this.head.val}`;
}

//: Set up the queue
var q = new SLQueue();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
q.head = node1;

console.log(q.front());
