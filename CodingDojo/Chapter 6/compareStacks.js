/*
Compare Stacks:

Given two Stack objects, create a standalone function to return
whether they are equal. Stacks are equal only if they have equal
elements in identical order. You can use an additional third
Stack for storage; you will need it because you must return
the given Stacks to their original condition upon exit.
*/

const Node = require('./_NodeSLL');
const SLStack = require('./_SLStack');

function compare(s1, s2) {
    if (!s1.head && !s2.head) {
        return true;
    }
    if (s1.size() != s2.size()) {
        return false;
    }
    var runner1 = s1.head;
    var runner2 = s2.head;
    while(runner1 && runner2) {
        if (runner1.val != runner2.val) {
            return false;
        }
        runner1 = runner1.next;
        runner2 = runner2.next;
    }
    return true;
}

var S1 = new SLStack();
var S2 = new SLStack();
//: Compare empty stacks
console.log(compare(S1, S2));   // true

var node1= new Node(1);
S1.head = node1;

//: Compare non-equal stacks
console.log(compare(S1, S2));   // false

var node1a = new Node(1);
S2.head = node1a;

//: Compare equal elements and identical order stacks
console.log(compare(S1, S2));   // true

var node2 = new Node(2);
S1.head.next = node2;
var node2a = new Node(2);
node2a.next = node1a;
S2.head = node2a;

//: Compare equal elements but not identical order stacks
console.log(compare(S1, S2));   // false
