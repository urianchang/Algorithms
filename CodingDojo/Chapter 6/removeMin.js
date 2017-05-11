/*
SLQueue: Remove Min

Create a standalone function to remove SLQueue's
lowest value, otherwise leaving values in the same
sequence. Use only local variables; allocate no other
objects. Remove all duplicates of this value.
*/

const Node = require('./_NodeSLL');
const SLQueue = require('./_SLQueue');

function removeMin(q) {
    if (!q.head) {
        return "Queue is empty";
    }
    //: Find min
    var min = q.head.val;
    var runner = q.head;
    while (runner) {
        if (runner.val < min) {
            min = runner.val;
        }
        runner = runner.next;
    }
    //: Remove node(s) with min value
    var runner2 = q.head;
    while (runner2.next) {
        if (runner2.next.val === min) {
            runner2.next = runner2.next.next;
        } else {
            runner2 = runner2.next;
        }
    }
    if (q.head.val === min) {
        q.head = q.head.next;
    }
    return "Removed min value(s) from queue";
}

var Q = new SLQueue();
// console.log(removeMin(Q));
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
var node1a = new Node(1);
var node1b = new Node(1);
// node1.next = node2;
// node2.next = node3;
// node3.next = node1a;
// node1a.next = node1b;
node3.next = node1;
node1.next = node1a;
node1a.next = node1b;
node1b.next = node2;
Q.head = node3;
console.log(`Queue before: ${Q.size()}`);
console.log(removeMin(Q));
console.log(`Queue after: ${Q.size()}`);
