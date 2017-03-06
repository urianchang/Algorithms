/*
SList: Display

Create display(node) for debugging that returns
a string containing all list values. Build what
you wish console.log(myList) did!
*/

//Node functions
function ListNode(value) {
  this.val = value;
  this.next = null;
}

function sLinkedList() {
  this.head = null;
  this.display = function () {
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
}

//Create the list(s)
var list1 = new sLinkedList();
var node1 = new ListNode(6);
var node2 = new ListNode(7);
var node3 = new ListNode(8);
list1.head = node1;
node1.next = node2;
node2.next = node3;

list1.display();
