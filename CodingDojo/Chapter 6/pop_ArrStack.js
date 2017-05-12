/*
ArrStack: Pop

Create pop() to remove and return the top val.
*/

function ArrStack() {
    this.values = [];
}

ArrStack.prototype.push = function(val) {
    this.values.push(val);
    console.log(`${val} has been added to the stack`);
    return this;
}

ArrStack.prototype.pop = function() {
    var topVal = this.values.pop();
    console.log(`${topVal} has been removed from the stack`);
    return topVal;
}

var stack = new ArrStack();
stack.push(1).push(2);
stack.pop();
