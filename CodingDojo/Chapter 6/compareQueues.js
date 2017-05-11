/*
SLQueue: Compare Queues

Given two SLQueue objects, create a standalone
function that returns whether they are equal.
Queues are equal only if they have equal elements
in identical order. Allocate no other object,
and return the queues in their original condition
upon exit.
*/

const Node = require('./_NodeSLL');
const SLQueue = require('./_SLQueue');

function compare(q1, q2) {
    if (!q1.head && !q2.head) {
        return true;
    }
    if (q1.size() != q2.size()) {
        return false;
    }
    var runner1 = q1.head;
    var runner2 = q2.head;
    while (runner1 && runner2) {
        if (runner1.val != runner2.val) {
            return false;
        }
        runner1 = runner1.next;
        runner2 = runner2.next;
    }
    return true;
}

var Q1 = new SLQueue();
var Q2 = new SLQueue();
//: Compare empty queues
console.log(compare(Q1, Q2));   // true

var node1= new Node(1);
Q1.head = node1;

//: Compare non-equal queues
console.log(compare(Q1, Q2));   // false

var node1a = new Node(1);
Q2.head = node1a;

//: Compare equal elements and identical order queues
console.log(compare(Q1, Q2));   // true

var node2 = new Node(2);
Q1.head.next = node2;
var node2a = new Node(2);
node2a.next = node1a;
Q2.head = node2a;

//: Compare equal elements but not identical order queues
console.log(compare(Q1, Q2));   // false
