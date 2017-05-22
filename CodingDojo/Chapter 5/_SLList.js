//: Singly-linked List

const Node = require('./_NodeSLL');

function SLList() {
    this.head = null;
}

//: Add List Node to the back of the list
SLList.prototype.addBack = function(val) {
    var newNode = new ListNode(val);
    var n = this.head;
    while (n.next) {
      n = n.next;
    }
    n.next = newNode;
    return this;
}

//: Return last value
SLList.prototype.lastValue = function() {
    var N = this.head;
    while (N.next) {
      N = N.next
    }
    return N.val;
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

//: Insert value before given value. Return new list.
SLList.prototype.prepend = function(val, target) {
    var newNode = new Node(val);
    if (!this.head) {
        this.head = newNode;
    } else {
        var runner = this.head;
        if (runner.val === target) {
            var temp = this.head;
            this.head = newNode;
            newNode.next = temp;
        } else {
            while (runner.next) {
                if (runner.next.val === target) {
                    var temp = runner.next;
                    runner.next = newNode;
                    newNode.next = temp;
                    return this;
                }
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }
    return this;
}

//: Remove value and return list
SLList.prototype.remove = function(val) {
    if (!this.head) {
        console.log("List is empty");
        return this;
    } else {
        if (this.head.val === val) {
            this.head = this.head.next;
            console.log(`${val} has been removed`);
            return this;
        } else {
            var runner = this.head;
            while (runner.next) {
                if (runner.next.val === val) {
                    runner.next = runner.next.next;
                    console.log(`${val} has been removed`);
                    return this;
                }
                runner = runner.next;
            }
            console.log(`${val} cannot be found in the list`);
            return this;
        }
    }
}

//: Add new List Node after given value
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

module.exports = SLList;
