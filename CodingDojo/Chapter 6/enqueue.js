/*
SLQueue: Enqueue

Create SLQueue method enqueue(val) to add
the given value to the end of our queue. Remember
SLQueue uses a singly linked list (not an array).
*/

function Node(val) {
    this.val = val;
    this.next = null;
}

function SLQueue() {
    var head = null;
    var tail = null;
}

SLQueue.prototype.enqueue = function(val) {
    var newNode = new Node(val);
    if (!this.head) {
        this.head = newNode;
    } else {
        var runner = this.head;
        while (runner.next) {
            runner = runner.next;
        }
        runner.next = newNode;
    }
}

var q = new SLQueue();
var node1 = new Node(1);
var node2 = new Node(2);
q.head = node1;
node1.next = node2;
console.log('Before', q);
q.enqueue(42);
console.log('After', q);
