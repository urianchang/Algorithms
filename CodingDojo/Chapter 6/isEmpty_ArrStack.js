/*
ArrStack: Is Empty

Return whether the stack is empty.
*/

function ArrStack() {
    this.values = [];
}

ArrStack.prototype.push = function(val) {
    this.values.push(val);
    console.log(`${val} has been added to the stack`);
    return this;
}

ArrStack.prototype.isEmpty = function() {
    if (this.values.length === 0) {
        console.log("The stack is empty");
    } else {
        console.log("The stack is NOT empty");
    }
    return this;
}

var stack = new ArrStack();
stack.push(1).push(2);
stack.isEmpty();
var stack2 = new ArrStack();
stack2.isEmpty();
