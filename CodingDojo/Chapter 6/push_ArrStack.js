/*
ArrStack: Push

Create push(val) that adds val to our stack.
*/

function ArrStack() {
    this.values = [];
}

ArrStack.prototype.push = function(val) {
    this.values.push(val);
    console.log(`${val} has been added to the stack`);
    return this;
}

var stack = new ArrStack();
stack.push(1).push(2);
