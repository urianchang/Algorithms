/*
SLQueue: Contains

Create SLQueue method contains(val) to return
whether given value is found within the queue.
*/

function Node(val) {
    this.val = val;
    this.next = null;
}

function SLQueue() {
    var head = null;
    var tail = null;
}

SLQueue.prototype.contains = function(val) {
    if (!this.head) {
        return "Queue is empty";
    }
    var runner = this.head;
    while (runner) {
        if (runner.val === val) {
            return `${val} is in the queue`;
        }
        runner = runner.next;
    }
    return `${val} is NOT in the queue`;
}

//: Set up the queue
var q = new SLQueue();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
q.head = node1;

console.log(q.contains(42));
console.log(q.contains(3));
