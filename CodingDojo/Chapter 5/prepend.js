/*
SLList: Prepend Val

Create prependVal(ListNode, val, before) to insert
a new ListNode with val immediately before the node
containing before (or at end, if no node contains before).
Return the new list.
*/

const Node = require('./_NodeSLL');

function SLList() {
    this.head = null;
}

//: Display all nodes in list
SLList.prototype.display = function() {
    var N = this.head;
    var string = "Node values in this list: ";
    while (N.next) {
      string += N.val + ", ";
      N = N.next;
    }
    string += N.val
    console.log(string);
    return this;
}

SLList.prototype.prepend = function(val, target) {
    var newNode = new Node(val);
    if (!this.head) {
        this.head = newNode;
    } else {
        var runner = this.head;
        if (runner.val === target) {
            var temp = this.head;
            this.head = newNode;
            newNode.next = temp;
        } else {
            while (runner.next) {
                if (runner.next.val === target) {
                    var temp = runner.next;
                    runner.next = newNode;
                    newNode.next = temp;
                    break;
                }
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }
    return this;
}

var SLL = new SLList();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
// SLL.prepend(0, 1);
SLL.head = node1;
SLL.prepend(0, 2);
SLL.display();
