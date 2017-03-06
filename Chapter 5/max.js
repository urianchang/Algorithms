/*
SList: Max

Create function max(node) to return list's largest value.
*/

//Node functions
function ListNode(value) {
  this.val = value;
  this.next = null;
  this.max = function () {
    var max = this.val;
    var N = this.next;
    while (N) {
      if (N.val > max) {
        max = N.val;
      }
      N = N.next;
    }
    console.log("Maximum value: " + max);
    return this;
  }
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

node1.max();
