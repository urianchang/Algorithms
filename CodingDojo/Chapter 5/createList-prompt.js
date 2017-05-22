/*
Create SList (prompt):

Create an SList with values entered.
Use the prompt function to gather values
one value at a time from the user, putting
each into a ListNode that you add to the end
of the list. When the user hits [Cancel],
return the list that you have created.
*/

//: List Node
function ListNode(val) {
    this.val = val;
    this.next = null;
}

//: Singly-linked List
function SLList() {
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

//: Create list
var SLL = new SLList();

//: Ask for user input
var response = prompt("Enter value for list node: ");
while (response) {
    var newNode = new ListNode(response);
    if (!SLL.head) {
        SLL.head = newNode;
    } else {
        var runner = SLL.head;
        while (runner.next) {
            runner = runner.next;
        }
        runner.next = newNode;
    }
    var response = prompt("Enter value for list node: ");
}

//: Display nodes in list (check)
SLL.display();
