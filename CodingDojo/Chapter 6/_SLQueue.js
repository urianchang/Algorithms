//: Singly Linked List Queue

function SLQueue() {
    var head = null;
    var tail = null;
}

//: Enqueue / Add a value to the queue
SLQueue.prototype.enqueue = function(val) {
    var newNode = new Node(val);
    if (!this.head) {
        this.head = newNode;
    } else {
        var runner = this.head;
        while (runner.next) {
            runner = runner.next;
        }
        runner.next = newNode;
    }
    console.log(`${val} has been added to the queue`);
    return this;
}

//: Dequeue / Remove and return the value at the front of the queue
SLQueue.prototype.dequeue = function() {
    if (!this.head) {
        console.log("Queue is empty");
        return this;
    }
    var removedNode = this.head;
    this.head = this.head.next;
    console.log(`Dequeued value: ${removedNode.val}`);
    return removedNode.val;
}

//: Return the value at the front of the queue
SLQueue.prototype.front = function() {
    if (!this.head) {
        console.log("Queue is empty");
        return null;
    }
    console.log(`Value at front of queue: ${this.head.val}`);
    return this.head.val;
}

//: Check if queue is empty
SLQueue.prototype.isEmpty = function() {
    if (!this.head) {
        console.log("Queue is empty");
        return this;
    }
    console.log("Queue is NOT empty");
    return this;
}

//: Return the size of the queue
SLQueue.prototype.size = function() {
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

//: Check if queue contains a given value
SLQueue.prototype.contains = function(val) {
    if (!this.head) {
        console.log("Queue is empty");
        return this;
    }
    var runner = this.head;
    while (runner) {
        if (runner.val === val) {
            console.log(`${val} is in the queue`);
            return this;
        }
        runner = runner.next;
    }
    console.log(`${val} is NOT in the queue`);
    return this;
}

module.exports = SLQueue;
