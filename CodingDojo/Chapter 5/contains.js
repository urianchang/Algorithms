/*
List: Contains

Given a pointer to a ListNode and a val,
return whether val is found in any node within the list.
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

//Contains function
function contains(LL, val) {
    var N = LL.head;
    while (N) {
      if (N.val == val){
        return true;
      }
      N = N.next;
    }
    return false;
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

console.log(contains(list1, 7));
console.log(contains(list2, 1));
