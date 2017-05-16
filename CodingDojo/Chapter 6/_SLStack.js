//: Stack implementation based on Singly linked list

function SLStack() {
    this.head = null;
}

//: Add value to stack
SLStack.prototype.push = function(val) {
    var node = new Node(val);
    if (!this.head) {
        this.head = node;
        console.log(`${val} has been added to the stack`);
        return this;
    }
    var runner = this.head;
    while (runner.next) {
        runner = runner.next;
    }
    runner.next = node;
    console.log(`${val} has been added to the stack`);
    return this;
}

//: Remove and return top value of stack
SLStack.prototype.pop = function() {
    if (!this.head) {
        console.log("The stack is empty");
        return null;
    }
    if (this.head.next === null) {
        var removedNode = this.head;
        this.head = null;
        return removedNode;
    }
    var runner = this.head;
    while (runner.next.next) {
        runner = runner.next;
    }
    var removedNode = runner.next;
    runner.next = null;
    return removedNode;
}

//: Return stack's top value
SLStack.prototype.top = function() {
    if (!this.head) {
        console.log("The stack is empty");
        return null;
    }
    if (this.head.next === null) {
        return this.head;
    }
    var runner = this.head;
    while (runner.next) {
        runner = runner.next;
    }
    return runner;
}

//: Return whether given value is in stack
SLStack.prototype.contains = function(val) {
    if (!this.head) {
        return false;
    }
    var runner = this.head;
    while (runner) {
        if (runner.val === val) {
            return true;
        }
        runner = runner.next;
    }
    return false;
}

//: Return whether stack is empty
SLStack.prototype.isEmpty = function() {
    if (!this.head) {
        return true;
    }
    return false;
}

//: Return number of stacked values
SLStack.prototype.size = function() {
    if (!this.head) {
        return 0;
    }
    var count = 0;
    var runner = this.head;
    while (runner) {
        count++;
        runner = runner.next;
    }
    return count;
}

module.exports = SLStack;
