/*
SList: Move Max to Back

Create a standalone function that locates
the maximum value in a linked list, and moves
that node to the back of the list. Return
the new list, with all nodes still present,
and all (except for the new last node) in
their original order.
*/

//Node functions
function ListNode(value) {
  this.val = value;
  this.next = null;
  //Find max value
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
  //Find min value
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
  //Find average value
  this.average = function () {
    var sum = this.val;
    var count = 1;
    var N = this.next;
    while (N) {
      count++;
      sum += N.val;
      N = N.next;
    }
    console.log("Average: " + (sum/count));
    return this;
  }
}

function sLinkedList() {
  this.head = null;
  //Display all node values
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
  //Display the last value in the list
  this.lastVal = function () {
    var N = this.head;
    while (N.next) {
      N = N.next
    }
    console.log("The last value in the list is: ", N.val);
    return this;
  }
  //Create ListNode with value and add to the end of the list
  this.addBack = function(val) {
    var newNode = new ListNode(val);
    var n = this.head;
    while (n.next) {
      n = n.next;
    }
    n.next = newNode;
    return this;
  }
}

//Function to move min to Front
function maxToBack(sLinkedList) {
  var max = sLinkedList.head;
  var N = sLinkedList.head;
  var prevN = sLinkedList.head;
  while (N.next) {
    if (N.next.val > max.val) {
      max = N.next;
      prevN = N;
    }
    N = N.next;
  }
  if (max == sLinkedList.head) {
    sLinkedList.head = max.next;
    N.next = max;
    max.next = null;
  } else {
    prevN.next = max.next;
    N.next = max;
    max.next = null;
  }
  return sLinkedList;
}

//Create the list(s)
var list1 = new sLinkedList();
var node1 = new ListNode(6);
var node2 = new ListNode(4);
var node3 = new ListNode(5);
list1.head = node1;
node1.next = node2;
node2.next = node3;

console.log("Before...");
list1.display();
console.log("After...");
maxToBack(list1);
list1.display();
