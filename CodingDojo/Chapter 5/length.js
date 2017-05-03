/*
SList: Length

Create a function that accepts a pointer to the first list node,
and returns number of nodes in that SList.
*/

//Node functions
function ListNode(value) {
  this.val = value;
  this.next = null;
}
function sLinkedList() {
  this.head = null;
}

//Length function
function length(LL) {
  var N = LL.head;
  var count = 0;
  while (N) {
    count++;
    N = N.next;
  }
  return count;
}

//Create the list(s)
var list1 = new sLinkedList();
var node1 = new ListNode(6);
var node2 = new ListNode(7);
var node3 = new ListNode(8);
list1.head = node1;
node1.next = node2;
node2.next = node3;

console.log(length(list1));
