/*
List: Remove Front

Given a pointer to the first node in a list,
remove the head node and return the new list head
node. If list is empty, return null.
*/

//Node functions
function ListNode(value) {
  this.val = value;
  this.next = null;
  return this;
}
function sLinkedList() {
  this.head = null;
  return this;
}

//Remove Front function
function rmFront(LL) {
    LL.head = LL.head.next;
    return LL.head;
}

//Create the list
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

console.log(rmFront(list1));
console.log(rmFront(list2));
