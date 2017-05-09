/*
SLQueue: Is Empty

Create SLQueue method isEmpty() that
returns whether our queue contains no
values.
*/

function Node(val) {
    this.val = val;
    this.next = null;
}

function SLQueue() {
    var head = null;
    var tail = null;
}

SLQueue.prototype.isEmpty = function() {
    if (!this.head) {
        return "Queue is empty";
    }
    return "Queue is NOT empty";
}

//: Set up the queues
var q = new SLQueue();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
q.head = node1;

var q2 = new SLQueue();

console.log(q.isEmpty());   // not empty
console.log(q2.isEmpty());  // empty
