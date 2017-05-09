/*
Recursive List Length

Given first node of a singly linked list, create
a recursive function that returns number of nodes
in that list. Assume list contains no loops and is
short enough that you will not "blow your stack".
*/

function listLength(node) {
    if (node.next === null) {
        return 1;
    }
    return 1 + listLength(node.next);
}

function SLL() {
    this.head = null;
}

function Node(val) {
    this.val = val;
    this.next = null;
}

//: Create singly linked list
var list = new SLL();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
var node4 = new Node(4);
node1.next = node2;
node2.next = node3;
node3.next = node4;
list.head = node1;

//: Run the function
console.log(listLength(list.head));
