/*
SList: Min

Create min(node) to return list's smallest val.
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
  this.min = function () {
    var min = this.val;
    var N = this.next;
    while (N) {
      if (N.val < min) {
        min = N.val;
      }
      N = N.next;
    }
    console.log("Minimum value: " + min);
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

var list2 = new sLinkedList();
var node100 = new ListNode(100);
list2.head = node100;

node1.min();
node100.max();
