/*
SList: Back

Create a standalone function that removes the
last ListNode in the list and returns the new list.
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
}

//Remove Back function
function removeBack(list){
  var n = list.head;
  while (n.next.next) {
    n = n.next;
  }
  n.next = null;
  return list;
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

console.log("Before...");
list1.lastVal();
console.log("After...");
removeBack(list1);
list1.lastVal();
