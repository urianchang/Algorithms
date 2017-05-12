/*
ArrStack: Top

Return (not remove) the stack's top value.
*/

function ArrStack() {
    this.values = [];
}

ArrStack.prototype.push = function(val) {
    this.values.push(val);
    console.log(`${val} has been added to the stack`);
    return this;
}

ArrStack.prototype.top = function() {
    var topVal = this.values[this.values.length - 1];
    console.log(`${topVal} is the stack's top value`);
    return topVal;
}

var stack = new ArrStack();
stack.push(1).push(2);
stack.top();
