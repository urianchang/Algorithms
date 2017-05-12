/*
ArrStack: Size

Return the number of stacked values.
*/

function ArrStack() {
    this.values = [];
}

ArrStack.prototype.push = function(val) {
    this.values.push(val);
    console.log(`${val} has been added to the stack`);
    return this;
}

ArrStack.prototype.size = function() {
    console.log(`Stack size: ${this.values.length}`);
    return this;
}

var stack = new ArrStack();
stack.push(1).push(2);
stack.size();
