/*
SList: Remove Val

Create removeVal(ListNode, val). Given a pointer
to the head ListNode, remove the node with the
given val. Return the new list. What will
you do if val is not found?
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

SLList.prototype.remove = function(val) {
    if (!this.head) {
        console.log("List is empty");
        return this;
    } else {
        if (this.head.val === val) {
            this.head = this.head.next;
            console.log(`${val} has been removed`);
            return this;
        } else {
            var runner = this.head;
            while (runner.next) {
                if (runner.next.val === val) {
                    runner.next = runner.next.next;
                    console.log(`${val} has been removed`);
                    return this;
                }
                runner = runner.next;
            }
            console.log(`${val} cannot be found in the list`);
            return this;
        }
    }
}

var SLL = new SLList();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
SLL.head = node1;
SLL.display();
SLL.remove(10);
SLL.display();
