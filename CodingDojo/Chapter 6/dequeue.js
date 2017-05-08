/*
SLQueue: Dequeue

Create SLQueue method dequeue() to remove and return
value at the front of the queue. Remember SLQueue uses
singly linked list (not array).
*/

function Node(val) {
    this.val = val;
    this.next = null;
}

function SLQueue() {
    var head = null;
    var tail = null;
}

SLQueue.prototype.dequeue = function() {
    if (!this.head) {
        return "Queue is empty";
    }
    var removedNode = this.head;
    this.head = this.head.next;
    return `Dequeued value: ${removedNode.val}`;
}

//: Set up the queue
var q = new SLQueue();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
q.head = node1;

console.log('Before:', q);
console.log(q.dequeue());
console.log('After:', q);
