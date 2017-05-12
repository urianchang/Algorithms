//: Stack Implementation based on Array

function ArrStack() {
    this.values = [];
}

//: Add value to stack
ArrStack.prototype.push = function(val) {
    this.values.push(val);
    console.log(`${val} has been added to the stack`);
    return this;
}

//: Remove and return top value of stack
ArrStack.prototype.pop = function() {
    var topVal = this.values.pop();
    console.log(`${topVal} has been removed from the stack`);
    return topVal;
}

//: Return stack's top value
ArrStack.prototype.top = function() {
    var topVal = this.values[this.values.length - 1];
    console.log(`${topVal} is the stack's top value`);
    return topVal;
}

//: Check if given val is within the stack.
ArrStack.prototype.contains = function(val) {
    if (this.values.length === 0) {
        console.log("The stack is empty");
        return this;
    }
    for (var idx = 0; idx < this.values.length; idx++) {
        if (this.values[idx] === val) {
            console.log(`${val} is within the stack`);
            return this;
        }
    }
    console.log(`${val} is NOT within the stack`);
    return this;
}

//: Check if stack is empty
ArrStack.prototype.isEmpty = function() {
    if (this.values.length === 0) {
        console.log("The stack is empty");
    } else {
        console.log("The stack is NOT empty");
    }
    return this;
}

//: Return size of stack
ArrStack.prototype.size = function() {
    console.log(`Stack size: ${this.values.length}`);
    return this.values.length;
}

module.exports = SLQueue;
