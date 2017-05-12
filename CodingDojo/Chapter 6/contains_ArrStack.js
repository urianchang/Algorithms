/*
ArrStack: Contains

Return whether given val is within the stack.
*/

function ArrStack() {
    this.values = [];
}

ArrStack.prototype.push = function(val) {
    this.values.push(val);
    console.log(`${val} has been added to the stack`);
    return this;
}

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

var stack = new ArrStack();
stack.push(1).push(2);
stack.contains(1);
stack.contains(4);
var stack2 = new ArrStack();
stack2.contains(1);
