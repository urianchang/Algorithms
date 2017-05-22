/*
SList: Append Val

Create appendVal(list, val, after) that inserts
a new ListNode containing given val immediately
after the node containing after (or at end,
if after not found). Return the new list.
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

SLList.prototype.append = function(val, target) {
    var newNode = new Node(val);
    if (!this.head) {
        this.head = newNode;
    } else {
        var runner = this.head;
        while (runner.next) {
            if (runner.val === target) {
                var temp = runner.next;
                runner.next = newNode;
                newNode.next = temp;
                return this;
            }
            runner = runner.next;
        }
        runner.next = newNode;
    }
    return this;
}

var SLL = new SLList();
var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
node1.next = node2;
node2.next = node3;
// SLL.append(9, 2);
SLL.head = node1;
SLL.display();
SLL.append(10, 2);
SLL.display();
